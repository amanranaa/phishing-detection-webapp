from flask import Flask, render_template, request, jsonify
import re
import requests

app = Flask(__name__)

def check_phishing(url):
    score = 0

    # 1. IP Address in URL
    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        score += 1

    # 2. URL Length
    if len(url) > 75:
        score += 1

    # 3. @ Symbol
    if "@" in url:
        score += 1

    # 4. HTTPS
    if not url.startswith("https"):
        score += 1

    # 5. Suspicious Words
    phishing_words = ["login", "verify", "update", "secure", "account"]
    for word in phishing_words:
        if word in url.lower():
            score += 1

    return score

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    url = data["url"]

    score = check_phishing(url)

    if score >= 3:
        result = "⚠️ Phishing Website Detected"
        status = "danger"
    else:
        result = "✅ Legitimate Website"
        status = "safe"

    return jsonify({"result": result, "status": status})

if __name__ == "__main__":
    app.run(debug=True)
