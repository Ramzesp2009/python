import requests

my_request = requests.get('https://www.python.org')

print(my_request)
# print(my_request.text)
print(my_request.status_code)