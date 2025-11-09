class Player:
    def __init__(self, player):
        self.name = player['name']
        self.nationality = player['nationality']
        self.team = player['team']
        self.goals = player['goals']
        self.assists = player['assists']
        self.games = player['games']

    def __str__(self):
        return f"{self.name:23}{self.team:18}{self.goals} + {self.assists} = {self.goals+self.assists}"
