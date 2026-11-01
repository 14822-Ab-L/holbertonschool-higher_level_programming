#!/usr/bin/python3
"""A simple API server using Python's http.server."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handle HTTP requests for the simple API."""

    def do_GET(self):
        """Handle GET requests."""

        if self.path == "/":
            message = "Hello, this is a simple API!"

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(message.encode("utf-8"))

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            message = "OK"

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(message.encode("utf-8"))

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            message = "Endpoint not found"

            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(message.encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    """Start the HTTP server."""

    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)

    print("Starting server on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
