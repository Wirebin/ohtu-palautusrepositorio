class PlayerStats:
  def __init__(self, reader):
    self.reader = reader

  def top_scorers_by_nationality(self, nationality: str):
    p = self.reader.get_players()
    p_filtered = filter(lambda p: p.nationality == nationality, p)
    p_sorted = sorted(p_filtered, key=lambda p: p.goals + p.assists, reverse=True)

    print(f"Players from {nationality}:\n")
    return p_sorted
