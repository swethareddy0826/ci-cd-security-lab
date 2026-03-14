import requests

# fake API key for security detection
API_KEY = "123456SECRETKEY"

def get_data():
    url = "https://api.github.com"
    response = requests.get(url)
    return response.status_code

print(get_data())
