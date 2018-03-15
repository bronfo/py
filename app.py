try:
    import http.server as httpsvr
except ImportError:
    import SimpleHTTPServer as httpsvr
try:
    import socketserver
except ImportError:
    import SocketServer as socketserver

PORT = 8080

Handler = httpsvr.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
