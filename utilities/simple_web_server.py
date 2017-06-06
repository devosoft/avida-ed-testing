import threading
import os

from http.server import SimpleHTTPRequestHandler, HTTPServer


def run_http_server():
    """
    Creates a basic HTTP server so that the Avida-ED UI can be run locally.

    :return: None.
    """
    proj_dir = os.getcwd()
    os.chdir("C:/Users/Jake/PycharmProjects/avida_ed_ui")
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
