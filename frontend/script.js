function analyze() {
    const data = {
    income: Number(document.getElementById("income").value),
    monthly_spending: Number(document.getElementById("spending").value),
    height: Number(document.getElementById("height").value),
    weight: Number(document.getElementById("weight").value),
    gpa: Number(document.getElementById("gpa").value)
    };
    
  fetch("http://127.0.0.1:5000/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  })
    .then(res => res.json())
    .then(out => {
      document.getElementById("score").innerText = out.life_load_score;

      const status = document.getElementById("status");
      status.innerText = out.status;
      status.className = "badge " + out.status.toLowerCase().split(" ")[0];

      document.getElementById("finance").innerText =
        "Finance Score: " + out.finance_score;

      document.getElementById("health").innerText =
        "Health Score: " + out.health_score;

      document.getElementById("academic").innerText =
        "Academic Score: " + out.academic_score;

      const tips = document.getElementById("tips");
      tips.innerHTML = "";
      out.recommendations.forEach(t => {
        const li = document.createElement("li");
        li.innerText = t;
        tips.appendChild(li);
      });
    });
}