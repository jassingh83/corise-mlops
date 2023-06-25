import requests
import json

REQUESTS_FILE_PATH = 'data/requests.json'
# URL = 'http://0.0.0.0:80/predict'
URL = 'http://127.0.0.1:8000/predict'

with open(REQUESTS_FILE_PATH, 'r') as file:
    for request_json in file:
        request = json.loads(request_json)
        # print(request_json)
        response = requests.post(URL, json=request)
        
        if response.status_code == 200:
            print(response.json())
        else:
            print("Failed to get reponse: ", response.status_code)
        