import socket

def scanner(ip, port_start, port_end):
    open_ports = []
    close_ports = []

    for port in range(port_start, port_end):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        else:
            close_ports.append(port)
    return open_ports, close_ports
