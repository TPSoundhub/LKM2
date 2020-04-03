# M2Sb1-see-examples.py"
# ---------------------------------------------------------------------------------------------------------
# Programme that generates waves like in M2Sa-e0-hear-examples.py (mono) and M2Sa-e0-hear-examples.py (stereo),
# but here plot curves instead of playing them back on speakers.
#
# Revision 0.4 - 03 apr 2020 - Knud Funch, Soundhub danmark - LYDKit til undervisningbrug - Region MidtJylland
# To be used as material in module 2 test in Physics/Math class
#
# To be run from within Thonny IDE on both PC,  MAC and/or Raspberry PI.
#
# As precondition the following libraries needs to be included in IDE - That is to be installed via TOOLS/MANAGE PACKAGES
# from within Thonny.
#
#         - numpy for putting sine into an array that can easily be manipulated/worked with on high level
#         - matplotlib - for plotting
#         - scipy - for FFT (fourier/spectrum)
#
#
from M2Sa0lib import *

import matplotlib.pyplot as plt
from scipy.fftpack import fft,fftfreq

def plot_wave_and_freq(x,ms):  # lenght of wave to plot in ms
    plt.subplot(121)
    length = (1/d)/1000*ms  # fraction of a sec to plot
    plt.axis([0,int(sf*length),-32000,32000])   # one sec samples in time and +/- 32 in amp 16 bit value
    plt.plot(x)
    FFT = abs(fft(x))
    freqs = fftfreq(x.size, 1/sf)
    plt.subplot(122)
    plt.axis([0,8000,5,10])            # only positive below 8000 Hz and amp above 5 in log10
    plt.plot(freqs,np.log10(FFT))
    plt.show()
    

# ------------------------------------------------------------------------------------------------------------------------------
#
# Below - some examples - do modify, run code, listen and reflect same as in hear version just here yuo make and see a plot of wave instead
#         Do not mind the divide by zero warning you get in the shell.
#

sound_1 = generate_pure_tone(440,8000)               # Generate a pure sine wave/tone with freq 440 - try other values after having seen sound_1/5/9 as is.
sound_2 = -sound_1                                   # Flipping sound over x-axis meaning out of phase compared to sound_1
sound_3 = sound_1+sound_2                            # Going away - cancelling out 100% - if you try to play this nothing can be seen all go to zero!
                                                     # but try the same in stereo where the 2 signals are in each channel in M2Sc-e0-examples.py

sound_4 = generate_pure_tone(443,8000)
sound_5 = sound_1+sound_4                            # adding two signals with slight diff in freq => beating (eg. 440 and 443 as values in sound_1 and sound_4 )
                                                     # do try to make new sounds by simple adding and subtration of pure waves


sound_9  = generate_freq_modulated_tone(440,8000,3)  # 3 as modulator frequence easy to hear but not so easy to see.
sound_10 = generate_freq_modulated_tone(440,8000,30) # 30 as modulator frequence now effect can bee seen easily.

# Below actual plot of the sound/wave generated. By changing the second parameter you can define how many miliseconds of the wave you would like to see
# Note with sample frequency of 44100 (in M2Salib) then eg 10ms means you get 441 samples on the x-axsis. The y-axis is amplityde, and as it is defined in
# M2Salib it is an 16-bit signed integer value, as the generator scales the sine accordingly for sound card reproduction reason.. 

plot_wave_and_freq(sound_1,10)
plot_wave_and_freq(sound_5,1000)  # To see the beat you must have a whole second in the plot!
plot_wave_and_freq(sound_9,100)   # hard to see modulation effect - but easy to hear M2Sa-e0-hear-examples.py.
plot_wave_and_freq(sound_10,100)  # easy to see - need 100 ms to see it though! Do note the difference in frequence spectrum compared to sound_9