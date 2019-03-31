## carlyA

import random

class rps():
    ### initializing function ###
    def __init__(self):
        return

    def shoot(self, last_round):
        options = ['R', 'P', 'S']
        if last_round == 'R':
            return('P')
        elif last_round == 'P':
            return('S')
        elif last_round == 'S':
            return('R')
        else:
            return(random.choice(options))
