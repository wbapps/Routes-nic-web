
/**
 * Module dependencies.
 */

var express = require('express')
  , http = require('http')
  , controllers = require('./controllers');

var app = express();

app.configure (function (){
  app.set('port', process.env.PORT || 8000);
  app.set('views', __dirname + '/views');
  app.set('view engine', 'jade');
  app.use(express.bodyParser());
  app.use(express.methodOverride());
  app.use(app.router);
  app.use(express.compress());
  app.use("/public", express.static(__dirname + "/public"));
});

app.get("/", controllers.pages.home);

app.get("/hi", function (req, res){
   var message = [
        "<h1>Hello, Express!</h1>",
        "<p>Welcome to Building web apps in node.js</p>",
        "<p>you'll love Express because it's</p>",
        "<ul><li>fast</li>",
        "<li>fun</li>",
        "<li>flexible</li></ul>"].join("\n");
    res.send(message);
});

/*
app.get("/users/:userId", function (req, res){
    res.send("<h1> Hello, User #" + req.params.userId + "!");
})
*/
app.post("/users", function (req, res){
    res.send("Creating a new user with the name " + req.body.username + ".");
});

app.get(/\/users\/(\d*)\/?(edit)?/, function (req, res){
  // /users/10
  // /users/10/
  // /users/10/edit
  var message = "user #" + req.params[0] + "'s profile";

  if(req.params[1] === 'edit'){
    message = "Editing " + message;
  } else {
    message = "Viewing " + message;
  }
  res.send(message);
});

http.createServer(app).listen(app.get('port'), function (){
  console.log("Express server listening on port " + app.get('port'));
});
