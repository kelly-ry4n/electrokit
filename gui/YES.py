import pyglet
from pyglet.window import key
from pyglet.media import Player
import random
import sys
sys.path += [sys.path[0] + '../../']
from piezo.PiezoThreading import VolumeThread
from Queue import Queue

in_q = Queue()
out_q = Queue()

vol = VolumeThread(in_q,out_q)
vol.start()


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

drums = {
	key.W:snare,
	key.A:tom1,
	key.S:tom2,
	key.D:kick,
	key.F:chh,
	key.G:crash,
	key.SPACE:ride
}

@window.event
def on_key_press(symbol, modifiers):
	p = Player()

	p.queue(drums[symbol])
	in_q.put(None)
	v = out_q.get(block=True)[1]
	print v
	p.volume = v
	print p.volume
	p.play()
	# snare.play();

@window.event
def on_draw():
	window.clear();
	background.blit(0,0);

pyglet.app.run();
