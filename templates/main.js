var express = require('express');
/*
var app = express();

var sleep = require('system-sleep');
*/
var result="<html><body><h2>"
var app2 = express();
var path2 = require('path');
var result="@";
// viewed at http://localhost:8080
app2.get('/', function(req, res) {
    res.sendFile(path2.join(__dirname + '/indexml.html'));
});

app2.listen(8080);


// import express JS module into app 
// and creates its variable. 

var express = require('express'); 
var app = express(); 

// Creates a server which runs on port 3000 and 
// can be accessed through localhost:3000 
app.listen(8081, function() { 
	console.log('server running on port 8081'); 
} ) 

// Function callName() is executed whenever 
// url is of the form localhost:3000/name 
app.get('/process_get', callName); 

function callName(req, res) { 
	
	// Use child_process.spawn method from 
	// child_process module and assign it 
	// to variable spawn 
	var spawn = require("child_process").spawn; 
	
	// Parameters passed in spawn - 
	// 1. type_of_script 
	// 2. list containing Path of the script 
	// and arguments for the script 
	
	// E.g : http://localhost:3000/name?firstname=Mike&lastname=Will 
	// so, first name = Mike and last name = Will 
	response = {
		
		path:req.query.path
	 };
	var process = spawn('python3',["./main.py"] ); 

   
	// Takes stdout data from script which executed 
	// with arguments and send this data to res object 
	process.stdout.on('data', function(data) { 
      result+=data.toString;
   result+="</h2></body></html>"
		//res.send('<html><body> style="color:rgba(134, 76, 243, 0.897)">'+data.toString()+'</h2></body></html>'); 
		res.send(data.toString())
	} ) 
} 

// save code as start.js 

