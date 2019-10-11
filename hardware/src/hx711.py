from machine import Pin, freq

def read(SCK=15, DAT=13):
    """ reads a raw value from hx711 """

    data = Pin(DAT, Pin.IN)
    sck = Pin(SCK, Pin.OUT, value=0)
    
    initialFreq = freq() # so we can slow it down afterwards
    freq(160000000) # hx711 needs a high clock frequency :o
    
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

        freq(initialFreq) # back to initialFreq
    
    return value

def scale(value,rawmin=100941, rawmax=274919, rangemin=0, rangemax=100):
    """ scales a raw value to an output range
        rawmin int - the raw scale reading for empty
        rawmax int - the raw scale reading for full
        rangemin int - the output value for empty 
        rangemax int - the output value for full 
    """

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - rawmin) / float(rawmax - rawmin)

    # Convert the 0-1 range into a value in the right range.
    value = rangemin + (valueScaled * ((rangemax * 10) - rangemin))

    value = value // 10 * 10 // 10 # float to int

    return max(value, rangemin) # value must be greater or equal to rangemin

