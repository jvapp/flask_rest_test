import os
import requests
from dotenv import load_dotenv

"""
task background worker run separate from the application. load_dotenv() in app.py 
will not load env vars into this script. load_dotenv() must be called here.
"""

load_dotenv()

DOMAIN = os.getenv("MAILGUN_DOMAIN")


def send_simple_message(to, subject, body):
    return requests.post(
        f'https://api.mailgun.net/v3/{DOMAIN}/messages',
        auth=("api", os.getenv("MAILGUN_API_KEY")),
        data={"from": f"Data Admin <mailgun@{DOMAIN}>",
              "to": [to],
              "subject": [subject],
              "text": body})


def send_user_registration_email(email, username):
    return send_simple_message(
        email,
        "Successfully signed up",
        f'Hi {username}! you have successfully signed up for the Chement REST API.',
    )
