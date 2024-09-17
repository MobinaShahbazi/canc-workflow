# from requests import SpiffArenaAPIClient
#
# client = SpiffArenaAPIClient()
# print(client.get_task_data(4,'f37338af-df02-4f1a-8e35-b9b5d4179e8d'))

import requests

# URL to which the request will be sent
url = 'https://api.example.com/post-endpoint'

# Data to be sent in the POST request
data = {
    'key1': 'value1',
    'key2': 'value2'
}

# Creating a request object
request = requests.Request('POST', url, data=data)

# Preparing the request
prepared_request = request.prepare()

# Sending the prepared request
response = requests.Session().send(prepared_request)

# Checking the status code of the response
if response.status_code == 200:
    print('POST request was successful!')
    print('Response:')
    print(response.json())  # Assuming the response is in JSON format
else:
    print('POST request failed with status code:', response.status_code)