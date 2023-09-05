import requests

def main():
    url = 'http://localhost:5000/api/check_username'
    username = input("Enter username: ")

    data = {'username': username}

    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            data = response.json()
            message = data.get('message')
            print(f"Server response: {message}")
        else:
            print(f"Access denied. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
