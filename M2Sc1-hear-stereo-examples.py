# M2Sc1-hear-stereo-examples.py
# -----------------------------------------------------------------
# Programme that generates tones from sine waves - A basic version with limited amout of code lines for generating a sound.
#
# Revision 0.5 - 03 Apr 2020 - Knud Funch, Soundhub danmark - LYDKit til undervisningbrug - Region MidtJylland
# To be used as material for test in Physics/Math class
#
# To be run from within Thonny IDE on both PC,MAC and/or Raspberry PI.
#
from M2Sc0lib import *

#---------------------------------------------------------------------------------------------------------------------------
#  Build and play back sounds by simple modification of the below. Listen, measure, experiment and reflect..
#

sound_1 = generate_pure_tone(440,8000,In_phase)           # l/r in phase
sound_2 = generate_pure_tone(440,8000, Out_of_phase)      # l/r out of phase  - listen to the 2 and do you hear any difference? Why/why not?

sound_3 = generate_freq_modulated_tone(440,8000,3) 
sound_4 = generate_pure_tone(443,8000,In_phase)

sound_5 = sound_2+sound_4
sound_6 = sound_1+sound_4                          

print("playback sound_1 in phase in the 2 channels")
play_sound(sound_1,1,1,Once)
print("playback sound_2 same as sound_1 but out of phase in the 2 channels - compare to mono - why can we hear it this time?")
play_sound(sound_2,1,1,Once)

print("playback sound_3 FM in left channel only")
play_sound(sound_3,1,0,Once)
print("playback sound_3 FM in right channel only")
play_sound(sound_3,0,1,Once)

print("playback sound_5 - 2 and 4 added to beats in both channels sound 2 = 1 out of phase")
play_sound(sound_5,1,1,Once)
print("playback sound_5 - 1 and 4 added to beats in both channels")
play_sound(sound_6,1,1,Once)


print("playback sound_1 and sound_4 on top of each other forever. How does this compare with beats in mono? Use headphones as well as speakers")
play_sound(sound_1,0,1,Forever)   # 440 in right  - try with earphone - what happens - how does it compare to mono beats experiment?
play_sound(sound_4,1,0,Forever)   # 443 in left


# gives the option to make experiments, measurements and tasks with 
# - intensity addition from one to two speakers
# - with constructive and destructive interference
#
# and same tasks/questions in the basic mono version can of cource be made with this version as well but simpler code in mono version...

            