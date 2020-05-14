# Calling REST APIs with Python
# Use the requests library
# pip install requests
# https://www.geeksforgeeks.org/get-post-requests-using-python/

import requests

resp = requests.get('https://dog.ceo/api/breeds/list/all')
if resp.status_code != 200:
    # Something went wrong
    raise ApiError('GET /breeds/list/all {}'.format(resp.status_code))
print('Success!')
print (resp.json())

resp=requests.post('https://jsonplaceholder.typicode.com/posts')
