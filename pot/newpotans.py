import time
import Adafruit_ADS1x15



adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1

print('Press Ctrl-C for quit...')

while True:

    values = [0]*4
    for i in range(4):

        values[i] = adc.read_adc(i, gain=GAIN)

    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))

    time.sleep(0.2)
