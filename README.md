# ElectroKit

This is the software for the electronic drumset project for McHacks 2014. #TeamPhysClub


## Rough Outline

The program itself will, in my (Dakota's) mind at least, consist of pictures of different drums on a simple screen. This is the BARE MINIMUM for a GUI that we should definitely have done by the end of the weekend. If not, that's pathetic.

The bridge between software and hardware will come via the MakeyMakey kit. What the MakeyMakey does is simple: keystrokes. However, in the pyglet (and presumably pygame) game module(s), handling keystrokes is incredibly simple:

@window.event
def on_key_press(symbol, modifiers):
   if symbol == key.E:
      #(do stuff)

So we'll have sounds being played back in there. For audio playback, although pyglet (and again, pygame) will most certainly have functions that handle sound, we can simply use a proper library called "Snack" (see the "Tools" section).

For the hardware set-up, my idea is the following: keystrokes from the MakeyMakey are done, it seems, by completing the circuit. This is usually done by having the person hold a wire connected to the MakeyMakey (from here on, "the human end") and then press the conducting button which is also connected, thus completing the circuit. Instead, this human end should be connected to a power source at all times. This should then be connected to every drum/cymbal ("pad") but with a piezoelectric sensor breaking the circuit. When the pad is hit, the sensor produces some voltage and completes the circuit sending a signal. Done!


## Tools

For the modules: please make sure all of them work properly on your computer. Duh.

- MakeyMakey (Dakota has ordered one as of Jan. 23rd)
- piezoelectric sensors (Dakota or Kelly?)
- alligator clips, a lot of them
- some pads of some sort for the actual drums
- drumsticks (Kelly, dibs'd)
- switches of sorts (for hihat pedal and bass drum)
- Snack module (audio - http://www.speech.kth.se/snack/download.html)
- Pyglet module (gaming - http://www.pyglet.org/download.html)
- Pygame module (gaming - http://www.pygame.org/download.shtml)


## Issues

Here are a few "problems" we've already talked about or that we've thought of.

- What material are we going to use for the pads themselves?
- How will the piezoelectric sensor be put inside the pad?
- What will hold the drums up? (Do we have a frame?)
- How will the hihat pedal work, if we get it to at all?
- Will there be any delay?
- What's the deal with note velocity? (hitting the pad harder or softer won't change the volume output)


## Ideas

Add your ideas here.
- Have a filename below each picture; clicking on the picture will allow the user to change the sound from a list also on the screen; sounds should be organized: hihats, snare, toms, crash, ride, other cymbals, bass drum, miscellaneous, etc
- Be able to add sounds into the soundbank
- Be able to record drumming

## Questions

-WE'RE USING LINUX RIGHT?
