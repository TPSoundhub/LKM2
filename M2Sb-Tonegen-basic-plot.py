# M2Sb-Tonegen-basic-plot.py"
#
# Programme that generates sine waves like in tonegen basic mono and tonegen basic stereo,
# but here plot curves instead of playing them back on speakers.
#
# Revision 0.2 - 30Mar2020 - Knud Funch, Soundhub danmark - LYDKit til undervisningbrug - Region MidtJylland
# To be used as material in module 2 test in Physics/Math class
#
# To be run from within Thonny IDE on both PC MAC (and PI).
#
# As precondition the following libraries needs to be included in IDE - That is to be installed via TOOLS/MANAGE PACKAGES
# from within Thonny.
#
#         - numpy for putting sine into an array that can easily be manipulated/worked with on high level
#         - pygame - which already should be in place due to project 2019
#         - matplotlib - for plotting
#         - scipy - for FFT (fourier/spectrum)
#
#

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,fftfreq

sf = 44100  # Sampling frequence! samples pr second. Twice the highest freq you want to reproduce as minimum (nyquist)
            # 44100/48000 is a widely used and match with sound card and pygame sound default settings typically.  
d = 1.0     # duration - lenght of tone generated in seconds.

#
# Basic function to put a sine wave into an np array and given a frequnce and an amplitude as defined in parameters
# Any frequency below 1/2 the sampling rate given in sf can be used. If higher then it is not a pure tone anymore, and
#

def generate_pure_tone(freq,amp_max):  # same in both L/R channel in stereo
    t = np.arange(0,d,1/sf)
    # put sine wave with the frequency freq into table t
    x = np.sin(2*np.pi*freq*t)
    # Scale input from -/+1 to +/-amp_scale and within 16 bit integers due to sound card.
    x = (x*amp_max).astype(np.int16)
    return x                      

def generate_freq_modulated_tone(freq,amp_max,mf):
    t = np.arange(0,d,1/sf)
    x = np.sin(2*np.pi*(freq*t+np.sin(2*np.pi*mf*t)))   # mf as modulator freq 
    # Scale input from -/+1 to +/-amp_scale and within 16 bit integers.
    x = (x*amp_max).astype(np.int16)
    return x

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
    
#
# Now - Play around using the functions for generating different waves - below just some examples to get you started
#
#


sound_1 = generate_pure_tone(440,8000)        
sound_2 = -sound_1                                  # Flipping sound over x-axis meaning out of phase compared to sound_1
sound_3 = sound_1+sound_2                           # Going away - cancelling out

sound_4 = generate_pure_tone(443,8000)
sound_5 = sound_1+sound_4                           # adding two signals with slight diff in freq => beating

sound_6 = generate_pure_tone(12000,8000)
sound_7 = generate_pure_tone(12440,8000)
sound_8 = sound_6+sound_7                            # adding two signals with slight diff in freq => beating


sound_9  = generate_freq_modulated_tone(440,8000,3)  # 3 as modulator frequence easy to hear but hard to see in wave plot
sound_10 = generate_freq_modulated_tone(440,8000,30) # 30 as modulator frequence noe it can bee seen

sound_11 = -sound_1
                                                  
# etc.... combine sines into more complex wave forms and plot them to compare with other measurements snd sound ..

#plot_wave_and_freq(sound_1,50)
#plot_wave_and_freq(sound_2,50)   # flipped
#plot_wave_and_freq(sound_3,50)   # wave gone - signal cancelled out ideal cancellation..

#plot_wave_and_freq(sound_5,1000) # look at a whole sec to observe the beat effect of combining two almost identical waves = beats

#plot_wave_and_freq(sound_9,50)   # You have hard time seeing it on the wave but observe the freq - compare to how it sounds
#plot_wave_and_freq(sound_10,1000)   # Here you can see the modulation effect on the wave - compare with the beats one from above

plot_wave_and_freq(sound_1,50)
