from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# إعداد قاعدة البيانات
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'messages.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# تعريف النموذج
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Message {self.name}>'
@app.route('/messages')
def show_messages():
    messages = Message.query.all()
    return render_template('messages.html', messages=messages)

# صفحة الشكر
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

# الصفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html')

# التعامل مع النموذج
@app.route('/send-email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # تخزين البيانات في قاعدة البيانات
    new_message = Message(name=name, email=email, message=message)
    db.session.add(new_message)
    db.session.commit()

    # التوجيه إلى صفحة الشكر
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
