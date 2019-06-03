import requests

headers = {
    'User-Agent':'PhantomJS'
}

response = requests.get('http://127.0.0.1:8000/',headers=headers)
print(response.text)