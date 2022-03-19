
var application_root = __dirname;
express = require('express');
request = require('request');
bodyParser = require('body-parser');
const path = require('path');
const app = express();

app.use(bodyParser.urlencoded({extended: true})); // Basic use
app.use(express.static(path.join(application_root,'files')));

app.get('', function(req, res) {
    res.send('hello'); //used to test page and inspect has no use otherwise
});

app.post('/signup', (req, res) => {
    const { firstName, lastName, email} = req.body;
   
    if(!firstName || !lastName || !email) {
        res.redirect('/fail.html');
        return;
    }
    const options = {
        url: 'https://<dc>.api.mailchimp.com/3.0/'
    }
});

const PORT = process.env.PORT || 3000; //port can be anything that works does but can be specific 

app.listen(PORT, console.log('Server started on port:', PORT));


//NOTES of what to get done for PW(personal Website)
 // find the MC code after creating a list 
 // Connect to MC(Mail Chimp API)
 //Create Icon ONLY
 // more user I/O 
 // Back button is missing idk where it went
 // Failure page was disconnected :((((((