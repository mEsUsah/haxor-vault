import os
from dotenv import load_dotenv
from django.core.mail import send_mail
from users.models import User

load_dotenv(override=True)

def send_verification_email(user: User) -> None:
    """Send a verification email to the user."""
    
    subject = 'Verify your account'
    recipient_list = [user.email]
    HOST = os.getenv("SITE_HOST")
    html_message = f'<h1>Verify your account:</h1>\
        <p>Follow the link below to verify your vault.haxor.no account:</p>\
        <p><a href="{HOST}/verify/{user.verification_code}">{HOST}/verify/{user.verification_code}</a></p>'
    
    send_mail(subject=subject, 
              recipient_list=recipient_list,
              from_email=None,
              message=None,
              html_message=html_message, 
    )