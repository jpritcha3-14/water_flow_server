import wiringpi
import time
import subprocess

print('running pin interrupt parent')

def gpio_callback(callbackCount=[0]):
    callbackCount[0] += 1 
    print("GPIO_CALLBACK! Count:", callbackCount[0])
    if callbackCount[0] % 1000 == 0:
        subprocess.Popen(['python3','manage.py','db_writer_child', str(callbackCount[0])])

PIN_TO_SENSE = 18
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(PIN_TO_SENSE, wiringpi.GPIO.INPUT)
wiringpi.pullUpDnControl(PIN_TO_SENSE, wiringpi.GPIO.PUD_DOWN)

wiringpi.wiringPiISR(PIN_TO_SENSE, wiringpi.GPIO.INT_EDGE_RISING, gpio_callback)

print('setup complete')
while True:
    wiringpi.delay(2000)

