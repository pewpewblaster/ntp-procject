import socket

# Adresa i port poslužitelja
server_address = ('localhost', 12345)

# Stvaranje socket objekta
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Povezivanje na adresu i port
server_socket.bind(server_address)

# Slušanje dolaznih veza
server_socket.listen(1)

print("Waiting for a connection...")
connection, client_address = server_socket.accept()

try:
    # Prijem podataka iz toka
    with open('server_received.txt', 'wb') as file:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            file.write(data)

finally:
    # Zatvaranje veze i socket-a
    connection.close()
    server_socket.close()
