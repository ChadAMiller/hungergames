# Hunger Games Test Program

This is an implementation of a test engine for [Brilliant.org's Hunger Games Competition](http://brilliant.org/competitions/hunger-games/).

This is an OOP solution where player classes are expected to inherit from a base `Player` class. The `Game` class only expects the methods required by the competition (`hunt_choices`, `hunt_outcomes`, `round_end`).

I included the three sample players from the sample code, under the names `Pushover`, `Freeloader`, and `Alternator`.

There are a couple other sample players implemented in bots.py.  These are `Random`, `MaxRepHunter`, and `FairHunter`.  

The Random player decides to hunt with some probability p and slack with probability 1-p.  You can decide this probability when the player is created.  For a Random player that hunts 50% of the time and slacks 50% of the time you would create the player with Random(0.5).

The MaxRepHunter is a player who only hunts with players who have the current maximum reputation.  A common question in the discussion section was how to beat someone who only slacks (Freeloader).  A pair of MaxRephunter's will beat a group of any size of Freeloaders.  Give it a shot.

The FairHunter is a player who tries to play fair by hunting with probability equal to opponents reputation.  This means he will hunt with hunters and slack with slackers.  He never tries to take advantage of hunters.

## Usage

*    `python app.py` runs a sample game with exactly one of each test bot. It's 3 lines of code and pretty easy to generalize to whatever custom players you might make up.

*    If you want to step through rounds one at a time rather than run the whole game in one shot, you can use `Game.play_round()` instead of `Game.play_game()`. You can also complete the game at any time using `play_game` even after stepping through some rounds.

*    If you're new to Python and just want to test a given solution against the builtin robots, edit `Player.py` and fill your solution in the class at the bottom.

*    You can modify the maximum and average number of rounds using parameters to the `Game` initializer, e.g. `game = Game(players, min_rounds = 1000, average_rounds = 20000)`. An easy way to see the options is `pydoc Game.Game`.

*    All players inherit from `Player.BasePlayer`. If you're going to stay synched with this repo, it's a good idea to keep it that way in case we add features like better pretty-printing.

## Official Solution

The goal is for `Player.py` to be a valid contest submission. To verify against Brilliant's official test script (included in this repo), run `python tester.py Player.py`. If this errors before you've edited anything, I have a bug. Please let me know.

I will deliberately be keeping this repo free of *any* strategic information until after the contest, so that using code from it is not cheating. You may copy/modify whatever you want.

## Bugs

If you find a bug, the fastest way to tell me is by submitting an issue on the [tracker](https://github.com/ChadAMiller/hungergames/issues) (I have email notification turned on). You can also email me (address in my [profile](https://github.com/ChadAMiller)).

## Patches/Pull Requests

Thanks to the many people who've submitted/suggested changes! I've already gotten more help than I expected. I don't expect everybody to read all of the below, but here's where I'm coming from when I evaluate submissions:

*    I tend to code all at once in single sessions, so whatever you want to do, you're probably not duplicating my work. This is especially true if I posted the Issue myself. If you want to do something, go for it.

*    `python tester.py Player.py` must pass at all times.

*    Any instance of `Game.py` must conform to the official rules 100%. Any player-visible difference between `Game.py` and the official rules is a bug.

*    Because `Game.py` is pretending to be the server, it will not "trust" player instances at all. It will store its own state information like reputations and food even if the players are also storing that information.

*    `bots.py` must have no global variables other than class definitions (so that `from bots import *` is safe)

*    Due to interest from people who don't know Python or even programming at all yet, I imagine there will be some people that just want to run simulations and some that want to patch the engine. To accomodate those people, my goal is that this engine be 100% usable by someone who only edits `Player.py`, `app.py`, and perhaps `bots.py`. The other files, particularly `Game.py` should be usable as "black boxes".

*    Toward that end, my comment philsophy is that `Player.py` should be friendly to even people who learned Python yesterday, while `Game.py` will be a lot sparser because I assume contributors know what they're doing and don't want to clutter the code too much. Detailed docstrings are encouraged everywhere.

Thanks again for all your help!

--Chad