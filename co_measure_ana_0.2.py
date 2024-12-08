from machine import ADC, Pin
from neopixel import NeoPixel
from time import sleep

APIN=ADC(Pin(29))
RED = 255,0,0
BLUE = 0,0,255
OFF = 0,0,0
LED = Pin(16)
SIGNAL_PIN = Pin(0, Pin.OUT)
RCV_PIN = Pin(2, Pin.IN)

np = NeoPixel(LED,1)
CONVERSION_FACTOR = 3.3 / (65535)

SIGNAL_PIN.on()
def get_value():
    apin_value=APIN.read_u16()* CONVERSION_FACTOR
    return apin_value

ref = 0
captures = 10

#get reference point for current (known good at given temp/humidity)
def calibrate(data_points):
    ref=0
    for i in range(data_points):
        val = get_value()
        sleep(1)
        ref+=val
    ref=ref/data_points  
    return ref

ref = calibrate(captures)
print("REF",ref)


while True:
    apin_value=APIN.read_u16()* CONVERSION_FACTOR
    print("Voltage:", apin_value)
    sleep(1)
    if apin_value > ref + 0.2:
        np[0] = RED
        np.write()
    else:
        np[0] = OFF
        np.write()
    if RCV_PIN.value() == 1:
        np[0] = BLUE
        np.write()
        calibrate(captures)
        np[0] = OFF
        np.write()
    else:
        pass
        
        
    
