var twilio = require('twilio'),
// Authentication of twilio account

client = twilio('XXXXX', 'XXXX'),
cronJob = require('cron').CronJob;                     

var numbers = ['+XXXXX631581', '+XXXXXXXX04','+XXXX4207732']; 
var sms1 = 'WARNING! FEVER FOR SENIOR CITIZEN #21 HAS ENTERED THE DANGER ZONE!';
var sms2 = 'WARNING! FEVER FOR SENIOR CITIZEN #49 HAS ENTERED THE DANGER ZONE!';

for( var i = 0; i < numbers.length; i++ ) {
    client.messages.create({ 
      to:numbers[i], 
      from:'+XXXX79', 
      body:'Hello ZAMNET Volunteer! '+ sms2}, 
      function( err, data1 ) {console.log('ZAMNET SINGLE #1'+sms2)},
      function( err, data2 ) {console.log('ZAMNET SINGLE #1'+sms1)}
    );
}