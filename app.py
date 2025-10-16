from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8181

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        message = "<h1>Hello from Retivov</h1><p>Pаботает</p>"
        self.wfile.write(message.encode("utf-8"))

if __name__ == "__main__":
    print(f"Server running on port {PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()