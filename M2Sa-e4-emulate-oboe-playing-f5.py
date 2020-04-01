# M2Sa-e4-emulate-oboe-f5.py
# -----------------------------------
# Using M2Salib.py to make series with all overtones gradually and play them to hear how they sound.
#
# Revision 0.3 - 01 Apr 2020 - Knud Funch, Soundhub danmark - LYDKit til undervisningbrug - Region MidtJylland
# To be used as material in module 2 test in Physics/Math class
#
# To be run from within Thonny IDE on either PC, MAC (or Raspberry PI).
#
from M2Salib import *
# ------------------------------------------------------------------------------------------------------------------------------
#
# Below   - Example 4 - emulate oboe playing f5
#           See https://www.youtube.com/watch?v=fwtA2-Nhixw&feature=youtu.be
#           (at time 4:52 for oboe example)
#         

bf = 698.456      # Keep bf*13 < 1/2 of sf !!   # try other fundamentals
ba = 32000        # full scale with signed 16-bit amplitude

f1  = generate_pure_tone(bf,ba*0.1122)      # fundamental

o2  = generate_pure_tone(2*bf,0.3890*ba)    # n'th overtone with n*fundamental freq  
o3  = generate_pure_tone(3*bf,0.0316*ba)    # and 1/n times fundamental amplitude 
o4  = generate_pure_tone(4*bf,0.0398*ba)
o5  = generate_pure_tone(5*bf,0.0354*ba)
o6  = generate_pure_tone(6*bf,0.0298*ba)
o7  = generate_pure_tone(7*bf,0.0119*ba)

overtones = [o2,o3,o4,o5,o6,o7]

print("fundamental")
sound = f1
ot = 2

for i in overtones:
    pygame.sndarray.make_sound(sound).play()
    time.sleep(d+0.05)
    print("plus overtone: ",ot)
    sound=sound+i
    ot = ot+1
pygame.sndarray.make_sound(sound).play(-1)  
