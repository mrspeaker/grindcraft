# Grindcraft

*A Minecraft soundtrack for your daily grind.*  
by Mr Speaker. Dot net.  
v0.1  

The problem with the real world is it's not enough like Minecraft. The fix is simple: pipe haunting and beautiful C418 tracks at various random times throughout the day, in a Minecraft-y fashion. To keep you on your toes, add in some rare-but-scary cave sounds. Voila.

## To play:

$ python grindcraft.py &

* Set "debug" to False if you don't want to see the time info
* Set the oneFullDay to vary the amount of tracks (see below)

## Requires:

* Python
* Pygame to play ogg files
* Minecraft installed at default Mac location

(I'm looking to reduce the requirements for ogg playing, and cross-platforming etc... any suggestions welcomed)  
(Remember, these songs have a looong silent intro - so wait a bit if it ain't working!)

## How often do the tunes play?

According to the Minecraft Wiki: "In-game music is cued by the time of day, with a random track being played at sunrise, sunset, noon and midnight.". But this is nonsense. A brief reverse-engineering of the Minecraft sound engine shows something like so:

    ticksBeforeMusic = rand.nextInt(half a day) // (one Minecraft day is 24000 ticks)
    every tick:
        subtract 1 from ticksBeforeMusic.
        if ticksBeforeMusic == 0:
            play a random C418 track
            ticksBeforeMusic = rand.nextInt(half a day) + half a day

One day in Minecraft is about 20 minutes, but your work day is probably noticeably longer. To adjust the number of tracks you hear, change the oneFullDay variable at the top of the script. I like one day to go a couple of hours. Then when the tunes drift in you feel all warm and tingly.

To compensate for the tingly-ness, Grindcraft will also be scare you witless with random scary cave noises. In minecraft the cave noise algorithm is more complex. If you lived in a dark cave all day it would play every rand.nextInt(half a day) + quarter of a day. But it only plays if there's a really dark place near you, so it's much less often.

I'm not going to check the light level of your office, so Grindcraft just plays a random cave sound once every 1 to 2 days.

## Todo

* Make it work for other people, not just me (windows default dir etc.)
* Abstract pygame stuff so it's easy to choose the ogg player
* Error handling
