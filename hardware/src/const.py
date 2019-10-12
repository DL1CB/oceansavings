from micropython import const

"""
Micropython | NodeMCU Board
-----------------------------------------
        0   | D3
        2   | D4 (also Led1 but inverse)*
        4   | D2
        5   | D1
        9   | SD2
        10  | SD3
        12  | D6
        13  | D7
        14  | D5
        15  | D8
        16  | D0 (also Led2 but inverse)*
"""

#GPIO
SCL = const(5) #D1 [output mode]
SDA = const(4) #D2 [input & output mode]

DAT = const(5) #D1 [input mode]
SCK = const(4) #D2 [output mode]

LED = const(2) #D4 [output mode]

# Currently unused gpio
D0 = const(16) #D0
D3 = const(0) #D3 
D5 = const(14) #D5
D6 = const(12) #D6

#wifi credentials
#essid = 'SummerTime'
#password = 'Calmhat436'
essid = 'DTShackathon'
password = 'HackTime247'

#server api url
url = 'https://stinkydb.herokuapp.com/v1/graphql'
deviceid = "1eb6aa14-4004-4a57-a0aa-dbf7a837c992"
token = None

#versioning
version = const(1)

