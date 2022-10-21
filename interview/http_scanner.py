import requests

response = requests.get('https://www.intuit.com/')

print(response.headers)

try:

    header = response.headers['X-Frame-Options'].lower()
    
    if ',' in header:
        header = header.split(',')[0]
    if  header == 'deny' or header == 'sameorigin': 
        print("X-Frame-Options header is present")

except KeyError:
        print('X-Frame-Options header not present')

try:
    
    header = response.headers['X-Content-Type'].lower()
    
    if ',' in header:
        header = header.split(',')[0]
    if  header == 'nosniff': 
        print("X-Content-Type header is present")

except KeyError:
        print('X-Content-Type header not present')

try:
    
    if response.headers['Strict-Transport-Security'].lower():
        print('Strict-Transport-Security header present')

except KeyError:
        print('Strict-Transport-Security header not present')

