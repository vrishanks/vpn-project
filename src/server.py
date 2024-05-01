import argparse
import socket
import threading
import http.server
import socketserver
import os

def handle_client(client_socket):
    print("Received connection from:", client_socket.getpeername())
    client_socket.close()

def start_vpn_server(port):
    print("[*] Starting VPN server...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(5)
    print("[*] VPN server started on 0.0.0.0:", port)

    while True:
        client, addr = server.accept()
        print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def start_web_server(port):
    print("[*] Starting web server...")
    os.chdir('web_content')
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("[*] Web server started on 0.0.0.0:", port)
        httpd.serve_forever()

def main():
    parser = argparse.ArgumentParser(description="VPN Server")
    parser.add_argument("--port", type=int, default=8888, help="Port number")
    args = parser.parse_args()

    vpn_thread = threading.Thread(target=start_vpn_server, args=(args.port,))
    vpn_thread.start()

    web_thread = threading.Thread(target=start_web_server, args=(args.port + 1,))
    web_thread.start()

if __name__ == "__main__":
    main()
