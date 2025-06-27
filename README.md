# 🧠 Employee AI Insight Tool

A web-based HR assistant that collects employee assessment data and generates AI-powered personalized summaries, actionable recommendations, and a wellness score using GPT-4.

---

## 🚀 Features

- 📝 **Assessment Form**  
  Collects productivity and personal development feedback from employees.

- 🧑‍💼 **Employee Mapping**  
  Each assessment is linked to a specific employee by email (auto-creates if not found).

- 🤖 **AI Insight Generator (OpenAI GPT-4)**  
  Automatically generates:
  - Personal Summary (3–4 sentences)
  - Top 3 Recommendations
  - Overall Wellness Score

- 📄 **Beautiful Report Page**  
  View structured results styled with Tailwind CSS.

- 🛢️ **PostgreSQL Database Integration**  
  All employees and their assessments are stored in a PostgreSQL database.

---

## 📂 Folder Structure

```
r1/
│
├── assessment_app/
│   ├── migrations/
│   ├── templates/
│   │   ├── assessment.html
│   │   └── report.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── r1/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/
│   └── css/
│       └── input.css   # Tailwind input file
│       └── output.css  # Tailwind output file
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 🔧 Prerequisites

- Python 3.8+
- PostgreSQL
- Node.js + Tailwind CSS

---

### 📦 1. Clone and Setup Virtual Environment

```bash
git clone https://github.com/your-username/employee-ai-insight-tool.git
cd employee-ai-insight-tool
python -m venv env
.\env\Scriptsctivate  # Windows
# OR
source env/bin/activate  # macOS/Linux
```

---

### 📦 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🛠️ 3. PostgreSQL Database Setup

Login to PostgreSQL and run:

```sql
CREATE DATABASE employee_ai;
CREATE USER <XXXXXXXX> WITH PASSWORD 'XXXXXXXX';
GRANT ALL PRIVILEGES ON DATABASE employee_ai TO <XXXXXXXXXX>;
```

---

### ⚙️ 4. Tailwind CSS Setup

```bash
npm install -D tailwindcss
npx tailwindcss init
```

Use this command to build Tailwind CSS:

```bash
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch
```

---

### 🧠 5. Add OpenAI Key

In `views.py`, set your API key directly (if not using `.env`):

```python
OPENAI_API_KEY = "sk-xxxx..."
```

---

### 🧱 6. Migrations & Superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
npm run watch:css 
```

---

### ▶️ 7. Run the Server

```bash
python manage.py runserver
```

---

### 🌐 Access the App

Go to [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## ✨ Sample Output

- 👤 Employee: John Doe  
- 📌 Recommendations: Prioritize time-blocking, take short breaks, improve communication  
- 📊 Wellness Score: 78/100

---

## 📌 Technologies Used

- **Backend**: Django 5
- **Database**: PostgreSQL
- **Styling**: Tailwind CSS
- **AI Integration**: OpenAI GPT-4
- **Forms & Templates**: Django Forms + Jinja Templates

---

## 📄 License

MIT License – Feel free to use, modify, and build on this project!