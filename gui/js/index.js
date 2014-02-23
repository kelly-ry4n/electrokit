var fs = require('fs');
var http = require('http');

var tempmapper, mapper; //mapper will be: {FILE1: FILE1.EXT, FILE2: FILE2.EXT, ...} - tempmapper will be reversed


function initializeselects() {
	// this function should be called upon initialization
	tempmapper = {}, mapper = {};

	var defaultdirs = ['snare', 'tom1', 'tom2', 'tom3', 'kick', 'chh', 'ohh', 'crash', 'ride'];
	var allaudiofiles = [];

	for (var i=0; i<defaultdirs.length; i++) {
		//get ALL of the audio files into one array
		var audiofiles = fs.readdirSync(process.cwd() + "/audio/" + defaultdirs[i] + '/'); //gets the audio files from each default dir

		for (var j=0; j<audiofiles.length; j++) {
			allaudiofiles.push(defaultdirs[i] + '/' + audiofiles[j]); //pushes, e.g.,  snare/snare-1.mp3
			tempmapper[defaultdirs[i] + "/" + audiofiles[j]] = null;  //sets, e.g.,  {"snare/snare-1.mp3": null}
		}
		allaudiofiles.push("-------------.");
	}

	$('.drum').each(function() {
		//add ALL of the audio files for each select
		var id = $(this).attr('id');
		var selid = "#sel"+id;

		for (var i=0; i<allaudiofiles.length; i++) {

			if (allaudiofiles[i] !== '-------------.') {
				var info = allaudiofiles[i].split("/");  //  e.g. "snare/snare-1.mp3" --> ["snare", "snare-1.mp3"]
				var dir = info[0], fileext = info[1];    //  e.g. get snare and snare-1.mp3
				var file = fileext.split(".")[0];
				tempmapper[dir+'/'+fileext] = file;

			} else {
				var file = '-------------';
			}

			$(selid).append(new Option(file, file));
		}

		$(selid).val('-------------');
	});

	for (var key in tempmapper) { mapper[tempmapper[key]] = key; }
}



$(document).ready(function() {

	initializeselects();
	var usersounds = {"pad1": null, "pad2": null, "pad3": null, "pad4": null, "pad5": null, "pad6": null, "pad7": null, "pad8": null, "pad9": null};

	$('.seldrum').change(function() {
		var id = $(this).attr('id'); //selpad#		
		var file = $(this).val();    //snare-1 (for example)
		
		if (file !== '-------------') {
			var dirfileext = mapper[file];
			console.log(dirfileext);
			
			var sound = new Audio(process.cwd() + '/audio/' + dirfileext);
			sound.play();
		}
		
	});


});



/*
var server = http.createServer(function(req, res) {
	res.writeHead(200, {"content-type": "text/html"});
	var data = fs.readFileSync('./../index.html');
	res.end(data);

	$(".drum").each(function() {
		console.log(this);
	});
}).listen(8080);

console.log('listening on 8080...');
*/