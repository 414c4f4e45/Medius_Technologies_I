from flask import Flask
from flask_mail import Mail, Message
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Configuration for Flask-Mail using environment variables
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL').lower() in ['true', '1', 't']
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = (os.getenv('MAIL_DEFAULT_SENDER_NAME'), os.getenv('MAIL_DEFAULT_SENDER'))

mail = Mail(app)

@app.route('/send-email')
def send_email():
    # Define recipients and CC recipients
    recipients = ['tech@themedius.ai']
    cc_recipients = ['hr@themedius.ai']

    # Create the email message
    msg = Message(subject='Python (Selenium) Assignment - SomenathBurnwal',
                  recipients=recipients,
                  cc=cc_recipients)
    
    # Add a body with a weblink
    msg.body = '''Dear [Internship Coordinator / Hiring Team],

I hope this message finds you well. Please find attached my Python script designed for the internship assignment. 

Description: This script utilizes Selenium WebDriver to automate the submission of a Google Form. It navigates to the form, fills it with predefined data, captures screenshots before and after submission, and handles form submission electronically.

You can review the code repository for this assignment on GitHub: "https://github.com/414c4f4e45/Medius_Technologies_I"

I have also included my resume along with zip files containing screenshots and the code repository for your review.

Thank you for considering my application. Yes, I'm available and prepared to work full-time from 10 am to 7 pm for the next 3-6 months.

Best regards,
Somenath Burnwal
'''

    # List of ZIP file paths to attach
    file_paths = ['../screenshots.zip', '../code_repo.zip', '../somenath_AIML_2025.pdf']

    # Attach each file
    for file_path in file_paths:
        try:
            with app.open_resource(file_path) as fp:
                # Determine MIME type based on file extension
                if file_path.endswith('.pdf'):
                    mime_type = 'application/pdf'
                elif file_path.endswith('.zip'):
                    mime_type = 'application/zip'
                else:
                    mime_type = 'application/octet-stream'  # Default MIME type

                # Attach the file to the email message
                msg.attach(os.path.basename(file_path), mime_type, fp.read())
        except FileNotFoundError:
            return f'Attachment file {file_path} not found', 404

    # Send the email
    try:
        mail.send(msg)
        return 'Email sent!'
    except smtplib.SMTPException as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)

