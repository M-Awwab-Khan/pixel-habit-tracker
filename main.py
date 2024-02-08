import requests

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'

user_params = {
    "token": "aweioklngaopijsdfkj",
    "username": 'awwab',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)