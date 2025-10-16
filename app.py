from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8181
#12
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        message = "<h1>Hello world</h1><p>Za4tite 1 labu please!!!</p>"
        self.wfile.write(message.encode("utf-8"))

if __name__ == "__main__":
    print(f"Server running on port {PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()