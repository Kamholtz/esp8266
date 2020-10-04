import battmon
import wifi
import urequests as requests
import ujson
import time
# Complete project details at https://RandomNerdTutorials.com
# https://randomnerdtutorials.com/micropython-esp32-esp8266-dht11-dht22-web-server/

bm = battmon.BatteryMonitor()

wifi.connect_wifi_ben()
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

def web_page():
  html = """<!DOCTYPE HTML><html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
  <style>
    html {
     font-family: Arial;
     display: inline-block;
     margin: 0px auto;
     text-align: center;
    }
    h2 { font-size: 3.0rem; }
    p { font-size: 3.0rem; }
    .units { font-size: 1.2rem; }
    .dht-labels{
      font-size: 1.5rem;
      vertical-align:middle;
      padding-bottom: 15px;
    }
  </style>
</head>
<body>
  <h2>Solar Charger Server</h2>
  <p>
    <i class="fas fa-solar-panel" style="color: orange;"></i>
    <span class="dht-labels">Solar Panel Voltage</span>
    <span>"""+str(solar_v)+"""</span>
    <sup class="units">V</sup>
  </p>
  <p>
    <i class="fas fa-battery-three-quarters" style="color: deepskyblue;"></i>
    <span class="dht-labels">Battery Voltage</span>
    <span>"""+str(batt_v)+"""</span>
    <sup class="units">V</sup>
  </p>
</body>
</html>"""
  return html

while True:

  try:
    read_sensor()

    body = ujson.dumps({
      "i_device_id": 2,
      "i_channel_id": 1,
      "i_measurement_type": 1,
      "i_value": solar_v,
    })
    print ("Body: " + body)
    response = requests.post("http://192.168.1.8:5000/measurements", data = body)
    print("Resp: " + ujson.dumps(response))


    body = ujson.dumps({
      "i_device_id": 2,
      "i_channel_id": 2,
      "i_measurement_type": 1,
      "i_value": batt_v,
    })
    print ("Body: " + body)
    response = requests.post("http://192.168.1.8:5000/measurements", data = body)
    print("Resp: " + ujson.dumps(response))
  except OSError:
    print ("OSError ECONNABORTED")

  time.sleep(3)









# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('', 80))
# s.listen(5)

# while True:
#   conn, addr = s.accept()
#   print('Got a connection from %s' % str(addr))
#   request = conn.recv(1024)
#   print('Content = %s' % str(request))
#   sensor_readings = read_sensor()
#   print(sensor_readings)
#   response = web_page()
#   conn.send('HTTP/1.1 200 OK\n')
#   conn.send('Content-Type: text/html\n')
#   conn.send('Connection: close\n\n')
#   conn.sendall(response)
#   conn.close()

