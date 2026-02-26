# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from logic import (
    finance_score,
    health_score,
    academic_score_from_gpa,
    life_load,
    recommendations
)

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    #  0 is defult value if user not add any value then by defult value is 0
    income = data.get("income", 0)
    monthly_spending = data.get("monthly_spending", 0)
    height = data.get("height", 0)
    weight = data.get("weight", 0)
    gpa = data.get("gpa", 0)

    fin = finance_score(income, monthly_spending)
    health = health_score(height, weight)
    acad = academic_score_from_gpa(gpa)

    # can use ave insted of total Total is just for readability {in py name does not metters}
    # ave , status = life_load(fin , health , acad)
    total, status = life_load(fin, health, acad)
    tips = recommendations(fin, health, acad)

    return jsonify({
        "finance_score": fin,
        "health_score": health,
        "academic_score": acad,
        "life_load_score": total,
        "status": status,
        "recommendations": tips
    })


if __name__ == "__main__":
    app.run(debug=True)