
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
