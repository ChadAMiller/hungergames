from __future__ import division, print_function
from argparse import ArgumentParser

from Game import Game
from bots import *
from Player import Player

# Bare minimum test game. See README.md for details.


def main():
    parser = ArgumentParser()
    parser.add_argument("-p", "--pushover", dest="pushover",
                        default=1, type=int,
                        help="the number of Pushover bots to play with")
    parser.add_argument("-f", "--freeloader", dest="freeloader",
                        default=1, type=int,
                        help="the number of Freeloader bots to play with")
    parser.add_argument("-a", "--alternator", dest="alternator",
                        default=1, type=int,
                        help="the number of Alternator bots to play with")
    parser.add_argument("-m", "--max-rep-hunter", dest="mrp",
                        default=1, type=int,
                        help="the number of MaxRepHunter bots to play with")
    parser.add_argument("-r", "--random", dest="random",
                        default=["1,.2", "1,.8"], nargs="*",
                        help="the number and value of Random bots to play " \
                        "with (in the form 'number,p_hunt' such that number " \
                        "is an int, and p_hunt is a float from 0-1)")
    parser.add_argument("-e", "--end-early", dest="end_early",
                        default=False, action="store_true",
                        help="end the game if 'Player' is eliminated")
    args = parser.parse_args()
    players = [Player()]

    i = 0

    while i < args.pushover:
         players += [Pushover()]
         i += 1

    i = 0

    while i < args.freeloader:
        players += [Freeloader()]
        i += 1

    i = 0

    while i < args.alternator:
        players += [Alternator()]
        i += 1

    i = 0

    while i < args.mrp:
        players += [MaxRepHunter()]
        i += 1

    for r in args.random:
        (num, value) = r.split(",")
        num = int(num)
        value = float(value)
        assert value >= 0.00 and value <= 1.00
        i = 0

        while i < num:
            players += [Random(value)]
            i += 1

    game = Game(players, end_early=args.end_early)
    game.play_game()


if __name__ == '__main__':
    main()
