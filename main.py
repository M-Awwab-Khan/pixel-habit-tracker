import requests
import datetime as dt
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
TOKEN = 'aweioklngaopijsdfkj'
USERNAME = 'awwab'
GRAPH_ID = 'graph1'
PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
GRAPH_ENDPOINTS = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
TODAY = dt.datetime.now().strftime('%Y%m%d')

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_params = {
    'id': GRAPH_ID,
    'name': 'Coding Graph',
    'unit': 'hr',
    'type': 'float',
    'color': 'momiji'
}

graph_headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINTS, json=graph_params, headers=graph_headers)
# print(response.text)

# posting a pixel

pixel_headers = {
    'X-USER-TOKEN': TOKEN
}
params = {
    'date': TODAY,
    'quantity': '1.0'
}

response = requests.post(url=PIXEL_ENDPOINT, json=params, headers=pixel_headers)
print(response.text)