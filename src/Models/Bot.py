from src.Models.PlayerType import PlayerType
from src.Models.players import players
from src.helper.stratergy.BotFactory import BotFactory


class Bot(players):
    def __init__(self,player_id,name,symbol,difficulty):
        super().__init__(name,player_id,PlayerType.BOT,symbol)
        self.difficulty=difficulty
        self.strategy=BotFactory.getBot(self.difficulty)

    def decide_cell(self,board):
        return self.strategy.decide_move(board)
