# 🧠 Employee-Wellness-Ai-Assessment Platform

A Django + PostgreSQL application that collects employee assessment data and generates AI-powered insights including summaries, recommendations, and wellness scores using OpenAI's GPT-4 API.

---

## 🚀 Features

* **Employee Assessment Form**: Captures productivity and personal development metrics.
* **PostgreSQL Integration**: Employee and assessment data stored in a relational database.
* **AI-Powered Insight Generation**:

  * Personal summary
  * Actionable recommendations
  * Wellness score with explanation
* **Insightful Report Display**: Structured, readable AI-generated feedback for each employee.

---

## 🧪 AI Model Choice and Reasoning

* **Model**: GPT-4
* **Reason**: Offers structured and contextually rich responses suitable for summarization and recommendation tasks.

---

## 🏆 Most Effective Prompt

```plaintext
Given the following employee assessment data:
{data}

1. Personal Summary (3-4 sentences)
2. Top 3 Recommendations (actionable)
3. Overall Wellness Score with a short explanation
```

---

## 🧱 One Challenge Overcome

Ensuring PostgreSQL database schema matched Django models precisely, especially for longer AI-generated text fields.

---

## ⏱ Time Spent

\~6-8 hours (including setup, development, prompt tuning, and testing)

---

## 🧑‍💻 Setup Instructions Summary

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/employee-ai-insight.git
cd employee-ai-insight
```

### 2. Create Virtual Environment

```bash
python -m venv env
# Linux/macOS	source env/bin/activate
# Windows	env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

* Create a PostgreSQL DB: `employee_ai`
* Edit `settings.py`:

```python
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'employee_ai',
    'USER': 'your_db_user',
    'PASSWORD': 'your_db_password',
    'HOST': 'localhost',
    'PORT': '5432',
  }
}
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the Server

```bash
python manage.py runserver
```

### 7. Access Application

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 8. Configure OpenAI Key

Edit `views.py`:

```python
headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer YOUR_OPENAI_API_KEY"
}
```

---

## 📁 Folder Structure

```
employee-ai-insight/
├── assessment_app/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       ├── assessment.html
│       └── report.html
├── r1/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🔒 .gitignore Recommendations

```
.env
__pycache__/
db.sqlite3
*.pyc
env/
*.log
*.idea/
*.vscode/
*.DS_Store
```

---

## 📽 Live Demo Video (To Record)

* Fill out the form
* Generate AI insights
* Show report page with AI output

---

## 📬 GitHub Repository Link

[https://github.com/maniranjan2023/employee-wellness-ai-assessment]([https://github.com/maniranjan2023/employee-wellness-ai-assessment](https://github.com/maniranjan2023/employee-wellness-ai-assessment)


