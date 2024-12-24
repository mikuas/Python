import requests

if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/login'
    data = {
        'username': 'admin',
        'password': '114514'
    }

    response = requests.post(url, data=data)
    global token
    if response.status_code == 200:
        token = response.json()['access_token']
        print(f'Login successful token: {token}')

        # get api
        apiUrl = 'http://127.0.0.1:5000/api'
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = requests.get(apiUrl, headers=headers)
        if response.status_code == 200:
            print(response.text)
        else:
            print('Get API Error')
    else:
        print(f"Error: {response.text}")