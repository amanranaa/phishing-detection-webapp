# 🔐 Phishing Detection Web Application

A web-based phishing detection system developed using Python Flask that analyzes URLs using heuristic rules to determine whether a website is legitimate or phishing.

---

## 🚀 Features
- URL phishing detection
- Rule-based analysis
- User-friendly web interface
- Real-time results
- Responsive design

---

## 🛠 Tech Stack
- Python
- Flask
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

phishing-detection-webapp  
│  
├── app.py  
├── sample-testing-url.txt  
├── templates/  
│   └── index.html  
├── static/  
│   ├── style.css  
│   └── script.js  
└── .gitignore  

---

## ⚙ Installation

```bash
git clone https://github.com/yourusername/phishing-detection-webapp.git
cd phishing-detection-webapp
pip install -r requirements.txt
python app.py
## Open in browser:
http://127.0.0.1:5000 
```
## 📸 Screenshots
<img width="1867" height="1366" alt="Screenshot 2026-02-05 134237" src="https://github.com/user-attachments/assets/ec05048e-4ecc-4727-99a9-41c17f9babc6" />

<img width="2171" height="1266" alt="Screenshot 2026-02-05 134259" src="https://github.com/user-attachments/assets/0f1c9eac-4153-4c50-8a5b-9f1975d45aa4" />

📌 How It Works
The system analyzes:
- Presence of IP address in URL
- URL length
- HTTPS usage
- Suspicious keywords
If score ≥ threshold → Phishing
Else → Legitimate

🔮 Future Enhancements
1. Machine Learning integration
2. Blacklist API
3. Domain age checker
4. Deployment to cloud

👨‍💻 Author
Aman Kumar Rana


---

