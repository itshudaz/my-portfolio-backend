
# My Portfolio Backend
This is the backend for my personal portfolio website, built with **Flask**.  
It handles contact form submissions and stores them in a **SQLite** database.
The backend is connected to the live frontend hosted on GitHub Pages. Visitors can use the contact form on the site to send me a message.
---
##  Live Frontend
The portfolio website is live here:  
[🔗 My Portfolio Frontend](https://itshudaz.github.io/my-portfolio/)  
---
## Project Structure

my-portfolio-backend/
│
├── app.py                # Main Flask app
├── messages.db           # SQLite database
├── requirements.txt      # Dependencies
├── .gitignore            # Git ignore file
│
├── templates/            # HTML templates (index.html, thankyou.html)
└── static/               # Static files (CSS)

---

##  How to Run Locally

### 1. Clone the repository

git clone https://github.com/your-username/my-portfolio-backend.git
cd my-portfolio-backend


2. Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate


3. Install the required packages

pip install -r requirements.txt


4. Run the Flask app

flask run


5. Open in your browser
Visit: http://127.0.0.1:5000


Contact Form Flow

1. A visitor fills out the form on the portfolio site. 
2. The data (name, email, message) is sent to the backend.
3. The backend stores the message in messages.db.
4. The user is redirected to a thank you page.

⸻

Database

This app uses SQLite (messages.db) to store the messages.
To view the content of the database, you can use tools like DB Browser for SQLite.

.gitignore

venv/
__pycache__/
*.pyc
*.db
.env

This file ensures local development files like the virtual environment and database are not uploaded to GitHub.


Author

Made with care by Huda

Feel free to contact me through the form on my portfolio site!
