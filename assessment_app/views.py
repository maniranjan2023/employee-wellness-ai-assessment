from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Assessment
from .forms import AssessmentForm
import requests
import re
import json
import urllib.parse
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse



# 🔐 Replace this with your actual API key
OPENAI_API_KEY=""

def generate_ai_insights(data):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    prompt = f"""
You are a highly skilled organizational psychologist and HR performance coach. Analyze the following employee assessment data and generate an insightful, structured evaluation.

Assessment Input:
{data}

Your response must be divided into the following three sections. Use clear markdown formatting with headings and bullet points where applicable.

---

### 1. 🧠 Personal Summary
Write a 3–4 sentence professional summary of the employee’s current state, focusing on:
- Emotional and mental well-being
- Productivity levels
- Communication or collaboration habits
- Any behavioral patterns or anomalies

Avoid generic statements—base your analysis directly on the data.

---

### 2. 📌 Top 3 Recommendations
List 3 specific, personalized, and actionable suggestions that:
- Address root causes or potential improvement areas
- Are realistic and within the employee’s role or control
- Promote measurable change in performance or well-being

Use bullet points and start each with a strong action verb.

---

### 3. 📊 Wellness Score
Give a score from **1 (low) to 10 (excellent)** for overall wellness and briefly explain:
- What factors contributed to this score?
- How can it be improved (if applicable)?

Ensure the explanation connects directly to the assessment findings.

---
Ensure your tone remains empathetic, constructive, and evidence-based.
make shure all the response in poitnwise manner in bullet point so that readibility is good.
"""

    payload = {
        "model": "gpt-4.1",  # or "gpt-4" if that's what you have access to
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful HR assistant generating insights from employee assessments."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.4,
        "max_tokens": 700
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            print("OpenAI API Error:", response.status_code)
            print(response.text)
            return "AI response could not be generated due to an error."
    except Exception as e:
        print("Request exception:", e)
        return "AI response could not be generated due to an exception."
    

def export_pdf_view(request, assessment_id):
    assessment = get_object_or_404(Assessment, id=assessment_id)
    question_labels = [
        "Work Hours", "Time Management", "Task Satisfaction", "Meeting Effectiveness",
        "Stress Level", "Work-Life Balance", "Career Satisfaction", "Learning Motivation",
        "Team Collaboration"
    ]
    responses = [
    int(assessment.work_hours) if assessment.work_hours is not None and str(assessment.work_hours).isdigit() else 0,
    int(assessment.time_management) if assessment.time_management is not None and str(assessment.time_management).isdigit() else 0,
    int(assessment.task_satisfaction) if assessment.task_satisfaction is not None and str(assessment.task_satisfaction).isdigit() else 0,
    int(assessment.meeting_effectiveness) if assessment.meeting_effectiveness is not None and str(assessment.meeting_effectiveness).isdigit() else 0,
    int(assessment.stress_level) if assessment.stress_level is not None and str(assessment.stress_level).isdigit() else 0,
    int(assessment.work_life_balance) if assessment.work_life_balance is not None and str(assessment.work_life_balance).isdigit() else 0,
    int(assessment.career_satisfaction) if assessment.career_satisfaction is not None and str(assessment.career_satisfaction).isdigit() else 0,
    int(assessment.learning_motivation) if assessment.learning_motivation is not None and str(assessment.learning_motivation).isdigit() else 0,
    int(assessment.team_collaboration) if assessment.team_collaboration is not None and str(assessment.team_collaboration).isdigit() else 0
]
    
    print("PDF Chart Data:", responses)
    # Generate QuickChart URL
    chart_config = {
        "type": "bar",
        "data": {
            "labels": question_labels,
            "datasets": [{
                "label": "Responses",
                "data": responses,
                "backgroundColor": "rgba(59, 130, 246, 0.5)",
                "borderColor": "rgba(59, 130, 246, 1)",
                "borderWidth": 1
            }]
        },
       
    }
    chart_url = "https://quickchart.io/chart?c=" + urllib.parse.quote(json.dumps(chart_config))

    context = {
        'assessment': assessment,
        'question_labels': question_labels,
        'responses': responses,
        'chart_url': chart_url,
    }
    template = get_template('report_pdf.html')
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="assessment_report_{assessment.id}.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response
def assessment_view(request):
    if request.method == 'POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.pop('name')
            email = form.cleaned_data.pop('email')

            employee, _ = Employee.objects.get_or_create(email=email, defaults={'name': name})
            assessment = form.save(commit=False)
            assessment.employee = employee

            ai_response = generate_ai_insights(form.cleaned_data)

            # Use regex to split by section headings
            summary = recommendations = wellness = ""
            sections = re.split(r'###\s*\d\.\s*[\w\s🧠📌📊]*', ai_response)
            if len(sections) >= 4:
                summary = sections[1].strip()
                recommendations = sections[2].strip()
                wellness = sections[3].strip()
            else:
                summary = ai_response

            # Remove all ** from the AI responses only (does not affect unrelated code)
            summary = re.sub(r'\*\*', '', summary)
            recommendations = re.sub(r'\*\*', '', recommendations)
            wellness = re.sub(r'\*\*', '', wellness)

            assessment.ai_summary = summary
            assessment.ai_recommendations = recommendations
            assessment.wellness_score = wellness

            assessment.save()
            return redirect('report', assessment.id)
    else:
        form = AssessmentForm()
    return render(request, 'assessment.html', {'form': form})

def report_view(request, assessment_id):
    
    assessment = get_object_or_404(Assessment, id=assessment_id)

    # Labels for numeric/categorical questions (customize as needed)
    question_labels = [
        "Work Hours",
        "Time Management",
        "Distraction Level",
        "Task Satisfaction",
        "Meeting Effectiveness",
        "Energy Preference",
        "Stress Level",
        "Work-Life Balance",
        "Career Satisfaction",
        "Learning Motivation",
        "Biggest Challenge",
        "Growth Area",
        "Team Collaboration",
        "Communication Style"
    ]

    # Numeric/categorical values for chart (convert categorical to string or numeric as needed)
    responses = [
        assessment.work_hours,
        assessment.time_management,
        assessment.distraction_level,      # categorical
        assessment.task_satisfaction,
        assessment.meeting_effectiveness,
        assessment.energy_preference,      # categorical
        assessment.stress_level,
        assessment.work_life_balance,
        assessment.career_satisfaction,
        assessment.learning_motivation,
        assessment.biggest_challenge,      # text, not suitable for chart
        assessment.growth_area,            # categorical
        assessment.team_collaboration,
        assessment.communication_style     # categorical
    ]

    # For charting, you may want only numeric fields:
    chart_labels = [
        "Work Hours",
        "Time Management",
        "Task Satisfaction",
        "Meeting Effectiveness",
        "Stress Level",
        "Work-Life Balance",
        "Career Satisfaction",
        "Learning Motivation",
        "Team Collaboration"
    ]
    chart_responses = [
        assessment.work_hours,
        assessment.time_management,
        assessment.task_satisfaction,
        assessment.meeting_effectiveness,
        assessment.stress_level,
        assessment.work_life_balance,
        assessment.career_satisfaction,
        assessment.learning_motivation,
        assessment.team_collaboration
    ]

    return render(
        request,
        'report.html',
        {
            'assessment': assessment,
            'question_labels': chart_labels,
            'responses': chart_responses,
        }
    )
