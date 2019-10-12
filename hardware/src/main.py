import uasyncio as asyncio  #https://github.com/peterhinch/micropython-async/blob/master/TUTORIAL.md

from const import version, deviceid
from tasks import update_weight, ledflash, tare

print('\n\n ocean saving - v',version, ' id:', deviceid)

# the async event loop prevents tasks from blocking each other
loop = asyncio.get_event_loop()
#loop.create_task( tare() )
loop.create_task( update_weight() )
loop.create_task( ledflash() )  
loop.run_forever()

