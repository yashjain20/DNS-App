from flask import Flask, request, jsonify
import socket

app = Flask(__name__)

@app.route('/register', methods=['PUT'])
def register():
    data = request.get_json()
    hostname = data['hostname']
    ip = data['ip']
    as_ip = data['as_ip']
    as_port = data['as_port']

    message = f"TYPE=A\nNAME={hostname}\nVALUE={ip}\nTTL=10\n"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (as_ip, int(as_port)))

    return jsonify({'message': 'Registered'}), 201

@app.route('/fibonacci')
def fibonacci():
    number = request.args.get('number')
    if not number.isdigit() or int(number) < 0:
        return jsonify({'error': 'Bad format'}), 400
    
    fib_value = calculate_fibonacci(int(number))
    return jsonify({'fibonacci': fib_value}), 200

def calculate_fibonacci(n):
    if n <= 1:
        return n
    else:
        return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)

if __name__ == '__main__':
    app.run(port=9090)
