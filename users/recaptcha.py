import requests
import os
import logging


def validate_captcha_token(token: str) -> bool:
    """Validate the captcha token using Google's reCAPTCHA API."""
    
    logger = logging.getLogger('errorlogger')
    secret_key = os.getenv("CAPTCHA_SECRET_KEY")
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
        'secret': secret_key,
        'response': token
    }).json()

    if response['success'] and response['score'] >= 0.5:
        return True
    else:
        logger.error(f"validation failed with error codes: {response['error-codes']}")

    return False