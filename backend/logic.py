# logic.py

def finance_score(income, monthly_spending):
    """
    Financial stress based on income vs monthly spending
    """

    if income <= 0:
        return 90

    ratio = monthly_spending / income

    if ratio < 0.4:
        return 30    # healthy
    elif ratio < 0.7:
        return 60    # manageable
    else:
        return 90    # risky


def health_score(height_cm, weight_kg):
    if height_cm <= 0:
        return 90

    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)

    if 18.5 <= bmi <= 24.9:
        return 30
    elif 25 <= bmi <= 29.9:
        return 60
    else:
        return 90


def academic_score(subjects):
    if not subjects:
        return 30

    total_credits = 0
    for s in subjects:
        total_credits += s.get("credit", 0)

    avg = total_credits / len(subjects)

    if avg < 3:
        return 30
    elif avg < 5:
        return 60
    else:
        return 90


def life_load(fin, health, acad):
    avg = (fin + health + acad) // 3

    if avg < 40:
        status = "Low Load"
    elif avg < 70:
        status = "Moderate Load"
    else:
        status = "High Load"

    return avg, status

def academic_score_from_gpa(gpa):
    """
    Academic stress based on last semester GPA
    """

    if gpa >= 8.0:
        return 30   # low stress
    elif gpa >= 6.0:
        return 60   # moderate stress
    else:
        return 90   # high stress


def recommendations(fin, health, acad):
    tips = []

    if fin >= 60:
        tips.append("Reduce monthly expenses or increase income stability.")
    else:
        tips.append("Your financial balance looks healthy.")

    if health >= 60:
        tips.append("Improve sleep, diet, or physical activity.")
    else:
        tips.append("Your health indicators are in a good range.")

    if acad >= 60:
        tips.append("Consider reducing academic load or improving time management.")
    else:
        tips.append("Academic workload is well managed.")

    return tips