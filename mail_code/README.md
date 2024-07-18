### Email Sending Flask Application

This Flask application sends an email with an attachment using Flask-Mail. Sensitive information, such as email server credentials, is stored in a `.env` file and loaded with the `python-dotenv` package. The `.env` file is added to `.gitignore` to keep it out of version control.

#### Key Features
- **Environment Variables**: Loads email server settings from the `.env` file.
- **Email Sending Route**: The `/send-email` route sends an email with:
  - **Recipients**: `tech@themedius.ai` and CC to `hr@themedius.ai`
  - **Subject**: "Python (Selenium) Assignment - Somenath Burnwal"
  - **Body**: A brief description of my approach to the assignment.
  - **Attachment**: ZIP files from `../`
- **Error Handling**: Catches and returns SMTP exceptions.

#### Instructions to Run:
To run, write `python3 app.py` in the terminal and then access the URL `http://127.0.0.1:5000/send-email` in your browser to send the email.

