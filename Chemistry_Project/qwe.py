from machine import I2C, Pin
from urtc import DS1307
from ssd1306 import SSD1306_I2C
import time
import utime

#########################################################################################################

led = Pin(25, Pin.OUT)
Button = Pin(16, Pin.IN)
Out_PIN = Pin(17, Pin.OUT)

#########################################################################################################

WIDTH = 128
HEIGHT = 32

oled_i2c = I2C(1, scl = Pin(19), sda = Pin(18), freq=400000) 

display = SSD1306_I2C(WIDTH,HEIGHT,oled_i2c)

#Moisture_sensor = Machine.ADC(0)

i2c_rtc = I2C(0,scl = Pin(1),sda = Pin(0),freq = 400000)
rtc = DS1307(i2c_rtc)

set_Time = int(0)

################################### scan i2c bus for available devices ###################################

result = I2C.scan(i2c_rtc)
result2 = I2C.scan(oled_i2c)

###########################################################################################################

print("I2C scan result : ", result)

if result2 != []:
    led.high()
    time.sleep(1)
    led.low()
    time.sleep(0.1)
    led.high()
    time.sleep(0.1)
    led.low()
    time.sleep(0.1)
    led.high()
    time.sleep(0.1)
    led.low()
    time.sleep(0.1)
    led.high()
    time.sleep(0.1)
    led.low()
    time.sleep(0.1)
    led.high()
    time.sleep(0.1)
    led.low()
    time.sleep(2)
else:
    print("retry")

##############################################################################################################

if result != []:
    display.fill(0)
    print("I2C connection successfull")
    display.text("RTC I2C-0 ctd",10,15)
    display.show()
    time.sleep(1)
    display.fill(0)
    led.high()
    time.sleep(1)
    led.low()
else:
    print("retry")

###############################################################################################################

def read_temp():
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    formatted_temperature = "{:.1f}".format(temperature)
    string_temperature = str("Temperature:" + formatted_temperature)
    print(string_temperature)
    time.sleep(2)
    return string_temperature

################################################################################################################

while True:
    (year,month,date,day,hour,minute,second,p1)=rtc.datetime() #(year,month,date,day,hour,minute,second,ms)    
    
    display.fill(0)
    temperature = read_temp()
    display.text(temperature,0,0)
    display.show()
    display.text(str(hour)+ ":"+str(minute)+ ":"+str(second) ,30,13)
    display.show()
    print(hour,":",minute,":",second)
    display.text(str(set_Time)+":00",43,25)
    display.show()
    display.fill(0)
    time.sleep(1)
    
    
