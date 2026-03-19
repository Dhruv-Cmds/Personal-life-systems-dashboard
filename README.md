# Personal Life Systems Dashboard

## Introduction
A backend-driven web application that evaluates a student's financial, health, and academic conditions to generate a unified Life Load Score. The system focuses on decision support by combining multiple real-life factors into a single analysis.

---

## Features
- Financial load analysis
- Health risk evaluation (BMI-based)
- Academic pressure scoring
- Aggregated Life Load Score
- Rule-based recommendations

---

## Tech Stack
- Backend: Python, Flask
- Frontend: HTML, CSS
- Logic: Rule-based system

---

## How It Works
The system collects user inputs across three domains:
- Finance (expenses, balance)
- Health (height, weight → BMI)
- Academics (study load, pressure)

These inputs are processed through a rule-based engine to compute:
- Individual scores for each domain
- A final Life Load Score
- Recommendations based on overall stress level

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Dhruv-Cmds/Personal-Life-Dashboard.git

2. Navigate into the project directory:
  ```
  cd Personal-Life-Dashboard/backend
  ```

3. Install dependencies:

pip install -r requirements.txt

## Usage

1. Run the backend server:
  ```
  python app.py
  ```

2. Open the frontend:

Open frontend/index.html in your browser
or
  ```
  Visit: http://127.0.0.1:5000/ (if integrated)
  ```

## Screenshots

### Input Interface
![Input UI](screenshots/ui-input.png)

### Analysis Result
![Output UI](screenshots/ui-output.png)

### Backend Running
![Backend](screenshots/backend-running.png)

## Project Structure

```
Personal-Life-Dashboard/
│
├── backend/
│   ├── app.py
│   ├── logic.py
│   └── requirements.txt
│
├── frontend/
│   └── index.html
│
├── screenshots/
│
├── README.md
└── .gitignore
```

## Why This Project

This project focuses on combining multiple real-life systems
