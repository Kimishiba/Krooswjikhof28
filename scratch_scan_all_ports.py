import socket
from concurrent.futures import ThreadPoolExecutor

ip = "192.168.1.41"

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    s.close()

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(1, 10000))
