# M2Sclib.py
#
# M2Sc - Basic tonegeneration functions in stereo  (two channels)
# -----------------------------------------------------------------
# Programme that generates tones from sine waves - A basic version with limited amout of code lines for generating a sound.
#
# It includes a bit more compared to the mono version of the lib M2Salib as a step up with regard to functionality. That is:
#       - Capability to control wheter or not sound is played in left or right channel only or in both
#       - Can generate pure tone with same sound in both left and right or with the two fully out of phase.
#       - Added a fundtion to play back the sound on top of pygame basic playfunction. It is called "play_sound" and takes 4 arguments.
#            - sound which is the sound array generated
#            - vol_l and vol_r for setting the play back volume in the 2 channels. Between 0 and 1. In that way panning can be made/controlled
#            - forever a boolean that takes True/False as arguments, True means it plays until stopped. False it plays as long as defined by 'd'
#                 - In the case of False the function will only return after sound has been played to the end. So if you want to play 2 sounds
#                   simultaneous then you must start them with True - then up till 8 sounds can be mixed together in playback.
#
# Revision 0.4 - 01 Apr 2020 - Knud Funch, Soundhub danmark - LYDKit til undervisningbrug - Region MidtJylland
# To be used as material for test in Physics/Math class
#
# To be run from within Thonny IDE on both PC,MAC and/or Raspberry PI.
#
# As precondition the following libraries needs to be included in IDE - That is to be installed via TOOLS/MANAGE PACKAGES
# from within Thonny.
#
#         - numpy  - for putting sine into an array taht can easily be manipulated/worked with on high level
#         - pygame - for generating and playing sound cross platform (PC/MAC/PI) and with opportunity for playing more at same time 
#
# To show a tone can be made easily from within Thonny/Python environment, which means there is a progression path for
# 'building stuff' within the same framework as shown in Module 1.
#
# This is the key reason for making it in python/thonny - as it is acknowledged a sine wave sound can be made in easiler way.
# The option for using it later as a building block is the reason for this path!
#

import time  
import pygame
import numpy as np

sf = 44100  # Sampling frequence! samples pr second. Twice the highest freq you want to reproduce as minimum (nyquist)
            # 44100/48000 is a widely used and match with sound card and pygame sound default settings typically.  
d = 3.0     # duration - lenght of tone generated in seconds.

In_phase     = True
Out_of_phase = False

Forever = True
Once    = False

#
# Basic function to put a sine wave into an np array and given a frequnce and an amplitude as defined in parameters
# Any frequency below 1/2 the sampling rate given in sf can be used. If higher then it is not a pure tone anymore, and
# with a sf at 44100 or above you can not hear it anyway.. aliasing effect can be heard though so ....
# Amplitude as a value matching/relative to sound card 16-bit capability.
#     To avoid clipping do make sure the combined
#     max ampitude ni sounds generated is 1/2*65.535 as this is the max value possible in 16-bit (signed +/- 32,767)
#     It is OK to try to get values that are higher - try and listen. Its not a pure tone anymore!
# compared with the basic mono version we here have one more parameter telling wheter or not to make the left/right channels
# in or out of phase - out of phase means fully out of phase (opposite values).


def generate_pure_tone(freq,amp_max,in_phase):  # same in both L/R channel in stereo
    t = np.arange(0,d,1/sf)
    # put sine wave with the frequency freq into table t
    x = np.sin(2*np.pi*freq*t)
    # Scale input from -/+1 to +/-amp_scale and within 16 bit integers due to sound card.
    x = (x*amp_max).astype(np.int16)
    if in_phase:
        x = np.dstack((x,x))[0]           # Due to stereo same signal in both left and right channel.
    else:
        x = np.dstack((x,-x))[0]          # just switching sign on all values means complete out of phase - same as y = np.sin(-2*np.pi*freq*t)
    return x                              # or said in other words mirrring in x-axis

def generate_freq_modulated_tone(freq,amp_max,mf):
    t = np.arange(0,d,1/sf)
    x = np.sin(2*np.pi*(freq*t+np.sin(2*np.pi*mf*t)))   # mf as modulator freq 
    # Scale input from -/+1 to +/-amp_scale and within 16 bit integers.
    x = (x*amp_max).astype(np.int16)
    x = np.dstack((x,x))[0]  # Same in both left and right channel 
    return x

def play_sound(sound,vol_l,vol_r,forever):
    channel = pygame.mixer.find_channel()
    channel.set_volume(vol_l,vol_r)
    if forever:
        channel.play(pygame.sndarray.make_sound(sound),-1)
    else:
        channel.play(pygame.sndarray.make_sound(sound))
        time.sleep(d+0.2)       # make sure sound plays to the end before ending this function
        
# initialise pygame mixer with proper values to match sound generated
# Here sampling freq=sf, and 16 bit (signed) to stay within soundcards basic capability and in stereo (2 channels)
#
pygame.mixer.init(sf, -16, 2)
