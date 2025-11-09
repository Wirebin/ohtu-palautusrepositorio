class PlayerStats:
  def __init__(self, reader):
    self.reader = reader

  def top_scorers_by_nationality(self, nationality: str):
    p = self.reader.get_players()
    if nationality != "":
      p_filtered = filter(lambda p: p.nationality == nationality, p)
    else:
      p_filtered = p
    p_sorted = sorted(p_filtered, key=lambda p: p.goals + p.assists, reverse=True)

    return p_sorted
