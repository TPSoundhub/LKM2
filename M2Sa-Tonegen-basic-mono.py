# M2Sa - Tonegen-basic-mono.py
# -----------------------------------------------------------------
# Programme that generates tones from sine waves - A basic version with limited amount of code lines for generating a sound
#
# Revision 0.3 - 30 Mar 2020 - Knud Funch, Soundhub Danmark - LYDKit til undervisningsbrug - Region MidtJylland
# To be used as test material for coupling to Physics/Math class module 2.
#
# To be run from within Thonny IDE on both P, MAC and/or Raspberry PI.
#
# As precondition the following libraries needs to be included in IDE - That is to be installed via TOOLS/MANAGE PACKAGES
# from within Thonny.
#
#         - numpy for putting sine into an array taht can easily be manipulated/worked with on high level
#         - pygame - which already should be in place due to project 2019
#
# Tones can be made easy from within the Thonny/Python environment, which means there is a progression path for
# 'building interactive stuff' within the same platform.
#
# With simple modifications to this code you can make experiments giving some basic understanding of waves, intensity and harmonics....
#
#-----------------------------------------------------------------
# The code contain two basic functions for generating a sound wave:
# 
#   generate_pure_tone(freq,amp_max)
#   generate_freq_modulated_tone(freq,amp_max,mf)
# 
# both return an array wich defines a wave that can be played back by a call to a pygame function/method like:
#
#   pygame.sndarray.make_sound(sound_1).play()
# 
# where sound_1 is the wave returned from one of the two functions above or any combination of several by simple addition of one or more
# sound arrays.
#
# generate_pure_tone(freq,amp_max)
# --------------------------------
# Basic function to put a sine wave into an np array given a frequency and an amplitude defined in parameters
#
# Any frequency below 1/2 the sampling rate given in the constant sf can be used. If higher then it is not a pure tone anymore, and
# with a sf at 44100 or above you can not hear it.
#
# Amplitude as a value matching/relative to sound card 16-bit capability. To avoid clipping make sure the combined max ampitude in sounds
# generated is 1/2*65.535 as this is the max value possible in 16-bit (signed +/- 32,767)
#
# It is OK to try to get values that are higher - try and listen. Its not a pure tone anymore!
#
# generate_freq_modulated_tone(freq,amp_max,mf)
# ---------------------------------------------
# Similar to the above but the wave are frequency modulated by a frequence set in third parameter. Try it out and listen to
# what happens to the sound.
# ---------------------------------------
# Now - Play around using the functions for generating different waves - below the definition of the functions are some examples
# to get you started. Experiment by modifying the code. Combine sines into more complex sounds - listen and measure ...
#
# What are the amplitude steps/values to use for perceiving double the intensity?
# - Can you measure it?!
# - What are the typical used scale? Does it relate to what you observe?
#
# Try to combine several sounds by adding more sound together like sound_3 = sound_1 + sound_2 where sound 1 and 2 are with
# different frequencies and amplitudes.
#
# - If you add two sounds with only a few HZ between them in frequncy and same amplitude what do you observe?
#   (sound wise - listening - and meaurement wise?)
# - Can you explain?
#
# Try to combine base frequency sound with several odd or all harmonics with a decresing amplitude
#
# - What form does the sound take when measured? Try to use tonegen basic plot to see wave as a supplement.
# - Can you explain what that mean?
# - Explain any corelation to real instrument measurements if you observe any!
#
# Try to make a combination of sounds that match the spectrum for eg a trompet.
# - Why does it not osund like a real trompet?
# - Can another group/student by mesuring the signal gues what instrument you tried to emulate?
#
# etc.. etc ..
#
import pygame
import numpy as np

sf = 44100  # Sampling frequence! samples pr second. Twice the highest freq you want to reproduce as minimum (nyquist)
            # 44100/48000 is a widely used and match with sound card and pygame sound default settings typically.  
d = 3.0     # duration - lenght of tone generated in seconds.

def generate_pure_tone(freq,amp_max):
    # make an array with number of entries equal to d*sf with a step interval of 1/sf (sf samples pr sec)
    t = np.arange(0,d,1/sf)
    # put sine wave with the frequency freq into table t
    x = np.sin(2*np.pi*freq*t)
    # Scale input from -/+1 to +/-amp_scale and within 16 bit integers due to sound card.
    x = (x*amp_max).astype(np.int16)
    return x

def generate_freq_modulated_tone(freq,amp_max,mf):
    t = np.arange(0,d,1/sf)
    x = np.sin(2*np.pi*(freq*t+np.sin(2*np.pi*mf*t)))   # mf as modulator freq 
    x = (x*amp_max).astype(np.int16)
    return x

# initialise pygame mixer with proper values to match sound generated
# Here sampling freq=sf, and 16 bit (signed) to stay within soundcards basic capability and in mono
#
pygame.mixer.init(sf, -16, 1)

# ------------------------------------------------------------------------------------------------------------------------------
#
# Below - some examples - do modify, run code, listen and reflect

sound_1 = generate_pure_tone(440,8000)        
sound_2 = -sound_1                                   # Flipping sound over x-axis meaning out of phase compared to sound_1
sound_3 = sound_1+sound_2                            # Going away - cancelling out 100%

sound_4 = generate_pure_tone(443,8000)
sound_5 = sound_1+sound_4                            # adding two signals with slight diff in freq => beating

sound_6 = generate_pure_tone(12000,8000)             # at bringe noget som ikke er hørbart til noget hørbart - virker IKKE!! ?
sound_7 = generate_pure_tone(12440,8000)
sound_8 = sound_6+sound_7                            # adding two signals with slight diff in freq => beating


sound_9  = generate_freq_modulated_tone(440,8000,5)  # 3 as modulator frequence easy to hear. try something lower and listen
sound_10 = generate_freq_modulated_tone(1400,8000,8) # 30 as modulator frequence now it can bee seen

# Play sound - Listen to the sine curve you just made
# use -1 as parameter to make sound play 'forever' that is within Thonny until you press stop
# with no parameter it plays the lenght defined by constant 'd' that you can change as well to get a longer sounding tone
#
pygame.sndarray.make_sound(sound_9).play(-1)