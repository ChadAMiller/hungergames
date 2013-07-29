import unittest
from bots import *
from Player import BasePlayer
from Game import Game

# Unit tests to safeguard against rebreaking things.
# If you don't know what this is, ignore it.

class FakePlayer(BasePlayer):
    '''Dummy class that just hunts and records what happens to it'''
    def __init__(self):
        self.food = 0
        self.rep = 0
        
    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations
                    ):
        self.food = current_food
        self.rep = current_reputation
        
        self.hunt_choices_args =    (
                                    round_number,
                                    current_food,
                                    current_reputation,
                                    m,
                                    player_reputations,
                                    )
        
        return ['h']*len(player_reputations)
        
                    
    def hunt_outcomes(self, food_earnings):
        self.food += sum(food_earnings)
        self.hunt_outcomes_args = (food_earnings,)
        
    def round_end(self, award, m, number_hunters):
        self.food += award
        self.round_end_args = (award, m, number_hunters,)
        
        
        
class TestPlayer(unittest.TestCase):
    def test_tester(self):
        import tester
        tester.run_tests('Player.py')       


class TestFreeloaderBot(unittest.TestCase):
    def setUp(self):
        self.bot = Freeloader()
        
    def test_hunt_choices(self):
        self.assertEqual(['s', 's', 's'],
            self.bot.hunt_choices(1, 1200, 0, 3, [0,0,0]))
            
            

class TestAlternatorBot(unittest.TestCase):
    def setUp(self):
        self.bot = Alternator()
    
    def test_hunt_choices(self):
        self.assertEqual(['h', 's', 'h'],
            self.bot.hunt_choices(1, 1200, 0, 3, [0,0,0]))
            
        

class TestPushoverBot(unittest.TestCase):
    def setUp(self):
        self.bot = Pushover()
        
    def test_hunt_choices(self):
        self.assertEqual(['h', 'h', 'h'],
            self.bot.hunt_choices(1, 1200, 0, 3, [0,0,0]))
            
            

class TestBasePlayer(unittest.TestCase):
    def setUp(self):
        self.bot = BasePlayer()
        
    def test_hunt_choices(self):
        self.assertRaises(
            NotImplementedError,
            self.bot.hunt_choices,
            (1, 1200, 0, 3, [0,0,0]),
            )
        
    def test_hunt_outcomes(self):
        self.assertIsNone(self.bot.hunt_outcomes([-2, 1, 0]))
        
    def test_round_end(self):
        self.assertIsNone(self.bot.round_end(120, 12, 12))
        
        

class TestTwoPlayer(unittest.TestCase):
    def setUp(self):
        self.players = [FakePlayer(), FakePlayer()]
        self.game = Game(self.players, verbose=False)
        
        
    def test_two_turns(self):
        # Starting conditions in game engine
        self.assertEqual(self.game.players[0].food, 300)
        self.assertEqual(self.game.players[1].rep, 0.0)
        
        # Make sure data sent to player classes is right
        # Note that after this point, self.players[0] is not
        # necessarily self.game.players[0] because of shuffling
        self.game.play_round()
        self.assertEqual(self.players[0].food, 302)
        self.assertEqual(self.players[0].rep, 0)
        
        self.game.play_round()
        self.assertEqual(self.players[0].food, 304)
        self.assertEqual(self.players[0].rep, 1.0)
        
        # Test that Game is sending the correct arguments to BasePlayers       
        self.assertEqual(self.players[0].hunt_choices_args,
                        (2, 302, 1.0, 1, [1.0]))
        
        self.assertEqual(self.players[0].hunt_outcomes_args, ([0],))
        self.assertEqual(self.players[0].round_end_args, (2, 1, 2))
        
        # Test that Game stayed synched with Player.
        self.assertEqual(self.players[0].food, self.game.players[0].food)
        self.assertEqual(self.players[0].rep, self.game.players[0].rep)
        
    def test_full_game(self):
        #Make sure the game runs to completion without errors
        self.game.play_game()
        
        
    def test_m(self):
        self.assertEqual(self.game.calculate_m(), 1)
        self.assertEqual(self.game.m_bonus, 2)
        

if __name__ == '__main__':
    unittest.main()
    