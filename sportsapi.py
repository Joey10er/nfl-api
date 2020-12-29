
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
            formatted = json.dumps(result, indent=2)
            print(formatted)
            return result
        else:
            print(f'HTTP Request failed with status code {response.status_code}')
            return None

    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        return None
team_gamesback = {}
def get_teams():
    query = 'nfl/2020-2021-regular/standings.json'
    result = send_request(query)
    teams = result['teams']
    # Traverse result
    for team_info in teams:
        team = team_info['team']
        name = team['name']
        city = team['city']
        abbreviation = team['abbreviation']
        overallRank = team_info['overallRank']
        rank = overallRank['rank']
        gamesback = overallRank['gamesBack']
        team_gamesback[abbreviation] = gamesback
        print(f'Team: {name} in city {city} is ranked {rank} and {gamesback} games back')
        pass
get_teams()
pass
def get_injuries():
    # print first name, last name, team, gamesback
    query = 'nfl/injuries.json'
    args = {'team': 'NYG'}
    result = send_request(query, args)
    for player in result['players']:
        abbreviation_ = player['currentTeam']['abbreviation']
        print(f"Player: {player['firstName']} {player['lastName']} playing for {abbreviation_} is {team_gamesback[abbreviation_]} games back")
    pass
get_injuries()



