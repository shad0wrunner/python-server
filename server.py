import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 1337))
server_socket.listen(1)

while True:
    client_connection, client_address = server_socket.accept()
    print('Connected: ', client_address)
    received_data = client_connection.recv(1024)
    print(received_data)
    client_connection.sendall(b'HTTP/1.1 200 OK \n\n This is your server speaking.')
    client_connection.close()
