import socket

HOST = "127.0.0.1"
PORT = 65434

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            content = 'Well done'.encode('utf-8')
            conn.send(content)
            if not data:
                break
            headers = data.decode('utf-8').split('\r\n')
            method = headers[0].split()[0]
            status = 200
            for header in headers:
                if 'status=' in header:
                    try:
                        status = int(header.split('=')[1])
                    except ValueError:
                        pass
            response = f'HTTP/1.1 {status}\r\n'
            response += f'Method: {method}\r\n'
            response += '\r\n'.join(headers) + '\r\n\r\n'
            conn.sendall(response.encode())

