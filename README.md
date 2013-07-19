# Hunger Games Test Program

This is an implementation of a test engine for [Brilliant.org's Hunger Games Competition](http://brilliant.org/competitions/hunger-games/).

I set it up so that player classes are expected to inherit from `Player`. It's also quite possible to make instances of `Player` and add functions to it. The Game class only expects the methods required by the competition (`hunt_choices`, `hunt_outcomes`, `round_end`).

I included the three sample players from the sample code, under the names `Pushover`, `Freeloader`, and `Alternator`.

## Usage

*    `python app.py` runs a sample game with exactly one of each test character. It's 3 lines of code and pretty easy to generalize to whatever custom players you might make up

*    If you want to step through rounds one at a time rather than run the whole game in one shot, you can use `Game.play_round()` instead of `Game.play_game()`. You can also complete the game at any time using `play_game` even after stepping through the first few rounds.

*    My players inherit from `Player`, though it should also be fine to insantiate player and then attach functions to it.

*    Currently games default to 300 rounds minimum and 1000 rounds on average. These numbers came straight from my butt. You can easily change them in `Game.py` if you have better ones.

## Known Issues

*    `Game` needs to be rewritten until it doesn't embarrass me. In all seriousness, I tried to emulate the expected environment by saving food and reputation in the `Game` instead of in the `Players` and it made a lot of my code gross and awkward. I might change it.

*    `Game` doesn't check for negative food mid-round, so that a player with 1 food can still choose 100% hunts before dying. I'm not 100% certain whether this is allowed by the rules or not

*    My `Player` class fails [the official test script](https://gist.github.com/brilliant-problems/970beec35da3a7a14e16) because of my subclassing solution. I haven't decided whether I care or not.