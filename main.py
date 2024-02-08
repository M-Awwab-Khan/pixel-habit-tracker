import requests

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
TOKEN = 'aweioklngaopijsdfkj'
USERNAME = 'awwab'

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINTS = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_params = {
    'id':'graph1',
    'name': 'Coding Graph',
    'unit': 'hr',
    'type': 'float',
    'color': 'momiji'
}

graph_headers = {
    'X-USER-TOKEN': TOKEN
}

response = requests.post(url=GRAPH_ENDPOINTS, json=graph_params, headers=graph_headers)
print(response.text)