class Player(object):
    '''Base class so I don't have to repeat bookkeeping stuff'''
    
    def __repr__(self):
        try:
            return self.name
        except AttributeError:
            return NotImplemented
    
    def hunt_choices(*args, **kwargs):
        raise NotImplementedError("You must define a strategy!")
        
    def hunt_outcomes(*args, **kwargs):
        pass
        
    def round_end(*args, **kwargs):
        pass


class Pushover(Player):
    '''Player that always hunts.'''
    def __init__(self):
        self.name = "Pushover"
    
    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        return ['h']*len(player_reputations)

        
class Freeloader(Player):
    '''Player that never hunts.'''
    
    def __init__(self):
        self.name = "Freeloader"
    
    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        return ['s']*len(player_reputations)
        

class Alternator(Player):
    '''Player that alternates between hunting and not.'''
    def __init__(self):
        self.name = "Alternator"
        self.moves = ['s', 'h']
        
    def update_strat(self):
        self.moves.reverse()
        
    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        self.update_strat()
        return [self.moves[0]]*len(player_reputations)
        