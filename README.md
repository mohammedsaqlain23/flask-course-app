# Flask Course App

A full-stack Flask web application for managing courses and enrollments.  
Built with Python, Flask, SQLAlchemy, and Bootstrap for a beautiful and responsive UI.

---

## Features

- Add, view, and manage courses  
- Enroll students in courses  
- Clean, user-friendly interface with Bootstrap  
- SQLite database for easy setup  
- Ready for deployment with Docker support  

---

## Installation

### Prerequisites

- Python 3.8+  
- Git  

### Run locally (without Docker)

```bash
git clone https://github.com/mohammedsaqlain23/flask-course-app.git
cd flask-course-app
python3 -m venv venv
source venv/bin/activate       # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
flask db upgrade              # Setup database
flask run                     # Start development server
