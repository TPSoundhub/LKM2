# see-examples-3.py
# -----------------------------------------
# make series with overtones and plot them to see how they look.
#
# Revision 0.5 - 25 Nov 2020 - Knud Funch, Soundhub danmark - LYDKit til undervisningbrug - Region MidtJylland
# To be used as material in module 2 test in Physics/Math class
#
# To be run from within Thonny IDE on either PC, MAC (or Raspberry PI).
#
from M2HEARlib import *
from M2SEElib import *
# ------------------------------------------------------------------------------------------------------------------------------
#
# Below   - Example 1 - play:
#         - Fundamantal frequency 
#         - Fundamantal frequency plus all overtones/Harmonics
#         - Fundamantal frequency plus odd overtones 
#
# Q - How does this relate to standing waves in tubes? Can you explain?
#         

bf = 880        
ba = 8000

f1  = generate_signal(bf,ba)          # fundamental

o2  = generate_signal(2*bf,1/2*ba)    # n'th overtone with n*fundamental freq  
o3  = generate_signal(3*bf,1/3*ba)    # and 1/n times fundamental amplitude 
o4  = generate_signal(4*bf,1/4*ba)
o5  = generate_signal(5*bf,1/5*ba)
o6  = generate_signal(6*bf,1/6*ba)
o7  = generate_signal(7*bf,1/7*ba)
o8  = generate_signal(8*bf,1/8*ba)
o9  = generate_signal(9*bf,1/9*ba)
o10 = generate_signal(10*bf,1/10*ba)
o11 = generate_signal(11*bf,1/11*ba)
o12 = generate_signal(12*bf,1/12*ba)
o13 = generate_signal(13*bf,1/13*ba)


all_overtones = [o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13]  # Saw

sound = f1
plot = plot_signal(f1)
plot.add_title("Fundamental")
play_signal(sound,forever=False)

ot = 2

for i in all_overtones:
    plot.clear_curve()
    sound=sound+i
    plot.add_title("incl alle overtoner til overtone: "+str(ot))
    plot.update(sound)
    play_signal(sound,forever=False)    
    ot=ot+1   
    
 