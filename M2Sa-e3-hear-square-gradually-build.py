# M2Sa-e3-hear-square-gradually-build.py
# -----------------------------------
# Using M2Salib.py to make series with odd overtones gradually added and play back to hear how it sound.
#
# Revision 0.3 - 01 Apr 2020 - Knud Funch, Soundhub danmark - LYDKit til undervisningbrug - Region MidtJylland
# To be used as material in module 2 test in Physics/Math class
#
# To be run from within Thonny IDE on either PC, MAC (or Raspberry PI).
#
from M2Salib import *
# ------------------------------------------------------------------------------------------------------------------------------
#
# Below   - Example 3 - play fundamental and gradually add odd overtones one by one:
#           Same pitch you perceive (freq of the fundamental) but different tonality compared to saw
#         

bf = 440        # Keep bf*13 < 1/2 of sf !!   # try other fundamentals
ba = 8000

f1  = generate_pure_tone(bf,ba)          # fundamental

print("fundamental", bf)
sound = f1
ot = 3

while ot*bf<sf/2:
    pygame.sndarray.make_sound(sound).play()
    time.sleep(d+0.05)
    print("plus overtone: ",ot, " freq: ",ot*bf)     
    sound=sound+generate_pure_tone(ot*bf,1/ot*ba)   # In this example we generate the tones on the fly with variables
    ot = ot+2
pygame.sndarray.make_sound(sound).play(-1)  
    