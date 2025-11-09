from rich.prompt import Prompt as rPrompt
from player_reader import PlayerReader
from player_stats import PlayerStats
from table_handler import TableHandler

def main():
    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"]
    season = rPrompt.ask("Season", choices=seasons, default="2024-25")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    tables = TableHandler()

    while True:
        nationality = rPrompt.ask("Nationality", choices=reader.get_nationalities(), default="")
        players = stats.top_scorers_by_nationality(nationality)
        tables.create_table(season, nationality, players)
        tables.show()

if __name__ == "__main__":
    main()
