import wiringpi
import time
from subprocess import Popen, PIPE

child = Popen(['python3', 'db_writer_child.py'], stdin=PIPE)
screen = Popen(['python3', 'screen_count.py'])

def gpio_callback(callbackCount=[0], child=child):
    callbackCount[0] += 1 
    print("GPIO_CALLBACK! Count:", callbackCount[0])
    if callbackCount[0] % 10 == 0:
        child.stdin.write(bytes(str(callbackCount[0]), 'utf-8') + b'\n')
        child.stdin.flush()

PIN_TO_SENSE = 18
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(PIN_TO_SENSE, wiringpi.GPIO.INPUT)
wiringpi.pullUpDnControl(PIN_TO_SENSE, wiringpi.GPIO.PUD_DOWN)

wiringpi.wiringPiISR(PIN_TO_SENSE, wiringpi.GPIO.INT_EDGE_RISING, gpio_callback)

print('setup complete')
while True:
    wiringpi.delay(2000)

