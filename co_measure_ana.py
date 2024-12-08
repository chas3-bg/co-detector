from machine import ADC, Pin
from neopixel import NeoPixel
from time import sleep

APIN=ADC(Pin(29))
RED = 255,0,0
OFF = 0,0,0
LED = Pin(16)
np = NeoPixel(LED,1)
CONVERSION_FACTOR = 3.3 / (65535)

def get_value():
    apin_value=APIN.read_u16()* CONVERSION_FACTOR
    return apin_value
ref = 0
captures = 5
for i in range(captures):
    val = get_value()
    sleep(1)
    print(val)
    ref+=val
    
    
ref= ref/captures
with open("ref.txt", "a") as ref1:
    ref1.write("Data points:")
    ref1.write(str(captures) + "\n")
    ref1.write("Average:" )
    ref1.write(str(ref) + "\n")


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
        
    