
import base64
import json

import requests
'''
curl https://api.mysportsfeeds.com/v2.1/pull/nfl/2020-2021-regular/standings.json \
            -u '1c245ef4-217e-417c-964c-ab4c3f:MYSPORTSFEEDS'
'''
apikey_token = '1c245ef4-217e-417c-964c-ab4c3f'
def send_request(query, args=None):
    result = {}
    url = f'https://api.mysportsfeeds.com/v2.1/pull/{query}'
    params = args if args else {}
    try:
        response = requests.get(
            url=url,
            params=params,
            headers={
                "Authorization": "Basic " + base64.b64encode(f'{apikey_token}:MYSPORTSFEEDS'.encode('utf-8'))
                            .decode('ascii'),
            }
        )
        if response.status_code == 200:
            result = response.content.decode('utf-8')
            result = json.loads(result)
            return result
        else:
            print(f'HTTP Request failed with status code {response.status_code}')
            return None

    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        return None

result = send_request('nfl/2020-2021-regular/standings.json')
# result is a dict
print(result)
# print all the team names
teams = result['teams']
# print as formatted string
formatted = json.dumps(result, indent=2)
print(formatted)

# Traverse result
for item in teams:
    team = item['team']
    name = team['name']
    city = team['city']
    print(f'Team: {name} in city {city}')
