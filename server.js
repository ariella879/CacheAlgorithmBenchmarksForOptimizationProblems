//jshint eversion:6

const express = require("express"); //require and incorporate express
const bodyParser = require("body-parser");
const ejs = require("ejs");
const {spawn} = require('child_process');
const path = require('path');

//function that represents the express module
//best practice to call it app
const app = express();
app.use(express.static(__dirname));

const inputs= [];

app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({extended: true}));
//app.use(express.static("public")); //css style

//Get request when the browser interacts with server it will be able to Get
//something back
//gives browser something to display
//method provided with express what happens when the browser gets in touch with
//function is callback function "/" home route "function()": what to do
//response: response server can make when request gets triggered
//FROM SERVER TO BROWSER

app.get("/", function(req, res){ //sends mainpage to browser
  res.render("mainpage"); //send browser response
});



//sending data to server
//post to our home route
app.post("/", function(req, res){ //takes input and stores it in the array
  var input = req.body.input;
  if(req.body.input){ 
    const problem_chooser = spawn('python', ['problem_chooser.py', input]);
    problem_chooser.stdout.on(
    	'data', 
    	(response_path) => {
        // 1 copy everything in response_path.toString().trim() to the static location 
        //     (NB: problem chooser should only send back the path)
        // 2 res.sendFile( THE STATIC LOCATION / t.html  )



        //res.sendFile(response_path.toString().trim());
      }
    );
  }
});

//listen on a specific port for any http requests with a callback
//anonymous function callback using a console log
app.listen(process.env.PORT || 3000, function(){
   //will appear on terminal
});
