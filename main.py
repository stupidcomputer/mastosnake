import requests
host = 'tilde.zone/'
prefix = 'api/v1/statuses'
token = '5mvTdpbj6lF55WRjky7IgOj-BNpH5MkBqSvaOeHLowM'
auth = {'Authorization': 'Bearer ' + token }
params = {
    'status': 'testing from python',
    'poll': {
        'options': ['a', 'b', 'c', 'd'],
        'expires_in': 86400,
        'multiple': False
    }
}

r = requests.post("https://" + host + prefix, json=params, headers=auth)
print(r.text)
