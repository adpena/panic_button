from twilio.rest import Client
from dotenv import load_dotenv
import os
from datetime import datetime
import sys
import time


class PanicButton:
    def __init__(self):
        load_dotenv(
            resource_path(("C:\\Users\\Shadow\\Documents\\GitHub\\panic_button\\.env"))
        )
        self.office_number = os.getenv("OFFICE_NUMBER")
        self.twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.panic_dispatch = os.getenv("PANIC_DISPATCH")
        self.panic_sender = os.getenv("PANIC_SENDER")

    def panic(self):
        print("##############################")
        print("### PANIC BUTTON ACTIVATED ###")
        print("##############################\n")
        panic_message = input("Press ENTER to skip or type message:\t")
        if panic_message == "":
            self.send_panic(panic_message)
        else:
            self.send_panic(panic_message)

    def send_panic(self, panic_message=""):
        datetime_sent = datetime.now().strftime("%m/%d/%Y @ %H:%M:%S")
        client = Client(self.twilio_account_sid, self.twilio_auth_token)
        if panic_message != "":
            message = client.messages.create(
                to=self.panic_dispatch,
                from_=self.panic_sender,
                body=f"PANIC BUTTON: Need help now @ {self.office_number}.\nMESSAGE: {panic_message}\nSENT: {datetime_sent}",
            )
            print(f"Message sent to {self.panic_dispatch} - help is on its way!\n")
        else:
            message = client.messages.create(
                to=self.panic_dispatch,
                from_=self.panic_sender,
                body=f"PANIC BUTTON: Need help now @ {self.office_number}.\nMESSAGE: N/A\nSENT: {datetime_sent}",
            )
            print(f"Message sent to {self.panic_dispatch} - help is on its way!\n")
        print("ALERT: This window will close in 5 seconds...")
        time.sleep(5)
        sys.exit()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    panic_button = PanicButton()
    panic_button.panic()
    k = input("press close to exit")
