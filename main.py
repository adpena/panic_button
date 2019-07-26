from twilio.rest import Client
from dotenv import load_dotenv
import os
from datetime import datetime

class PanicButton:
  def __init__(self):
    load_dotenv()
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
      # print(f"NEED HELP NOW @ {self.office_number}")
      self.send_panic(panic_message)
      exit()
    else:
      # print(f"NEED HELP NOW @ {self.office_number}")
      # print(f"MESSAGE: {panic_message}")
      self.send_panic(panic_message)
      exit()

  def send_panic(self, panic_message=""):
    datetime_sent = datetime.now().strftime("%m/%d/%Y @ %H:%M:%S")
    if panic_message != "":
      client = Client(self.twilio_account_sid, self.twilio_auth_token)
      message = client.messages.create(
      to=self.panic_dispatch, 
      from_=self.panic_sender,
      body=f"PANIC BUTTON: Need help now at {self.office_number}.\nMESSAGE: {panic_message}\nSENT: {datetime_sent}")
      print(f"Message sent to {self.panic_dispatch} - help is on its way!")
    else:
      client = Client(self.twilio_account_sid, self.twilio_auth_token)
      message = client.messages.create(
      to=self.panic_dispatch, 
      from_=self.panic_sender,
      body=f"PANIC BUTTON: Need help now at {self.office_number}.\nMESSAGE: N/A\nSENT: {datetime_sent}")
      print(f"Message sent to {self.panic_dispatch} - help is on its way!")


if __name__ == '__main__':
  panic_button = PanicButton()
  panic_button.panic()
