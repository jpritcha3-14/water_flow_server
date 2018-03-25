from http.server import CGIHTTPRequestHandler, HTTPServer

def run():
  print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  #server_address = ('127.0.0.1', 8081)
  server_address = ('', 80)
  httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
  print('running server...')
  httpd.serve_forever()

run()
