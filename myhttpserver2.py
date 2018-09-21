from http.server import HTTPServer, BaseHTTPRequestHandler

port = 7777

class MyHttpRequestHandler(BaseHTTPRequestHandler):
    pass


httpd = HTTPServer(('', port), MyHttpRequestHandler)
print('Server running on port', port)
httpd.serve_forever()