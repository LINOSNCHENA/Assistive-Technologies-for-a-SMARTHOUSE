// Twilio Credentials   

const accountSid = 'ACa5b2898f284381b46bc05c14c2c0ff3d'; 
const authToken = '59dea85a451127e47bb4fff3259bd510'; 
const client = require('twilio')(accountSid, authToken); 
var sms1 = 'WARNING! FEVER FOR SENIOR CITIZEN #21 HAS ENTERED THE DANGER ZONE!';
var sms2 = 'WARNING! FEVER FOR SENIOR CITIZEN #49 HAS ENTERED THE DANGER ZONE!';

async function main1() {
client.messages
  .create({body: sms1,  from: '+1 855 806 1779', to: '+420774348004' })
  .then(message => console.log('ZAMTEL #1 |:'+message.sid));}

async function main2() {
  client.messages
  .create({body: sms2,  from: '+1 855 806 1779', to: '+420774348004'})
  .then(message => console.log('ZAMTEL #2 |:'+message.sid));  }
main1();
main2();