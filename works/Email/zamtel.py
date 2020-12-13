from twilio.rest import Client

account_sid = 'XXX'
auth_token = 'XXX'
client = Client(account_sid, auth_token)

sms1 = 'WARNING! FEVER FOR SENIOR CITIZEN #49 HAS ENTERED THE DANGER ZONE!'
sms2 = 'WARNING! FEVER FOR SENIOR CITIZEN #21 HAS ENTERED THE DANGER ZONE!'

message = client.messages.create(
         body  ='| '+ '\n\n'+sms1+'\n\n'+' |',
         from_ ='XXXXXXX1779',
         to    ='+XXXXX348004')

print(message.sid)
print(message)