from jinja2 import Template
from datetime import datetime

TEMPLATE = """
<!DOCTYPE html>
<html>

<head>

<title>OWASP Quick Auditor</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{

    background:
    linear-gradient(
        rgba(5,10,20,0.85),
        rgba(5,10,20,0.90)
    ),
    url('assets/background.jpg');

    background-size:cover;
    background-position:center;
    background-attachment:fixed;

    color:#f1f5f9;

    font-family:'Segoe UI',sans-serif;

    padding:40px;
}

.container{
    max-width:1200px;
    margin:auto;
}

.hero{

    text-align:center;

    padding:30px;

    margin-bottom:30px;

    background:rgba(255,255,255,0.04);

    backdrop-filter:blur(10px);

    border:1px solid rgba(255,255,255,0.08);

    border-radius:20px;
}

.hero h1{

    font-size:42px;

    margin-bottom:15px;

    color:white;
}

.hero p{
    color:#cbd5e1;
}

.score-card{

    width:220px;

    margin:25px auto;

    padding:20px;

    border-radius:20px;

    background:rgba(255,255,255,0.05);

    backdrop-filter:blur(12px);
}

.score{

    font-size:48px;

    font-weight:bold;
}

.rank{

    margin-top:10px;

    font-size:20px;
}

.progress{

    width:100%;

    height:20px;

    background:rgba(255,255,255,0.08);

    border-radius:30px;

    overflow:hidden;

    margin-top:20px;
}

.bar{

    height:100%;

    background:#38bdf8;

    border-radius:30px;

    animation:grow 1.5s ease;
}

@keyframes grow{

    from{
        width:0;
    }
}

.badges{

    text-align:center;

    margin-bottom:30px;
}

.badges span{

    display:inline-block;

    margin:5px;

    padding:10px 15px;

    border-radius:20px;

    background:rgba(255,255,255,0.05);

    border:1px solid rgba(255,255,255,0.08);
}

.finding{

    margin-bottom:25px;

    padding:25px;

    background:rgba(255,255,255,0.05);

    backdrop-filter:blur(12px);

    border-radius:20px;

    border:1px solid rgba(255,255,255,0.08);

    animation:fadeUp .5s ease;
}

@keyframes fadeUp{

    from{
        opacity:0;
        transform:translateY(20px);
    }

    to{
        opacity:1;
        transform:translateY(0);
    }
}

.CRITICAL{
    border-left:5px solid #ef4444;
}

.HIGH{
    border-left:5px solid #f97316;
}

.MEDIUM{
    border-left:5px solid #eab308;
}

.LOW{
    border-left:5px solid #06b6d4;
}

.severity{

    display:inline-block;

    margin-bottom:15px;

    padding:5px 12px;

    border-radius:10px;

    background:rgba(255,255,255,0.08);
}

.mentor{

    margin-top:20px;

    padding:20px;

    background:rgba(255,255,255,0.03);

    border-radius:15px;
}

.mentor h3{

    margin-top:15px;

    margin-bottom:8px;

    color:#7dd3fc;
}

pre{

    margin-top:10px;

    background:#0f172a;

    padding:15px;

    border-radius:10px;

    overflow-x:auto;
}

.footer{

    text-align:center;

    margin-top:40px;

    color:#94a3b8;
}

</style>

</head>

<body>

<div class="container">

<div class="hero">

<h1>🔐 OWASP Quick Auditor</h1>

<p>Learn • Audit • Improve</p>

<div class="score-card">

<div class="score">
{{ score }}/100
</div>

<div class="rank">
{{ rank }}
</div>

<div class="progress">
<div class="bar" style="width:{{ score }}%"></div>
</div>

</div>

<p>
🎯 {{ url }}
</p>

<p>
📅 {{ date }}
</p>

</div>

<div class="badges">

<span>🏅 Header Hunter</span>
<span>🏅 Cookie Guardian</span>
<span>🏅 CORS Detective</span>
<span>🏅 Security Mentor</span>

</div>

{% for f in findings %}

<div class="finding {{ f.severity }}">

<div class="severity">
{{ f.severity }}
</div>

<h2>{{ f.check }}</h2>

<br>

<p>{{ f.detail }}</p>

<div class="mentor">

<h3>🤔 Why should I care?</h3>
<p>{{ f.advice.why }}</p>

<h3>🎯 Real World Impact</h3>
<p>{{ f.advice.impact }}</p>

<h3>🛠 How to Fix</h3>
<p>{{ f.advice.fix }}</p>

{% if f.advice.snippet %}
<pre>{{ f.advice.snippet }}</pre>
{% endif %}

<h3>⏱ Estimated Fix Time</h3>
<p>{{ f.advice.time }}</p>

<h3>🎓 Interview Question</h3>
<p>{{ f.advice.question }}</p>

<h3>✅ Sample Answer</h3>
<p>{{ f.advice.answer }}</p>

</div>

</div>

{% endfor %}

<div class="footer">

OWASP Quick Auditor • Built by Security Enthusiast 🚀

</div>

</div>

</body>

</html>
"""

def generate_report(url, findings):

    score = 100

    for f in findings:

        if f["severity"] == "CRITICAL":
            score -= 20

        elif f["severity"] == "HIGH":
            score -= 10

        elif f["severity"] == "MEDIUM":
            score -= 5

        elif f["severity"] == "LOW":
            score -= 2

    score = max(score,0)

    if score >= 90:
        rank = "🛡️ Cyber Guardian"

    elif score >= 75:
        rank = "⚔️ Security Defender"

    elif score >= 50:
        rank = "🥈 Security Analyst"

    else:
        rank = "🚨 Vulnerability Magnet"

    tmpl = Template(TEMPLATE)

    html = tmpl.render(
        url=url,
        findings=findings,
        score=score,
        rank=rank,
        date=datetime.now().strftime("%Y-%m-%d %H:%M")
    )

    with open("report.html","w",encoding="utf-8") as f:
        f.write(html)

    print("\\n📄 Report saved to report.html")
