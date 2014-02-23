import pyglet
from pyglet.window import key

window = pyglet.window.Window();

background = pyglet.image.load("img/background.jpg");

snare = pyglet.media.StaticSource(pyglet.media.load('./audio/snare/snare-1.mp3'));
tom1 = pyglet.media.StaticSource(pyglet.media.load('./audio/tom1/tom1-1.mp3'));
tom2 = pyglet.media.StaticSource(pyglet.media.load('./audio/tom2/tom2-1.mp3'));
tom3 = pyglet.media.StaticSource(pyglet.media.load('./audio/tom3/tom3-1.mp3'));
kick = pyglet.media.StaticSource(pyglet.media.load('./audio/kick/kick-1.mp3'));
chh = pyglet.media.StaticSource(pyglet.media.load('./audio/chh/chh-1.mp3'));
ohh = pyglet.media.StaticSource(pyglet.media.load('./audio/ohh/ohh-1.mp3'));
crash = pyglet.media.StaticSource(pyglet.media.load('./audio/crash/crash-1.mp3'));
ride = pyglet.media.StaticSource(pyglet.media.load('./audio/ride/ride-1.mp3'));

@window.event
def on_key_press(symbol, modifiers):
	if symbol == key.W:
		snare.play();
	elif symbol == key.A:
		tom1.play();
	elif symbol == key.S:
		tom2.play();
	elif symbol == key.D:
		kick.play();
	elif symbol == key.F:
		chh.play();
	elif symbol == key.G:
		crash.play();
	elif symbol == key.SPACE:
		ride.play();

@window.event
def on_draw():
	window.clear();
	background.blit(0,0);

pyglet.app.run();
