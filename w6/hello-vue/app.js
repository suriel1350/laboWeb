var express = require('express');
var PORT = 3000;
var app = express();
app.get('/', function(req, res)
{
        res.sendfile('index.html');
}
);
app.listen(PORT);
console.log('Running on port ' + PORT);
