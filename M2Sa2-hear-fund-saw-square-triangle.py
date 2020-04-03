# M2Sa2-hear-fund-saw-square-triangle.py
# -----------------------------------------
# Using M2Salib.py to make series with overtones and play them back to hear how they sound.
#
# Revision 0.4 - 03 Apr 2020 - Knud Funch, Soundhub danmark - LYDKit til undervisningbrug - Region MidtJylland
# To be used as material in module 2 test in Physics/Math class
#
# To be run from within Thonny IDE on either PC, MAC (or Raspberry PI).
#
from M2Sa0lib import *
# ------------------------------------------------------------------------------------------------------------------------------
#
# Below   - Example 1 - play:
#         - Fundamantal frequency 
#         - Fundamantal frequency plus odd overtones (giving a square like signal - see M2Sb-e1-plot-fund-saw-square-triangle)
#         - Fundamantal frequency plus odd overtones with shifting sign (giving a triangle like signal)
#                                                    (phase shifted by pi)
#
# Note - Triangle and square sounds almost the same - Can you make it more differentiated?
#        Hint: Add more overtones to square.
#
# Q - How does the saw and the square relates to standing waves in tubes? Can you explain?
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

addall = f1+o2+o3+o4+o5+o6+o7+o8+o9+o10+o11+o12+o13  # saw
addodd = f1+o3+o5+o7+o9+o11+o13                      # square
a_sodd = f1-o3+o5-o7+o9-o11+o13                      # triangle

print("pure sine")
pygame.sndarray.make_sound(f1).play()
time.sleep(d+0.1)
print("saw")
pygame.sndarray.make_sound(addall).play()
while True:
    time.sleep(d+0.1)
    print("square")
    pygame.sndarray.make_sound(a_sodd).play()
    time.sleep(d+0.1)
    print("triangle")
    pygame.sndarray.make_sound(addodd).play()
    
    