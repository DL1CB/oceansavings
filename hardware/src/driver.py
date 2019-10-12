
import uasyncio as asyncio
from machine import Pin, freq

data = Pin(5, Pin.IN)
sck = Pin(4, Pin.OUT, value=0)
freq(160000000) #hx711 needs a high clock frequency :o
tareMin = 0

def translate(value, leftMin, leftMax, rightMin, rightMax):
    """ transaltes a range in input value to a range of output values """
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def readHX711():
    """ reads a raw value translates it to grams """
    value = 0
    if data.value() == 0:

        for i in range(24):
            sck.value(1)
            sck.value(0)
            value = value << 1 | data.value()

        for j in range(1):
            sck.value(1)
            sck.value(0)

        # convert 2's complement to integer
        if value & (1 << (24 - 1)):
            value -= 1 << 24

    return value

def tare(product=None, prop=None, value=None):
    global tareMin
    tareMin = readHX711()

def read():
    return translate(readHX711(), tareMin, (12700 + tareMin), 0, 1000) // 10 * 10  // 10

async def pollTask(product):
    """ asyncronously poll the hardware and commmit data to the product model """
    while 1:
        await asyncio.sleep(1)
        """ commit _weight input to product property weight"""
        #if product.props['unit'] == 1:  # grams
        product.commit('weight',  read())
        #if product.props['unit'] == 2:  # newtons
        #    product.commit('weight',  read() // 100)
        #if product.props['unit'] == 2:  # kilograms
        #    product.commit('weight',  read() // 1000)

def startdriver(product):
    """ initialize and start the hardware driver as a daemon """
    tare()
    tare()
    tare()
    # listen for product events  (uncomment as needed)
    product.on('tare',tare)
    # add a pollTask ot the event loop
    loop = asyncio.get_event_loop()
    loop.create_task(pollTask(product))

def stopdriver(product):
    """ stop and finalize the hardware driver """
    pass