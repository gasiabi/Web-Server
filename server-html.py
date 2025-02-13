from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8080

DIRECTORY = "public"

class MyHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def main():
    server = HTTPServer(("", PORT), MyHandler)
    print(f"Server running on http://localhost:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    main()
