import battmon
import wifi
# Complete project details at https://RandomNerdTutorials.com
# https://randomnerdtutorials.com/micropython-esp32-esp8266-dht11-dht22-web-server/

bm = battmon.BatteryMonitor()

wifi.connect_wifi_ben()

def read_sensor():
  global solar_v, batt_v
  solar_v = batt_v = 0
  try:
    solar_v = bm.read_solar_voltage()
    batt_v = bm.read_battery_voltage()
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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  print('Content = %s' % str(request))
  sensor_readings = read_sensor()
  print(sensor_readings)
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()


# class NodeMcu:

#     # ESP8266 allows software PWM in all I/O pins: GPIO0 to GPIO16. PWM signals on ESP8266 have 10-bit resolution
#     # The ESP8266 supports interrupts in any GPIO, except GPIO16.


#     # GPIO16: pin is high at BOOT
#     # eUsed for deep sleep
#     d0 = Pin(16)

#     # Usually used for I2C SCL
#     d1 = Pin(5)

#     # Usually used for I2C SDA
#     d2 = Pin(4)

#     # GPIO0: boot failure if pulled LOW
#     d3 = Pin(0)

#     # GPIO2: pin is high on BOOT, boot failure if pulled LOW
#     d4 = Pin(2)

#     # GPIO14: SCLK
#     d5 = Pin(14)

#     # GPIO12: MISO
#     d6 = Pin(12)

#     # GPIO13: MOSI
#     d7 = Pin(13)

#     # GPIO15: boot failure if pulled HIGH
#     # GPIO15: CS
#     d8 = Pin(15)

#     # GPIO3: pin is high at BOOT
#     rx = Pin(3)

#     # GPIO1: pin is high at BOOT, boot failure if pulled LOW
#     tx = Pin(1)

#     # GPIO10: pin is high at BOOT
#     sd3 = Pin(10)

#     # GPIO9: pin is high at BOOT
#     sd2 = Pin(9)

