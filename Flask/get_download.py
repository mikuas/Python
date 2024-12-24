import requests

if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/download?token=this_is_ture_token'

    result = requests.get(url)

    if result.status_code == 200:
        print(result.text)
    else:
        print('Error')