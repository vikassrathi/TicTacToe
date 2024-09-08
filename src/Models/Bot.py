from players import players
from PlayerType import PlayerType
class Bot(players):
    def __init__(self,player_id,name,symbol,difficulty):
        super.__init__(name,player_id,PlayerType.BOT,symbol)
        self.difficulty=difficulty

