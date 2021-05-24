# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

def send(body='Some body', to=''):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'AC70f59124304e09c03dc63d5e16d70593'
    auth_token = '5651e5f25d87fc34cd765ba9adcadf3d'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_='+14438430594',
        to='+58'+to
    )

    print(message.sid)