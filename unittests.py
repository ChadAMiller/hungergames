import unittest
from bots import *
from Player import BasePlayer

# Unit tests to safeguard against rebreaking things.
# If you don't know what this is, ignore it.

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
        self.assertIsNone(self.bot.round_end(120, 12, 12), None)


if __name__ == '__main__':
    unittest.main()
    