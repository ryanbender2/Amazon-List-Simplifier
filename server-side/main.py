from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

class ALS_Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Hello", "World")
        self.end_headers()

server_address = ("localhost", 5406)
httpd = HTTPServer(server_address, ALS_Server)
httpd.serve_forever()