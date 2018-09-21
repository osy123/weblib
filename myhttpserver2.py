from http.server import HTTPServer, BaseHTTPRequestHandler

port = 7777

class MyHttpRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        req_url = self.path[:self.path.find('?')]
        print(req_url)
        self.send_response(200)
        self.send_header('Content-Type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write('<h1>TEST</h1>'.encode('utf-8'))

httpd = HTTPServer(('', port), MyHttpRequestHandler)
print('Server running on port', port)
httpd.serve_forever()