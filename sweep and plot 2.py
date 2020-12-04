# "sweep and plot.py"
#
# Loop eksempel med løbende plot af signal
#
# Knud - SHD - 13 nov. 2020 Version 0.1 - En første simplificering mod forløb i Skanderborg
#              19 nov. 2020 Version 0.2 - Flyttet signal generering til bibliotek og droppet forskellig amp i h/v
#                                         SAMPLERATE og DURATION også i biblioteket. Samme bib til alle øvelser...
#              20 nov. 2020 Version 0.3 - Flytet funktionalitet ud i bibliotek så hoved program kan laves simpelt - få linier
#                                         samt at bibliotek så kan bruges til at lave simple SEE udgaver af HEAR eksemplerne ....
#              25 Nov. 2020 Version 0.4 - Droppet muligheden for delta. Kun med nu for at vise hvordan biblioteker kan bruges.
#                                         og at det der blev lavet til Herning forløb kan laves enkelt med bibliotekerne..
#                                         Udskrift i shell er interesant og kan evt. kombineres ind i plot bibliotek
#              04 Dec. 2020 Version 0.5 - Brug af simplificeret SEE lib hvor uskrift i shell er integreret i plot
#                                       
#
# Ved at ændre i konstanter kan man bruge den til lidt forskelligt.
#
# Når pogram er slut skal der blot klikkes indenfor plot vinduet for at få det fjernet og ryddet op
# Pt kommer der en række fejlmeldinger hvis man klikker i 'X' i vinduet både undervejs og til slut... (
# Brug stop stop
#
from M2HEARlib import *
from M2SEElib import *

# Bemærk atman ved frekvenser over 4000 begynder at have så få datapunkter pr. bølgelængde at plot begynder at se lidt underligt ud
# og over 6000 så begynder plot at være decideret fejl visende.
# Lyden er fortsat OK pga Nyquist
#
MAX_FREQ       = 2000      # Max freq i Hz - Der vi stopper
STEP_IN_SWEEP  = 2         # i Hz - den forskel der er mellem freq i while loop i sweep

#
# Globale variable - Start frekvens i de 2 kanaler.
#
freq = 100
first_round = True


while freq < MAX_FREQ:

    signal = generate_signal(freq,15000)
    if first_round:
        first_round=False
        plot=plot_signal(signal)
        plot.add_freq_title(freq)
    channel = play_signal(signal)   
    # Plot
    if not first_round:
        plot.clear_curve()
        plot.add_freq_title(freq)
        plot.update(signal)

    channel.stop()                    # Stop lyden inden en ny laves så de ikke blandes

    #
    # I dette eksempel lader vi frekvenserne i både højre og venstre vokse med STEP_IN_SWEEP for hver tur i while løkken.
    #
    freq+=STEP_IN_SWEEP
#
# Plot bliver stående til man klikker i X.

