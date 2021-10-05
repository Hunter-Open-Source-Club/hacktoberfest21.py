
from twilio.rest import Client
from dotenv import load_dotenv
from os import environ as env
load_dotenv()

print(env["ACCOUNT_SID"])

# Your Account SID from twilio.com/console
account_sid = env["ACCOUNT_SID"]
# Your Auth Token from twilio.com/console
auth_token  = env["AUTH_TOKEN"]

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=env["MY_NUMBER"], 
    from_=env["FROM_NUMBER"],
    body="Hello from Python!")

print(message.sid)
