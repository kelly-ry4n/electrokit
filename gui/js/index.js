var fs = require('fs');
var http = require('http');

function updatesoundselect(drum) {
	// drum is snare, chh, ohh, tom1, ...
	//var audiofiles = fs.readdirSync('./../audio/'+drum+'/');
	//return audiofiles;
	//$("#sel"+drum)
}

//console.log(updatesoundselect('crash'));


var server = http.createServer(function(req, res) {
	res.writeHead(200, {"content-type": "text/html"});
	var data = fs.readFileSync('./../index.html');
	res.end(data);
}).listen(8080);

console.log('listening on 8080...');