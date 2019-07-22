// import express JS module into app 
// and creates its variable. 
var express = require('express'); 
var app = express(); 
var path = require('path');
  
// Creates a server which runs on port 3000 and  
// can be accessed through localhost:3000 
app.listen(3000, function() { 
    console.log('server running on port 3000'); 
} ) 

app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname + '/login.html'));
});