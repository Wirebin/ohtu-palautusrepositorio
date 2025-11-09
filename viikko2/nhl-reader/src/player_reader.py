import requests
from player import Player

class PlayerReader:
  def __init__(self, url):
    self.url = url

  def get_players(self):
    response = requests.get(self.url).json()

    players = []

    for player_dict in response:
      player = Player(player_dict)
      players.append(player)

    return players

  def get_nationalities(self):
    response = requests.get(self.url).json()
    nats = []

    for player in response:
      if player['nationality'] not in nats:
        nats.append(player['nationality'])
    return sorted(nats)
