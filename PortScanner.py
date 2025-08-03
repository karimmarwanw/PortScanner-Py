import socket

def scanner(host, port_start, port_end):
    open_ports = []
    close_ports = []

    for port in range(port_start, port_end):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        else:
            close_ports.append(port)
    return open_ports, close_ports


host = input("Enter host: ")
try:
    port_start = int(input("Enter starting port: "))
    port_end = int(input("Enter ending port: "))
except ValueError:
    print("❌ Please enter valid numbers for ports.")
    exit()

print(f"\n🔍 Scanning {host} from port {port_start} to {port_end}...\n")

open_ports, close_ports = scanner(host, port_start, port_end)

print("✅ Open Ports:")
for port in open_ports:
    print(f" - Port {port}")

print("\n❌ Closed Ports:")
for port in close_ports:
    print(f" - Port {port}")