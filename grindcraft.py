#!/usr/bin/env python

# Grindcraft: Minecraft soundtrack for your daily grind.
# By Mr Speaker. Dot net.
# v0.1

import os
import time
import random
import pygame.mixer

#### OPTIONS ####
oneFullDay = 3 * 60 # minutes. One Minecraft day is 20 minutes.
volume = 1.0 # 0 to 1
resources = os.getenv("HOME") + "/Library/Application Support/minecraft/resources/"
scaryCaveSounds = True
playOneOnLoad = True
debug = True

#### NOPTIONS ####
def oggs(dir):
    songs = filter(lambda file: file.endswith('.ogg'), os.listdir(resources + dir))
    return map(lambda song: [dir, song], songs)
    
def mins2Days(mins):
    return str(round(mins / 60.0 / oneFullDay, 1))
    
def log(msg): 
    if debug: print msg

# Setup files
music = oggs("music")
newMusic = oggs("newmusic")
aPinchOfGenius = []

c418 = music + newMusic + aPinchOfGenius
c418scary = oggs("newsound/ambient/cave")

# Setup pygame mixer
pygame.mixer.init()
pygame.mixer.music.set_volume(volume)

if playOneOnLoad:
    sound = random.choice(c418)
    pygame.mixer.music.load(os.path.join(resources, sound[0], sound[1]))
    pygame.mixer.music.play()

# initial sleeps
oneDay = oneFullDay * 60
halfADay = oneDay / 2

songTime = random.randrange(0, halfADay)
caveTime = random.randrange(oneDay, 3 * oneDay)
songIsNext = True

log("One day is " + str(oneFullDay) + " minutes.")
log("Next song in " + mins2Days(songTime) + " days")

# play songs
time.sleep(songTime)

while(True):
    sound = random.choice(c418 if songIsNext else c418scary)
    path = os.path.join(resources, sound[0], sound[1])

    if pygame.mixer.music.get_pos() == -1:
        log("Playing sound " + sound[1] + ".")
        pygame.mixer.music.stop()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()

    if songIsNext:
        caveTime = caveTime - songTime
        songTime = random.randrange(halfADay, oneDay)
    else:
        songTime = songTime - caveTime
        caveTime = random.randrange(oneDay, 3 * oneDay)
    songIsNext = True if not scaryCaveSounds else songTime < caveTime
    
    log("Next song in " + mins2Days(songTime) + " days. Next cave in " + mins2Days(caveTime) + " days.")
    time.sleep(songTime if songIsNext else caveTime)

