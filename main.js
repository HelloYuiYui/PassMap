var fs = require('fs');
var express = require("express");
var app = express();
var http = require("http");//Server(app);
var bodyParser = require("body-parser");

app.use(bodyParser.json());
app.use(express.static(__dirname + '/'));

var port = 80;
var vals = {
    '3':'visafree',
    '2':'visaeta',
    '1':'visaonarrival',
    '0':'visarequired',
    '-1':'self'
};

// Converts country code to country name. i.e. TR = Turkey
function codeToName(){
    var obj = {};
    var data = fs.readFileSync('countrycodes.txt', 'utf8').split('\r\n');
    for (i=0;i<data.length;i++){
        var current = data[i].split(',');
        obj[current[1]] = current[0];
    }
    return obj;
}

// Converts country name to country code. i.e. Bulgaria = BG
function nameToCode(){
    var obj = {};
    var data = fs.readFileSync('countrycodes.txt', 'utf8').split('\r\n');
    for (i=0;i<data.length;i++){
        var current = data[i].split(',');
        obj[current[0]] = current[1];
    }
    return obj;
}

function data(){
    var data = fs.readFileSync('passport-index-dataset/passport-index-tidy.csv', 'utf8').split('\r\n');
    return data;
}

function getCountries(){
    var countries = [];
    
    // Passport,Destination,Value (3=visa_free,2=visa_eta,1=visa_on_arrival,0=visa required,-1=pass=dest)
    var contents = data();
    count = 0;
    for(i=0;i<contents.length;i++){
        if(i % 199 == 0){
            var pass = contents[i].split(',')[0],
                des = contents[i].split(',')[1],
                val = contents[i].split(',')[2];
            //console.log(pass);
            countries.push(pass);
        }
    }
    
    return countries;
}

function getPass(country){
    var objd = {
        'visarequired':[],
        'visaonarrival':[],
        'visaeta':[],
        'visafree':[],
        'self':[]
    };
    var index = getCountries().indexOf(country);
    var contents = data();
    var iStart = index * 199;
    //console.log(index);
    var iEnd = (index + 1) * 199;
    for(i=iStart;i<iEnd;i++){
        //console.log(iStart);
        var pass = contents[i].split(',')[0],
            des = contents[i].split(',')[1],
            val = contents[i].split(',')[2];
        //console.log(contents[i].split(',')[1]);
        //objd[val]=[];
        objd[vals[val]].push(des);
    }
    //console.log(objd);
    return objd;
}

function classify(){
    var cs = getCountries();
    var objs = {};
    /*
    var vfree = [];
    var veta = [];
    var vona = [];
    var vreq = [];
    */
    var contents = data()    
    cs.forEach(function(element) {
        //console.log(element);
        objs[element] = getPass(element);
    });
    
    return objs;
}

function addLog(c){
    var path = 'log.txt';
    
    fs.appendFile("log.txt", c, function(err) {
        if(err) {
            return console.log(err);
        }
    }); 
        
}

app.get('/', function(req, res){
    res.sendFile(__dirname + '/maps.html');
})

app.get('/codes', function(req, res){
    res.send(JSON.stringify(nameToCode()));
})

app.get('/country/:c', function(req, res){
    var monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    var ccodes = codeToName();
    var pass = ccodes[req.params.c.toUpperCase()];
    console.log(pass);
    var d = new Date
    addLog("[" + d.getDay() + " " + monthNames[d.getMonth()] + " " + d.getFullYear() + ", " + d.getHours() + ":" + d.getMinutes() + ", "+d.getSeconds()+"] "+pass+"\r\n")
    res.send(JSON.stringify(getPass(pass)));
})

app.set('port', process.env.PORT || 80);
app.set('host', process.env.HOST || '0.0.0.0');

app.listen(app.get('port'), function() {
  console.log("Node app is running at localhost:" + app.get('port'))
})

// Server and port settings.
//http.listen(port, '192.168.1.1', function(){
//    console.log('listening on *: ' + port);
//});



// 2754 1398