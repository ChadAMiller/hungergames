# Hunger Games Test Program

This is an implementation of a test engine for [Brilliant.org's Hunger Games Competition](http://brilliant.org/competitions/hunger-games/).

This is an OOP solution where player classes are expected to inherit from a base `Player` class. The `Game` class only expects the methods required by the competition (`hunt_choices`, `hunt_outcomes`, `round_end`).

I included the three sample players from the sample code, under the names `Pushover`, `Freeloader`, and `Alternator`.

## Usage

*    `python app.py` runs a sample game with exactly one of each test character. It's 3 lines of code and pretty easy to generalize to whatever custom players you might make up

*    If you want to step through rounds one at a time rather than run the whole game in one shot, you can use `Game.play_round()` instead of `Game.play_game()`. You can also complete the game at any time using `play_game` even after stepping through the first few rounds.

*    My players inherit from `Player`, though it should also be fine to insantiate `Player` and then attach functions to it.

*    Currently games default to 300 rounds minimum and 1000 rounds on average. These numbers came straight from my butt. You can easily change them in `Game.py` if you have better ones.

## Official Test Script/Solution

My `Player` class fails [the official test script](https://gist.github.com/brilliant-problems/970beec35da3a7a14e16) because it expects `Player` to be the solution, and not some base class that the solution is inheriting from. This is easily fixed by just copying any valid `hunt_choices` function over the one that's already in my Player base class (I actually ran it this way to make sure). I'm not going to "fix" it because I'd rather catch errors when a test strategy isn't written properly.

As far as I know, the following steps should produce something you can submit to the contest:

*    Copy/paste the `Player` class from `Players.py`
*    Replace any functions within that class with the equivalent functions from whatever specific strategy you came up with

For the record, I don't mind if anyone does this and I wouldn't consider it cheating. I'm deliberately keeping any strategy info out of this repo until after the contest.

## Known Issues

*    `Game` needs to be rewritten until it doesn't embarrass me. In all seriousness, I tried to emulate the expected environment by saving food and reputation in the `Game` instead of in the `Players` and it made a lot of my code gross and awkward. I might change it.
