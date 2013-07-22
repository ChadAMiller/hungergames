class BasePlayer(object):
    '''
    Base class so I don't have to repeat bookkeeping stuff.
    Do not edit unless you're working on the simulation.
    '''
    
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


class Player(BasePlayer):
    '''
    If you're just trying to test your solution, this is the one to edit.
    '''
    
    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        return ['s']*len(player_reputations)
        
    def hunt_outcomes(self, food_earnings):
        pass
        
    def round_end(self, award, m, number_hunters):
        pass
        