var express = require('express'),
path = require('path'),
nodeMailer = require('nodemailer'),
bodyParser = require('body-parser');

var app = express();
var port = 3000;
app.set('view engine', 'ejs');
app.use(express.static('public'));
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());
app.get('/', function (req, res) {      res.render('index');    });

app.post('/send-email', function (req, res) {
let transporter = nodeMailer.createTransport({
        host: 'smtp.gmail.com',       port: 587,      secure: false,
        auth: { user: 'dianaphirin@gmail.com',pass: 'XXXXemb2019' }  });

let mailOptions = {
        from: '"DIANA PHIRI" <dianaphirin@gmail.com>', 
        to: req.body.to,                
        subject: req.body.subject, text: req.body.body,                    
        //      html: '<b>WARNING! FEVER FOR SENIOR CITIZEN #21 HAS ENTERED THE DANGER ZONE!</b>' 
        //      Second Option
};

transporter.sendMail(mailOptions, (error, info) => {
        if (error) { return console.log(error);  }
        console.log('Pemba Posted Message %s sent: %s', info.messageId, info.response);
              res.render('index'); });
      });
app.listen(port, function(){console.log('Server is running at port: ',port);       });