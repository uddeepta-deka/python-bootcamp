from twilio.rest import Client
TWILIO_SID = "AC4b419c9355df8bb4147a1612081bff82"
TWILIO_AUTH_TOKEN = "9e4bd2f95917b8c3fb9c78e348bed62b"
TWILIO_VIRTUAL_NUMBER = "+13392931924"
TWILIO_VERIFIED_NUMBER = "+919625470376"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)