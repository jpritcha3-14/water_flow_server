import wiringpi

PIN_TO_SENSE = 18
count = [0] 

def gpio_callback(callbackCount=count):
    callbackCount[0] += 1 
    print("GPIO_CALLBACK! Count:", callbackCount[0])

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(PIN_TO_SENSE, wiringpi.GPIO.INPUT)
wiringpi.pullUpDnControl(PIN_TO_SENSE, wiringpi.GPIO.PUD_DOWN)

wiringpi.wiringPiISR(PIN_TO_SENSE, wiringpi.GPIO.INT_EDGE_RISING, gpio_callback)

while True:
    wiringpi.delay(2000)
    print('count outside:', count[0])
