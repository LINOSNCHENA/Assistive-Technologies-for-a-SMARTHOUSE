var twilio = require('twilio'),
// Authentication of twilio account

client = twilio('ACa5b2898f284381b46bc05c14c2c0ff3d', '59dea85a451127e47bb4fff3259bd510'),
cronJob = require('cron').CronJob;                     

var numbers = ['+260975631581', '+420774348004','+420773283754',
 '+42077096282','+260979232500', '+18018372837']; 
var sms1 = 'WARNING! FEVER FOR SENIOR CITIZEN #21 HAS ENTERED THE DANGER ZONE!';
var sms2 = 'WARNING! FEVER FOR SENIOR CITIZEN #49 HAS ENTERED THE DANGER ZONE!';

for( var i = 0; i < numbers.length; i++ ) {
    client.messages.create({ 
      to:numbers[i], 
      from:'+18558061779', 
      body:'Hello ZAMNET Volunteer! '+ sms2}, 
      function( err, data1 ) {console.log('ZAMNET SINGLE #1'+sms2)},
      function( err, data2 ) {console.log('ZAMNET SINGLE #1'+sms1)}
    );
}