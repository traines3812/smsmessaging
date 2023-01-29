from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"

# Initialize the client
client = Client(account_sid, auth_token)

# Send the SMS message
message = client.messages.create(
    to="+12345678901", 
    from_="+12345678901", 
    body="Hello, this is a test message sent using Twilio."
)

# Print the SID of the sent message
print(f"Message SID: {message.sid}")
