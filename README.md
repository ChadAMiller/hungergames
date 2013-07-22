# Hunger Games Test Program

EDIT 07/21: Hi, many new people! For those editing the repo: (1) Thank you and (2) I've added a notice at the end explaining where I plan to take this thing this week.

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

## Future Plans/Philosophy (for pull requests)

This repo is getting a lot more attention (and patches) than I expected. This is a great thing and I appreciate all your help, but it also made me realize that I need to make up my mind on some stuff so that we're all on the same page.

I've noticed a lot of people on Brilliant's forums want to learn Python just for this contest, many of them teenagers. I think this is really cool, and that it would be pretty easy to make this repo friendly to those people. Toward that end, I've decided:

*    The overall goal is that a player who just wants to enter the competition can edit one file and *only* one file if they're only interested in the competition and not the simulation engine itself. That might not be realistic in my/our spare time given the deadline, but I think we can at least leave `Game.py` for the people who are comfortable enough to contribute to the engine itself. ([Jake Nielsen](https://github.com/jknielse/hungergames-1) overhauled this class and I haven't looked closely at his changes yet. Depending on what happens, I'll probably make MIN_ROUNDS and AVERAGE_ROUNDS into `__init__` parameters instead of module-level globals. They'll still default to their current values to avoid breaking any calling code.)

*    The `Player` class will have a different name within the next couple days. I haven't decided what that will be, though the best I've come up with is `BasePlayer`. If you have a preference, see Issue #6 in this repo.

*    I will likely move the sample AI players into a file called `Bots.py` (which will in turn import the necessary base class). `Players.py` may get renamed to `Player.py` to make the new structure clearer. Whatever that file is called, it will contain the base player class that the other players inherit from, as well as a bare `Player` class that gives the minimum implementation required to pass the `tester.py` script from Brilliant.

*    The above two bullets mean that the final state of `Player.py` should be the final state of a contest submission, so I can get rid of those convoluted instructions above.

*    Any `Player`-visible difference between this repo and the eventual competition, no matter how minor, is a bug. I hope to have the last of these gone tomorrow barring any misunderstanding of the rules.

*    Since I mentioned I wasn't sure about this in the past: `Game` and all other classes will continue to store no instance information in player classes, instead tracking food and reputation information on its own. Any state within a player object should be created and tracked by that player's own code, and no other object should read or depend on it in any way.

*    Once the above is in place, I'll probably put some beginner-friendly documentation in the relevant files.

I hope to have all the concrete changes above implemented within the week. In the meantime, thanks again to everyone that's contributed so far, and any future contributors.

--Chad