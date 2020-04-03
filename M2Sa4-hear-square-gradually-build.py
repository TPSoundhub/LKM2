# M2Sa4-hear-square-gradually-build.py
# -----------------------------------
# Using M2Salib.py to make series with odd overtones gradually added and play back to hear how it sound.
#
# Revision 0.3 - 01 Apr 2020 - Knud Funch, Soundhub danmark - LYDKit til undervisningbrug - Region MidtJylland
# To be used as material in module 2 test in Physics/Math class
#
# To be run from within Thonny IDE on either PC, MAC (or Raspberry PI).
#
from M2Sa0lib import *
# ------------------------------------------------------------------------------------------------------------------------------
#
# Below   - Example 3 - play fundamental and gradually add odd overtones one by one:
#           Same pitch you perceive (freq of the fundamental) but different tonality compared to saw
#         

bf = 440        # Keep bf*max iterations < 1/2 of sf !!   # try other fundamentals
ba = 8000       # if kombined amp get over int 16 then distorsion - tehn reduce here or in amp line 29

f1  = generate_pure_tone(bf,ba)          # fundamental

print("fundamental", bf)
sound = f1
ot = 3

while ot*bf<sf/2:
    pygame.sndarray.make_sound(sound).play()
    time.sleep(d+0.05)
    amp = 1/ot*ba                               # try another ratio for amp careful as mentioned in line 18. Try eg. to add "*2" and hear the difference 
    print("plus overtone: ",ot, " freq: ",ot*bf, "amp: ",int(amp))     
    sound=sound+generate_pure_tone(ot*bf,amp)   # In this example we generate the tones on the fly with variables.
    ot = ot+2
pygame.sndarray.make_sound(sound).play(-1)  
    