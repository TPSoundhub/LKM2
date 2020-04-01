# M2Sb-e1-plot-fund-saw-square-triangle.py
# Using M2Sb-Tonegen-basic-plot.py to make series with overtones and plot them to see how they look.
#
# Revision 0.3 - 01 Apr 2020 - Knud Funch, Soundhub danmark - LYDKit til undervisningbrug - Region MidtJylland
# To be used as material in module 2 test in Physics/Math class
#
# To be run from within Thonny IDE on either PC, MAC (or Raspberry PI).
#
from M2Salib import *

import matplotlib.pyplot as plt
from scipy.fftpack import fft,fftfreq

def plot_wave_and_freq(x,ms):  # lenght of wave to plot in ms
    plt.subplot(121)
    length = (1/d)/1000*ms  # fraction of a sec to plot
    plt.axis([0,int(sf*length),-32000,32000])   # one sec samples in time and +/- 32 in amp (16 bit value)
    plt.plot(x)
    FFT = abs(fft(x))
    freqs = fftfreq(x.size, 1/sf)
    plt.subplot(122)
    plt.axis([0,8000,5,10])            # only positive below 8000 Hz and amp above 5 in log10
    plt.plot(freqs,np.log10(FFT))
    plt.show()
    
# ------------------------------------------------------------------------------------------------------------------------------
#
# Below   - Example 1 - plot:
#         - Fundamantal frequency 
#         - Fundamantal frequency plus odd overtones (giving a square like signal)
#         - Fundamantal frequency plus odd overtones with shifting sign (giving a triangle like signal)
#                                                    (phase shifted by pi)
#
# Note - The triangle is not perfect - Can you make it better?  Hint: faster decent of amplitude.
#        But can the difference be heard? (M2Sa-e1-hear-...)
#

bf = 440        # Keep bf*13 < 1/2 of sf !!
ba = 8000

f1  = generate_pure_tone(bf,ba)          # fundamental

o2  = generate_pure_tone(2*bf,1/2*ba)    # n'th overtone with n*fundamental freq  
o3  = generate_pure_tone(3*bf,1/3*ba)    # and 1/n times fundamental amplitude 
o4  = generate_pure_tone(4*bf,1/4*ba)
o5  = generate_pure_tone(5*bf,1/5*ba)
o6  = generate_pure_tone(6*bf,1/6*ba)
o7  = generate_pure_tone(7*bf,1/7*ba)
o8  = generate_pure_tone(8*bf,1/8*ba)
o9  = generate_pure_tone(9*bf,1/9*ba)
o10 = generate_pure_tone(10*bf,1/10*ba)
o11 = generate_pure_tone(11*bf,1/11*ba)
o12 = generate_pure_tone(12*bf,1/12*ba)
o13 = generate_pure_tone(13*bf,1/13*ba)


addall = f1+o2+o3+o4+o5+o6+o7+o8+o9+o10+o11+o12+o13   
addodd = f1+o3+o5+o7+o9+o11+o13                       
a_sodd = f1-o3+o5-o7+o9-o11+o13                     

plot_wave_and_freq(f1,10)          # sine for fundamental
plot_wave_and_freq(addall,10)      # series adding up saw
plot_wave_and_freq(addodd,10)      # series adding up square
plot_wave_and_freq(a_sodd,10)      # series adding up triangle - sort of


