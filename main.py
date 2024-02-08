import requests
import datetime as dt
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
TOKEN = 'aweioklngaopijsdfkj'
USERNAME = 'awwab'
GRAPH_ID = 'graph1'
PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
GRAPH_ENDPOINTS = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
TODAY = dt.datetime.now().strftime('%Y%m%d')
UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"

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

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINTS, json=graph_params, headers=headers)
# print(response.text)

# posting a pixel

headers = {
    'X-USER-TOKEN': TOKEN
}
pixel_params = {
    'date': TODAY,
    'quantity': input('How much did you code today? ')
}

response = requests.post(url=PIXEL_ENDPOINT, json=pixel_params, headers=headers)
print(response.text)

# updating a pixel
update_params = {
    'quantity': '2.5'
}

# response = requests.put(url=UPDATE_ENDPOINT, json=update_params, headers=headers)
# print(response.text)

# response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
# print(response.text)