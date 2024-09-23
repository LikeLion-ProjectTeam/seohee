from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Mail configuration
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = "465"
app.config["MAIL_USERNAME"] = "choyseohee@gmail.com"
app.config["MAIL_PASSWORD"] = "bjyn pjiv sxwq zyqf"  # Be careful sharing sensitive information
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True

mail = Mail(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']  # Sender name
    email = request.form['email']  # Receiver email entered by the user
    subject = request.form['subject']  # Subject of the email
    message = request.form['message']  # Message body
    
    msg = Message(subject=subject, sender="choyseohee@gmail.com", recipients=[email])
    msg.body = f"Message from {name}: \n\n{message}"
    
    # Send the email
    mail.send(msg)
    
    return 'Email sent SUCCESSFULLY!'

if __name__ == "__main__":
    app.run(debug=True)
