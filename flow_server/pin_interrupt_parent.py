import wiringpi
import time
from subprocess import Popen, PIPE

child = Popen(['python3', 'db_writer_child.py'], stdin=PIPE)

def gpio_callback(callbackCount=[0], lastUpdate=[time.time()], child=child):
    callbackCount[0] += 1 
    curTime = time.time()
    print("GPIO_CALLBACK! Count:", callbackCount[0])
    delta = curTime - lastUpdate[0]
    if delta >= 5:
        curFlow = 0.02592313*callbackCount[0] - 0.2476755
        curFlow = round(curFlow, 2)
        lastUpdate[0] = time.time()
        callbackCount[0] = 0
        child.stdin.write(bytes(str(curFlow), 'utf-8') + b'\n')
        child.stdin.flush()

PIN_TO_SENSE = 18
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(PIN_TO_SENSE, wiringpi.GPIO.INPUT)
wiringpi.pullUpDnControl(PIN_TO_SENSE, wiringpi.GPIO.PUD_DOWN)

wiringpi.wiringPiISR(PIN_TO_SENSE, wiringpi.GPIO.INT_EDGE_RISING, gpio_callback)

print('setup complete')
while True:
    wiringpi.delay(2000)

