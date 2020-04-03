# M2Sa1-hear-examples.py
# -----------------------------------------------------------------
# Programme that generates tones from sine waves - A very basic version with limited amount of code lines for generating a sound
#
# Revision 0.4 - 03 apr 2020 - Knud Funch, Soundhub Danmark - LYDKit til undervisningsbrug - Region MidtJylland
# To be used as test material for coupling to Physics/Math class module 2.
#
# To be run from within Thonny IDE on both P, MAC and/or Raspberry PI.
#
from M2Sa0lib import *
# ------------------------------------------------------------------------------------------------------------------------------
#
# Below - some examples - do modify, run code, listen and reflect
#

sound_1 = generate_pure_tone(440,8000)               # Generate a pure sine wave/tone with freq 440 - try other values after having heard sound_1/5/9 as is.
sound_2 = -sound_1                                   # Flipping sound over x-axis meaning out of phase compared to sound_1
sound_3 = sound_1+sound_2                            # Going away - cancelling out 100% - if you try to play this nothing can be heard!

sound_4 = generate_pure_tone(443,8000)
sound_5 = sound_1+sound_4                            # adding two signals with slight diff in freq => beating (eg. 440 and 443 as values in sound_1 and sound_4 )
                                                     # do try to make new sounds by simple adding and subtration of pure waves


sound_9  = generate_freq_modulated_tone(440,8000,3)  # 3 as modulator frequence easy to hear. How does it compare to beats. Try something lower and listen
sound_10 = generate_freq_modulated_tone(440,8000,30) # 30 as modulator frequence now it can bee seen in M2Sb-e0-see-examples.py. Still easy to hear

# Below the actual playback of a sound - Listen to the sound/wave you just made
# use -1 as parameter to make sound play 'forever' that is within Thonny until you press stop
# with no parameter it plays the lenght defined by constant 'd' (in M2Salib) that you can change as well to get a longer sounding tone
#
pygame.sndarray.make_sound(sound_1).play(-1)         # try to change sound to play eg. sound_5 instead of sound_1, and sound_9 to compare beats with FM modulated
                                                     


