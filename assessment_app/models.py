from django.db import models


GROWTH_AREA_CHOICES = [
    ('communication', 'Communication'),
    ('leadership', 'Leadership'),
    ('technical', 'Technical Skills'),
    ('time_management', 'Time Management'),
    ('collaboration', 'Collaboration'),
    ('problem_solving', 'Problem Solving'),
    ('creativity', 'Creativity'),
    
]

COMMUNICATION_STYLE_CHOICES = [
    ('direct', 'Direct'),
    ('indirect', 'Indirect'),
    ('assertive', 'Assertive'),
    ('passive', 'Passive'),
    ('aggressive', 'Aggressive'),
   
]

ENERGY_PREFERENCE_CHOICES = [
    ('morning', 'Morning'),
    ('afternoon', 'Afternoon'),
]

DISTRACTION_LEVEL_CHOICES = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
]

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Assessment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    work_hours = models.IntegerField()
    time_management = models.IntegerField()
    distraction_level = models.CharField(max_length=10,
        choices=DISTRACTION_LEVEL_CHOICES,
        default='medium'
        )
    task_satisfaction = models.IntegerField()
    meeting_effectiveness = models.IntegerField()
    energy_preference = models.CharField(max_length=10,
        choices=ENERGY_PREFERENCE_CHOICES,
        default='morning')
    stress_level = models.IntegerField()
    work_life_balance = models.IntegerField()

    career_satisfaction = models.IntegerField()
    learning_motivation = models.IntegerField()
    biggest_challenge = models.TextField()
    growth_area = models.CharField(choices=GROWTH_AREA_CHOICES,
        default='communication')
    team_collaboration = models.IntegerField()
    communication_style = models.CharField(max_length=20,
        choices=COMMUNICATION_STYLE_CHOICES,
        default='direct')

    ai_summary = models.TextField(blank=True, null=True)
    ai_recommendations = models.TextField(blank=True, null=True)
    wellness_score = models.CharField(blank=True, null=True)
