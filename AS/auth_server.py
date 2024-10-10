import socket

records = {}

def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', 53533))

    while True:
        data, addr = sock.recvfrom(1024)
        lines = data.decode().split('\n')
        if "VALUE" in lines[2]:
            name = lines[1].split('=')[1].strip()
            value = lines[2].split('=')[1].strip()
            records[name] = value
            response = f"TYPE=A\nNAME={name}\nVALUE={value}\nTTL=10\n"
            sock.sendto(response.encode(), addr)
        else:
            name_query = lines[1].split('=')[1].strip()
            response_value = records.get(name_query, 'Not Found')
            response = f"TYPE=A\nNAME={name_query}\nVALUE={response_value}\nTTL=10\n"
            sock.sendto(response.encode(), addr)

if __name__ == '__main__':
    start_server()
