import socket
import argparse

def scan_ports(target, start_port, end_port):
    print(f"Scanning ports on {target}...\n")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} : Open")
        sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("start_port", type=int, help="Start port range")
    parser.add_argument("end_port", type=int, help="End port range")

    args = parser.parse_args()

    scan_ports(args.target, args.start_port, args.end_port)
