import time
import pyupm_buzzer as upmBuzzer

# Create the buzzer object using GPIO pin 5
buzzer = upmBuzzer.Buzzer(5)

chords = [upmBuzzer.DO, upmBuzzer.RE, upmBuzzer.MI, upmBuzzer.FA, 
          upmBuzzer.SOL, upmBuzzer.LA, upmBuzzer.SI, upmBuzzer.DO, 
          upmBuzzer.SI];

# Print sensor name
print buzzer.name()

# Play sound (DO, RE, MI, etc.), pausing for 0.1 seconds between notes
for chord_ind in range (0,7):
    # play each note for one second
    print buzzer.playSound(chords[chord_ind], 1000000)
    time.sleep(0.1)

print "exiting application"

# Delete the buzzer object
del buzzer
