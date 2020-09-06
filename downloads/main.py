# Complete project details at https://RandomNerdTutorials.com

def read_sensor():
  global temp, hum
  temp = hum = 0
  try:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
      msg = (b'{0:3.1f},{1:3.1f}'.format(temp, hum))

      # uncomment for Fahrenheit
      #temp = temp * (9/5) + 32.0

      hum = round(hum, 2)
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
  <h2>ESP DHT Server</h2>
  <p>
    <i class="fas fa-thermometer-half" style="color:#059e8a;"></i>
    <span class="dht-labels">Temperature</span>
    <span>"""+str(temp)+"""</span>
    <sup class="units">&deg;C</sup>
  </p>
  <p>
    <i class="fas fa-tint" style="color:#00add6;"></i>
    <span class="dht-labels">Humidity</span>
    <span>"""+str(hum)+"""</span>
    <sup class="units">%</sup>
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

