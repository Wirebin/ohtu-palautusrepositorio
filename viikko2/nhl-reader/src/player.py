class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.games = dict['games']

    def __str__(self):
        return f"{self.name:23}{self.team:18}{self.goals} + {self.assists} = {self.goals+self.assists}"
