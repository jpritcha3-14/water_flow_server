import wiringpi
import time
from subprocess import Popen, PIPE

child = Popen(['python3', 'db_writer_child.py'], stdin=PIPE)
count = 0 
recordedZero = False
lastUpdate = time.time()

def gpio_callback():
    global count 
    global lastUpdate
    global recordedZero
    count += 1
    curTime = time.time()
    print("GPIO_CALLBACK! Count:", count)
    delta = curTime - lastUpdate

    # If flow is just starting up, reset timing
    if delta >= 5 and count == 1:
        lastUpdate = time.time()
        delta = 0
    
    if delta >= 5:
        curFlow = 0.02592313*count - 0.2476755
        curFlow = round(curFlow, 2)
        lastUpdate = time.time()
        count = 0
        recordedZero = False
        child.stdin.write(bytes(str(curFlow), 'utf-8') + b'\n')
        child.stdin.flush()

PIN_TO_SENSE = 18
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(PIN_TO_SENSE, wiringpi.GPIO.INPUT)
wiringpi.pullUpDnControl(PIN_TO_SENSE, wiringpi.GPIO.PUD_DOWN)

wiringpi.wiringPiISR(PIN_TO_SENSE, wiringpi.GPIO.INT_EDGE_RISING, gpio_callback)
print('GPIO Setup Complete')

while True:
    wiringpi.delay(5000)
    if (time.time() - lastUpdate >= 5 and not recordedZero
        or time.time() - lastUpdate >= 60 and recordedZero):
        child.stdin.write(bytes('0.00', 'utf-8') + b'\n')
        child.stdin.flush()
        recordedZero = True
        lastUpdate = time.time()
        count = 0
