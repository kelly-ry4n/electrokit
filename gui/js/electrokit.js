var allfiles = {};
var drumtypes = ['snare', 'tom1', 'tom2', 'tom3', 'kick', 'chh', 'ohh', 'crash', 'ride'];
var HR = '--------------';

var allfiles = {'snare': {'snare-1': './audio/snare/snare-1.mp3', 'snare-2': './audio/snare/snare-2.mp3', 'snare-3': './audio/snare/snare-3.mp3'},
				'tom1': {'tom1-1': './audio/tom1/tom1-1.mp3'}, 'tom2': {'tom2-1': './audio/tom2/tom2-1.mp3'}, 'tom3': {'tom3-1': './audio/tom3/tom3-1.mp3'},
				'kick': {'kick-1': './audio/kick/kick-1.mp3', 'kick-2': './audio/kick/kick-2.mp3', 'kick-3': './audio/kick/kick-3.mp3'},
				'chh': {'chh-1': './audio/chh/chh-1.mp3', 'chh-2':  './audio/chh/chh-2.mp3',  'chh-3': './audio/chh/chh-3.mp3', 'chh-4': './audio/chh/chh-4.mp3'},
				'ohh': {'ohh-1': './audio/ohh/ohh-1.mp3'}, 'crash': {'crash-1': './audio/crash/crash-1.mp3', 'crash-2': './audio/crash/crash-2.mp3'},
				'ride': {'ride-1': './audio/ride/ride-1.mp3', 'ride-2': './audio/ride/ride-2.mp3'}
				}

var allsounds = {}
for (var i=0; i<drumtypes.length; i++) {
	var d = drumtypes[i];

	for (var sound in allfiles[d]) {
		var EXODIAAAAAAAOBLITERAAAAAAAATE = new Audio(allfiles[d][sound]);
		allsounds[sound] = EXODIAAAAAAAOBLITERAAAAAAAATE;
	}
}

$(document).ready(function() {

	$(".seldrum").each(function() {
		for (var i=0; i<drumtypes.length; i++) {
			var d = drumtypes[i];

			for (var sound in allfiles[d]) {
				$(this).append(new Option(sound, sound));
			}

			$(this).append(new Option(HR, HR));
			$(this).val(HR);
		}
	});

	$(".seldrum").change(function() {
		var selid = $(this).attr('id');
		var file = $(this).val();
		var drumtype = file.split('-')[0];
		var filepath = allfiles[drumtype][file];

		allsounds[file].play();

	});

});