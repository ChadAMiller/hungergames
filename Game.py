from __future__ import division, print_function
import random

# I have no idea what these numbers should be yet
MIN_ROUNDS = 300
AVERAGE_ROUNDS = 1000

# Indexes into player list for better readability
PLAYER = 0
FOOD = 1
HUNTS = 2

def payout(*args):
    '''Times 3 because this calculates one person's share'''
    return args.count('h')*3
    
class Game(object):   
    def __init__(self, players, verbose=True):
        self.verbose = verbose
        self.max_rounds = MIN_ROUNDS + int(random.expovariate(1/(AVERAGE_ROUNDS-MIN_ROUNDS)))
        self.round = 0
        self.hunt_opportunities = 0
        
        self.players = players # to set self.P
        food = [300*(self.P-1)]*self.P
        total_hunts = [0]*self.P
        self.players = [[p,f,th] for p,f,th in zip(players,food,total_hunts)]
        
        
    @property
    def m_bonus(self):
        return 2*(self.P-1)
    
    @property
    def P(self):
        return len(self.players)
        
    def calculate_m(self):
        try:
            return random.randrange(1, self.P*(self.P-1))
        except ValueError:
            # m stops existing for 2 players
            return 3
            
        
    def play_round(self):
        # TODO: Refactor this beast
        self.round += 1
        m = self.calculate_m()
        
        random.shuffle(self.players)

        # reputation is total number of times player has hunted / total number of times they were offered the oppurtunity
        reputation_list = list(0 if self.hunt_opportunities == 0 else p[HUNTS]/self.hunt_opportunities for p in self.players)
        
        strategies = []
        for i,p in enumerate(self.players):
            # create a copy of the reputation list without this player in it
            player_reputation_list = reputation_list[:i]+reputation_list[i+1:]

            strategy = p[PLAYER].hunt_choices(self.round, p[FOOD], 
                                0 if self.hunt_opportunities == 0 else p[HUNTS]/self.hunt_opportunities,
                                m, player_reputation_list)

            strategy.insert(i,'s')
            strategies.append(strategy)


        self.hunt_opportunities += self.P-1
        
        results = [[0 for i in range(self.P)] for j in range(self.P)]                        
        
        for i in range(self.P):
            for j in range(i+1, self.P):
                if i != j:
                    results[i][j] = results[j][i] = payout(strategies[i][j], strategies[j][i])
                
        total_hunts = sum(s.count('h') for s in strategies)//2
        bonus = self.m_bonus if total_hunts >= m else 0
        
        for strat, result, player in zip(strategies, results, self.players):
            food = sum(result)
            hunts = strat.count('h')
            
            player[FOOD] += food-4*hunts-2*(self.P-1)+bonus
            
            player[HUNTS] += hunts
            
            player[PLAYER].hunt_outcomes(food)
            player[PLAYER].round_end(bonus, m, total_hunts)
            
            
        if self.verbose:
            print([(name, food, hunts/self.hunt_opportunities) for name, food, hunts in self.players])
                   
        
        if self.game_over():
            raise StopIteration
            
        
    def game_over(self):
        self.players = [p for p in self.players if p[FOOD] > 0]
        return (self.P < 2) or (self.round > self.max_rounds)
        
        
    def play_game(self):
        '''
        Preferred way to run the game to completion
        Written this way so that I can step through rounds one at a time
        '''
        
        while True:
            try:
                self.play_round()
            except StopIteration:
                print(self.players)
                break
        