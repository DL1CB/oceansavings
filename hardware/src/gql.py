
from const import url,deviceid
from gqlclient import execute

def weight_mutate(weight):

    print('weight_mutate ', weight)
    execute('''
        mutation weight($weight: Int) {
        update_devices(where: {id: {_eq: "1eb6aa14-4004-4a57-a0aa-dbf7a837c992"}}, _set: {weight: $weight}) {
            returning {
            weight
            }
        }
        }
    ''',{"weight":weight})
    