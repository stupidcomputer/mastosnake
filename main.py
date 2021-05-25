import requests
import json
import time
from mastosnake import Mastosnake as mastosnake
from snake import Snake as snake

host = 'tilde.zone/'
postend = 'api/v1/statuses'
getend = 'api/v1/polls/'
token = '5mvTdpbj6lF55WRjky7IgOj-BNpH5MkBqSvaOeHLowM'
auth = {'Authorization': 'Bearer ' + token }

def main():
    game = snake()
    mastogame = mastosnake(game)
    while True:
        data = mastogame.returnStatus()
        r = requests.post("https://" + host + postend, json=data, headers=auth)
        print("posting game status")

        if mastogame.game.gamestate == "gameover":
            print("gameover")
            time.sleep(10)
            game = snake()
            mastogame = mastosnake(game)
            continue

        time.sleep(120)

        poll_id = json.loads(r.text)['poll']['id']
        r = requests.get("https://" + host + getend + poll_id)
        mastogame.updateState(json.loads(r.text))
        print("game state has been updated")

        time.sleep(10)
        print("posting new game status")


#req = requests.post("https://" + host + prefix, json=params, headers=auth)
#print(req.text)
#print("https://" + host + prefix2 + json.loads(req.text)['id'])
#r = requests.get("https://" + host + prefix2 + json.loads(req.text)['poll']['id'])
#print(req.text)
#r = requests.get("https://" + host + prefix2 + '42003')
#print(r.text)
#mastosnake.updateState(json.loads(r.text))
#print(mastosnake.game.render())

main()
