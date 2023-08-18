import requests, json

base_url = 'https://127.0.0.1:443/api'
token_url = f'{base_url}/get_token'
protected_url = f'{base_url}/protected'

def get_token(username):
    headers = {'Username': username}
    response = requests.get(token_url, headers=headers, verify=False)
    print("Token Response Content:", response.text)
    return response.text

def send_protected_request(token_response):
    token_data = json.loads(token_response)
    token = token_data.get("jwt_token")
    if token:
        headers = {'Authorization': token}
        response = requests.get(protected_url, headers=headers, verify=False)
        print("Protected Response Content:", response.text)
        return response.text
    else:
        print("Error: Unable to extract JWT token from response.")
        return None

if __name__ == '__main__':
    admin_token = get_token('admin')
    print(f"Admin Token: {admin_token}")
    
    admin_protected_response = send_protected_request(admin_token)
    print("Admin Protected Response:", admin_protected_response)
