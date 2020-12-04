# see-examples-1.py
# -----------------------------------------------------------------
# Programme that generates tones from sine waves - A basic version with limited amout of code lines for generating a sound.
#
# Revision 0.8 - 25 Nov 2020 - Knud Funch, Soundhub danmark - LYDKit til undervisningbrug - Region MidtJylland
# To be used as material for test in Physics/Math class
#
# To be run from within Thonny IDE on both PC,MAC and/or Raspberry PI.
#
from M2HEARlib import *
from M2SEElib import *

#---------------------------------------------------------------------------------------------------------------------------
#  Build and plot signals by simple modification of the below. Experiment and reflect..
#

sound_1 = generate_signal(440)           
sound_2 = -sound_1
sound_3 = sound_1+sound_2
sound_4 = generate_signal(443)
sound_5 = sound_1+sound_4

plot_signal(sound_1)
plot_signal(sound_2)
plot_signal(sound_3)
plot_signal(sound_4)
plot_signal(sound_5,time_to_plot=1000)

