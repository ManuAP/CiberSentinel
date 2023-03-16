import os
import requests
import time
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
YOUR_EMAIL_ADDRESS = os.environ.get("YOUR_EMAIL_ADDRESS")
RECIPIENT_EMAIL_ADDRESS = os.environ.get("RECIPIENT_EMAIL_ADDRESS")

def get_recent_url_data():
    url = "https://urlhaus-api.abuse.ch/v1/urls/recent/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def send_email(subject, body):
    message = Mail(
        from_email=YOUR_EMAIL_ADDRESS,
        to_emails=RECIPIENT_EMAIL_ADDRESS,
        subject=subject,
        plain_text_content=body
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"Email sent successfully. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    last_id = None
    while True:
        recent_data = get_recent_url_data()
        if recent_data and "data" in recent_data:
            if last_id is None:
                last_id = recent_data["data"][0]["id"]
            else:
                if recent_data["data"][0]["id"] != last_id:
                    last_id = recent_data["data"][0]["id"]
                    subject = "New Threat Detected by URLhaus"
                    body = f"New threat detected:\n\n{recent_data['data'][0]}\n\nPlease take preventive measures."
                    send_email(subject, body)
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
