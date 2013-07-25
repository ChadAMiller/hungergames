# Hunger Games Test Program

This is an implementation of a test engine for [Brilliant.org's Hunger Games Competition](http://brilliant.org/competitions/hunger-games/).

This is an OOP solution where player classes are expected to inherit from a base `Player` class. The `Game` class only expects the methods required by the competition (`hunt_choices`, `hunt_outcomes`, `round_end`).

`bots.py` includes the three sample players from the sample code, under the names `Pushover`, `Freeloader`, and `Alternator`. It also contains some user-submitted strategies.

## Usage

*    First, try `python unittest.py`. You will see some test output. If the last line says anything except `OK`, there is a bug. Please let me know (see "Bugs", below).

*    `python app.py` runs a sample game with exactly one of each test bot. It's 3 lines of code and pretty easy to generalize to whatever custom players you might make up.

*    If you want to step through rounds one at a time rather than run the whole game in one shot, you can use `Game.play_round()` instead of `Game.play_game()`. You can also complete the game at any time using `play_game` even after stepping through some rounds.

*    If you're new to Python and just want to test a given solution against the builtin robots, edit `Player.py` and fill your solution in the class at the bottom.

*    You can modify the maximum and average number of rounds using parameters to the `Game` initializer, e.g. `game = Game(players, min_rounds=1000, average_rounds=20000)`. An easy way to see the options is `pydoc Game.Game`, or by entering the shell with `python` and typing `from Game import Game; help(Game)`.

*    All players inherit from `Player.BasePlayer`.

## Official Solution

The goal is for `Player.py` to be a valid contest submission. To verify against Brilliant's official test script (included in this repo), run `python tester.py Player.py` or `python unittest.py`.

I will deliberately be keeping this repo free of *any* strategic information until after the contest, so that using code from it is not cheating. You may copy/modify/submit whatever you want.

## Bugs

If you find a bug, the fastest way to tell me is by submitting an issue on the [tracker](https://github.com/ChadAMiller/hungergames/issues) (I have email notification turned on). You can also email me (address in my [profile](https://github.com/ChadAMiller)).

## Patches/Pull Requests

Thanks to the many people who've submitted/suggested changes! I've already gotten more help than I expected. I don't expect everybody to read all of the below, but here's where I'm coming from when I evaluate submissions:

*    I tend to code all at once in single sessions, so whatever you want to do, you're probably not duplicating my work. This is especially true if I posted the Issue myself. If you want to do something, go for it.

*    `python unittest.py` must pass at all times. If your code is failing tests but you believe there is an error in the test, post a comment with your pull request or open an Issue (even if you know how to fix it; I want to know if my understanding of the game is wrong).

*    Any instance of `Game.py` must conform to the official rules 100%. Any player-visible difference between `Game.py` and the official rules is a bug.

*    Because `Game.py` is pretending to be the server, it will not "trust" player instances at all. It will store its own state information like reputations and food even if the players are also storing that information.

*    `bots.py` must have no global variables other than class definitions (so that `from bots import *` is safe)

*    Due to interest from people who don't know Python or even programming at all yet, I imagine there will be some people that just want to run simulations and some that want to patch the engine. To accomodate those people, my goal is that this engine be 100% usable by someone who only edits `Player.py`, `app.py`, and perhaps `bots.py`. The other files, particularly `Game.py` should be usable as "black boxes".

*    Toward that end, my comment philsophy is that `Player.py` should be friendly to even people who learned Python yesterday, while `Game.py` will be a lot sparser because I assume contributors know what they're doing and don't want to clutter the code too much. Detailed docstrings are encouraged everywhere.

Thanks again for all your help!

--Chad