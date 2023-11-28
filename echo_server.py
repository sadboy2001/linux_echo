import socket

def echo_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                headers = data.decode().split('\r\n')
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