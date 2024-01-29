import socket

def perform_reconnaissance(target):
    try:
        # Résolution DNS
        target_ip = socket.gethostbyname(target)
        print(f"IP Address of {target}: {target_ip}")

        # Scan de ports
        open_ports = scan_ports(target_ip)
        print(f"Open ports on {target}: {open_ports}")

    except socket.error as e:
        print(f"Error: {e}")

def scan_ports(ip, start_port=1, end_port=1024):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open.")
            open_ports.append(port)

        sock.close()

    return open_ports

if __name__ == "__main__":
    target_host = input("Enter the target hostname or IP address: ")
    perform_reconnaissance(target_host)
