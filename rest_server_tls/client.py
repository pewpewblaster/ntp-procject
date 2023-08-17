import requests
import ssl
import socket

# Path to the server's self-signed certificate
server_certificate_path = 'ca.pem'  # Replace with the actual path

# Create an SSL context with the server's certificate
context = ssl.create_default_context(cafile=server_certificate_path)
url = 'https://127.0.0.1:443/api/resource'
token = '12345'
headers = {'Authorization': f'Bearer {token}'}
# Create a custom session
session = requests.Session()

# Send the request using the custom session and SSL context
response = requests.get(url, headers=headers, verify=False)
  # Set verify to True

# Print the response security details

# Check if the response used SSL/TLS (HTTPS)
print("Is SSL Used:", response.url.startswith('https'))

# Get the security protocol version from the SSL context
if response.url.startswith('https'):
    with socket.create_connection(('127.0.0.1', 443)) as sock:
        with context.wrap_socket(sock, server_hostname='127.0.0.1') as ssl_socket:
            print("Security Protocol:", ssl_socket.version())

            
# Check if the response is using a secure connection
print("Is Secure Connection:", response.url.startswith('https'))

# Check if the response generated any SSL warnings
print("SSL Warnings:", response.content)

