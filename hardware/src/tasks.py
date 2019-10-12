import uasyncio as asyncio

async def connect():
    """ connects to a wifi network """
    
    import network
  
    from const import essid, password

    sta_if = network.WLAN( network.STA_IF )
    ap_if = network.WLAN( network.AP_IF )

    sta_if.active( True ) # enable staion mode
    ap_if.active( False ) # disable accesspoint mode

    if not sta_if.isconnected():
        print('connecting to wifi')
        sta_if.connect( essid, password )
        while not sta_if.isconnected():
            await asyncio.sleep(1)


async def wakereason(state):
    """ determines the waking reaspn """
    from machine import reset_cause, DEEPSLEEP_RESET, WDT_RESET

    if reset_cause() == DEEPSLEEP_RESET:
        print('woken from deep sleep')
        state.emit('deepsleepwake')
    
    elif reset_cause() == WDT_RESET:
        print('woken from watch dog reset')
        state.emit('watchdogwake')

    else:
        print('woken by hard reset')
        state.emit('resetwake')

async def tare():
        import hx711 as h
        h.tare()
        await asyncio.sleep(0.1)
        h.tare()
        await asyncio.sleep(0.1)
        h.tare()
        await asyncio.sleep(0.1)




async def update_weight():
    """ inserts a devices device history record """
    from gql import weight_mutate
    import hx711 as h
    
    while True:
        await connect()
        weight_mutate(h.sample())
        await asyncio.sleep(0.1)


async def ledflash():
    """ flashes the led """
    from const import LED
    from machine import Pin
    led = Pin( LED, Pin.OUT )
    while 1:
        led.value( 0 )
        await asyncio.sleep_ms( 1 )
        led.value( 1 )
        await asyncio.sleep( 5 )
