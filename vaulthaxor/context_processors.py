import os 
from dotenv import load_dotenv
import os
import json

load_dotenv(override=True)

def export_vars(request):
    f = open('static/.vite/manifest.json')
    json_data = json.load(f)
    css_file = json_data['resources/scss/main.scss']['file']
    js_file = json_data['resources/js/main.ts']['file']
    js_file_login = json_data['resources/js/login.ts']['file']

    data = {
        'USE_S3': os.getenv("S3_ACTIVATED").lower() in ('true', '1', 't'),
        's3_file_css': css_file,
        's3_file_js': js_file,
        's3_file_js_login': js_file_login,
        'captcha_site_key': os.getenv("CAPTCHA_SITE_KEY"),
    }
    f.close()
    return data