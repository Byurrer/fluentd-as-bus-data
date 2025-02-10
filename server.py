import http.server
import socketserver

class RequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from GET!\n")

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        print(f"\nBody: {body.decode('utf-8', errors='replace')}")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from POST!\n")

if __name__ == "__main__":
    PORT = 8000
    with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
        print(f"Run server port: {PORT}")
        httpd.serve_forever()
