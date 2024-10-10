from flask import Flask, request, jsonify
import requests
import socket

app = Flask(__name__)

@app.route('/fibonacci')
def fibonacci():
    try:
        hostname = request.args.get('hostname')
        fs_port = request.args.get('fs_port')
        number = request.args.get('number')
        as_ip = request.args.get('as_ip')
        as_port = request.args.get('as_port')

        if not all([hostname, fs_port, number, as_ip, as_port]):
            return jsonify({'error': 'Bad Request'}), 400

        query = f'TYPE=A\nNAME={hostname}\n'
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(query.encode(), (as_ip, int(as_port)))

        data, _ = sock.recvfrom(1024)
        ip_address = data.decode().split('\n')[2].split('=')[1].strip()

        response = requests.get(f'http://{ip_address}:{fs_port}/fibonacci?number={number}')
        return response.text, 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=8080)
