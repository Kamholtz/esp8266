import battmon
import wifi
import urequests as requests
import ujson
import time
import machine
# Complete project details at https://RandomNerdTutorials.com
# https://randomnerdtutorials.com/micropython-esp32-esp8266-dht11-dht22-web-server/

bm = battmon.BatteryMonitor()

connected = wifi.connect_wifi_ben()
request_count = 0
solar_v = 0
batt_v = 0

def read_sensor():
  global solar_v, batt_v
  global request_count
  solar_v = batt_v = 0
  try:
    if request_count % 2 == 1:
      batt_v = bm.read_battery_voltage()
      solar_v = bm.read_solar_voltage()
    else:
      solar_v = bm.read_solar_voltage()
      batt_v = bm.read_battery_voltage()

    request_count = request_count + 1

    if (isinstance(solar_v, float) and isinstance(batt_v, float)) or (isinstance(solar_v, int) and isinstance(batt_v, int)):
      msg = (b'{0:3.1f},{1:3.1f}'.format(solar_v, batt_v))

      solar_v = round(solar_v, 2)
      batt_v = round(batt_v, 2)
      return(msg)
    else:
      return('Invalid sensor readings.')
  except OSError as e:
    return('Failed to read sensor.')


rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

# check if the device woke from a deep sleep
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('Woke from a deep sleep')

if connected:
  print("Connect to WiFi")
  try:
    read_sensor()

    body = ujson.dumps({
      "i_device_id": 2,
      "i_channel_id": 1,
      "i_measurement_type": 1,
      "i_value": solar_v,
    })
    print ("Body: " + body)
    response = requests.post("http://192.168.1.21:5000/measurements", data = body)
    print("Resp: " + ujson.dumps(response))


    body = ujson.dumps({
      "i_device_id": 2,
      "i_channel_id": 2,
      "i_measurement_type": 1,
      "i_value": batt_v,
    })
    print ("Body: " + body)
    response = requests.post("http://192.168.1.21:5000/measurements", data = body)
    print("Resp: " + ujson.dumps(response))
  except OSError:
    print ("OSError ECONNABORTED")

# set RTC.ALARM0 to fire after 10 seconds (waking the device)
rtc.alarm(rtc.ALARM0, 10000)

# put the device to sleep
machine.deepsleep()