import numpy as np
from numpy.random import Generator, PCG64

batting_avg = 0.25
batting_sd = 0.034
era_avg = 4.0
era_sd = 0.5

class Hitter:
    def __init__(self, batting_avg: float) -> None:
        self.batting_avg = batting_avg
    def get_ba(self) -> float:
        return self.batting_avg
class Pitcher:
    def __init__(self, era: float) -> None:
        self.era = era
    def get_era(self) -> float:
        return self.era
class Team:
    def __init__(self, hitters, pitchers) -> None:
        self.hitters = hitters
        self.pitchers = pitchers

def generate_team_ba() -> list:
    """Randomly generate a team and their batting averages."""
    rng = Generator(PCG64())
    team = []
    for i in range(9):
        player_ba = rng.normal(loc=batting_avg, scale=batting_sd)
        hitter = Hitter(batting_avg=player_ba)
        team.append(hitter)
    return team
# hitters = generate_team_ba()
# [print(hitter.get_ba()) for hitter in hitters]

def generate_team_era() -> list:
    """Randomly generate 3 pitchers for a team."""
    rng = Generator(PCG64())
    team = []
    for i in range(3):
        era = rng.normal(loc=era_avg, scale=era_sd)
        pitcher = Pitcher(era=era)
        team.append(pitcher)
    return team
# pitchers = generate_team_era()
# [print(pitcher.get_era()) for pitcher in pitchers]

# Generate 30 teams Pitchers & Hitters
teams = []
for i in range(30):
    hitters = generate_team_ba()
    pitchers = generate_team_era()
    teams.append(Team(hitters=hitters, pitchers=pitchers))
print(teams)


