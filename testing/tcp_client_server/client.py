import socket

# Adresa i port poslužitelja
server_address = ('localhost', 12345)

# Stvaranje socket objekta
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Povezivanje na poslužitelj
client_socket.connect(server_address)

try:
    # Slanje podataka u toku
    with open('client_data.txt', 'rb') as file:
        for data in file:
            client_socket.sendall(data)

finally:
    # Zatvaranje socket-a
    client_socket.close()