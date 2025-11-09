from rich.console import Console as rConsole
from rich.table import Table as rTable

class TableHandler:
  def __init__(self):
    self.console = rConsole()
    self.table = ""

  def create_table(self, season, nationality, players):
    self.table = rTable(title=f"Season {season} players from {nationality}")
    self.table.add_column("Player", style="bright_cyan")
    self.table.add_column("teams", style="#de00de")
    self.table.add_column("goals", style="bright_green")
    self.table.add_column("assists", style="bright_green")
    self.table.add_column("points", style="bright_green")

    for player in players:
        self.table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.goals + player.assists))

  def show(self):
    self.console.print(self.table)
