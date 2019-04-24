from flask import Flask
from flask import request
import os
from twilio.rest import Client
app = Flask(__name__)

@app.route('/')
def twilio_heroku_app():
    account_sid = os.environ.get('account_sid', None)
    auth_token = os.environ.get('auth_token', None)
    sandbox_number = os.environ.get('sandbox_number', None)
    to_number = request.args.get('to')
    msg_body = request.args.get('msg')
    
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                  body=msg_body,
                                  from_='whatsapp:'+sandbox_number,
                                  to='whatsapp:+91'+to_number
                              )

    return message.sid

if __name__ == '__main__':
    app.run()
