from dotenv import load_dotenv
from twilio.rest import Client
import os
load_dotenv()
account_sid=os.getenv("account_sid")
auth_token=os.getenv("auth_token")

print(account_sid)
print(auth_token)

client=Client(account_sid,auth_token)

call=client.calls.create(
    to=os.getenv("to"), 
    from_="+18506053836",
    url="http://demo.twilio.com/docs/voice.xml"
    )

print(call.sid)