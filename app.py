from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)

allowed_origin = "https://hackthefest.in/"

# def validate_origin():
#     if request.headers.get("Origin") != allowed_origin:
#         return jsonify({"error": "Invalid origin"}), 403

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # # Validate origin
    # error_response = validate_origin()
    # if error_response:
    #     return error_response

    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('textarea')

    # Send email to hackoverflow@cumail.in
    send_email(name, email, message)

    # Send automated personalized text
    send_personalized_text(name, email)

    # Return JSON response with JavaScript for the pop-up dialogue box
    response_data = {
        'message': 'Your message has been sent!',
        'script': 'alert("Your message has been sent!");'
    }
    return jsonify(response_data), 200


def send_email(name, email, message):
    # Set up SMTP server
    smtp_server = 'smtp.gmail.com'  # Gmail SMTP server
    smtp_port = 587  # SMTP port for Gmail
    sender_email = 'hackoverflow@cumail.in'  # Your email
    app_password = 'lgde lflp hmgu krrd'  # Your generated app password

    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = 'hackoverflow@cumail.in'
    msg['Subject'] = "New contact form submission from Hack the Fest website."

    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    msg.attach(MIMEText(body, 'plain'))

    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)


def send_personalized_text(name, email):
    # Set up SMTP server
    smtp_server = 'smtp.gmail.com'  # Gmail SMTP server
    smtp_port = 587  # SMTP port for Gmail
    sender_email = 'hackoverflow@cumail.in'  # Your email
    app_password = 'lgde lflp hmgu krrd'  # Your generated app password

    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = 'Message Confirmation'

    body = f"Hello {name}\n\nYour message has been sent. We'll get back to you soon!"
    msg.attach(MIMEText(body, 'plain'))

    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)
