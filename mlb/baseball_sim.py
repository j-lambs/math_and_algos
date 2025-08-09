import numpy as np
from numpy.random import Generator, PCG64

class Player:
    def __init__(self, batting_avg: float) -> None:
        self.batting_avg = batting_avg
    def get_ba(self) -> float:
        return self.batting_avg


batting_avg = 0.25
batting_sd = 0.034

# create random number generator
rng = Generator(PCG64())
team = []
for i in range(9):
    player_ba = rng.normal(loc=batting_avg, scale=batting_sd)
    player = Player(batting_avg=player_ba)
    team.append(player)

for player in team:
    print(player.get_ba())
