from decouple import config
from twilio.rest import Client

TWILIO_ACCOUNT_SID = config("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = config("TWILIO_AUTH_TOKEN")
TWILIO_SANDBOX_NUMBER = config("TWILIO_SANDBOX_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to_number, message):
    client.messages.create(
        body=message,
        from_=TWILIO_SANDBOX_NUMBER,
        to=f'whatsapp:{to_number}'
    )
