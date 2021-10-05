from dotenv import load_dotenv
from os import environ as env
from os import system as sys
import os

load_dotenv()

if env["ACCOUNT_SID"] == None:
    print("Please configure env file correctly. Account_SID is missing.")
elif env["AUTH_TOKEN"] == None:
    print("Please insert auth_token.")
elif env["FROM_NUMBER"] == None:
    print("Please enter your Twilio phone number.")
elif "MY_NUMBER" not in env:
    print("Please include destination number in .env file as MY_NUMBER=XXXXXXXXXX.")
else:
    sys(f"python {os.path.dirname(__file__)}\main.py")