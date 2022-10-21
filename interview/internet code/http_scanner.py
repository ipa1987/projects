import requests

url = 'https://api.github.com'

status = requests.status_codes
response = requests.get(url)

print(status)
print(response)
print(response.headers)
print(response.request.headers)

