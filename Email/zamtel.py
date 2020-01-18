from twilio.rest import Client

account_sid = 'ACa5b2898f284381b46bc05c14c2c0ff3d'
auth_token = '59dea85a451127e47bb4fff3259bd510'
client = Client(account_sid, auth_token)

sms1 = 'WARNING! FEVER FOR SENIOR CITIZEN #49 HAS ENTERED THE DANGER ZONE!'
sms2 = 'WARNING! FEVER FOR SENIOR CITIZEN #21 HAS ENTERED THE DANGER ZONE!'

message = client.messages.create(
         body='| '+ '\n\n'+sms1+'\n\n'+' |',
         from_='+1 855 806 1779',
         to='+420774348004')

print(message.sid)
print(message)