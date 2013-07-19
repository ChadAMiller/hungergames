from __future__ import division, print_function
from Game import Game
from Players import Pushover, Freeloader, Alternator

# Bare minimum test game. See README.md for details.

if __name__ == '__main__':
    players = [Pushover(), Freeloader(), Alternator()]
    game = Game(players)
    game.play_game()
