'''
import pyowm
from pyowm import OWM

owm = OWM('a66952168b007928153234c13aa8970d', language = 'ru')

obs = owm.weather_at_place('Kazan,ru')
w = obs.get_weather()

temp = int(w.get_temperature(unit='celsius').get('temp'))
status = w.get_detailed_status()

print('Температура на улице: %d' % temp)
print('На улице %s' % status)

print('__________')

print(owm.is_API_online())
print(obs.get_reception_time(timeformat='iso'))
print(w.get_reference_time(timeformat='iso'))
'''
x = ['x']
if len(x) == 0:
    print(0)
else:
    for a in x:
        if a == "egor":
            print('da')
        else:
            x.append('egor')

print(x)
