function route(app, regex, prefix) {
 app.get(regex, function (req, res) {
 var type = req.params[0];
 var path = req.params[1];
 var file = prefix + type + '/' + path
 res.sendfile(file);
 });
}

var express=require('express');
var PORT=8099;

var app=express();
app.get('/', function(req, res){
	res.sendfile('loginFacebook.html');
});

route(app, /^\/(assets|jscolor-2.0.4)\/(.*)/, './');

app.listen(PORT);
console.log('Running on port ' + PORT);