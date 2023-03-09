# author: gomiero1
# version: 0.0.2
# usage: /path/to/python3 /home/gomiero1/HTTP503Responder.py
# notes: change port as needed.
# requirements: python3

import http.server
import os

os.system('reset')
print('HTTP Server running on port 8088')


class RequestHandler(http.server.BaseHTTPRequestHandler):
    Page = 'Server is busy.'

    def do_get(self):
        self.send_response(503)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.send_header("User-Information", "Server is busy.")
        self.end_headers()

    def do_post(self):
        self.send_response(503)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.send_header("User-Information", "Server is busy.")
        self.end_headers()


if __name__ == '__main__':
    serverAddress = ('', 8088)
    server = http.server.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
