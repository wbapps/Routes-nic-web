
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

http.createServer(app).listen(app.get('port'), function (){
  console.log("Express server listening on port " + app.get('port'));
});
