import SimpleHTTPServer
import SocketServer

PORT = 8080

class WebRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		self.wfile.write("hi")
Handler = WebRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
