from src.Models.Bot import Bot
from src.Models.BotDifficulty import BotDifficulty
from src.Models.PlayerType import PlayerType
from src.Models.Symbol import Symbol
from src.Models.players import players
from src.controller.GameController import GameController

if __name__=='__main__':
    gc=GameController()
    dimension=3
    players=[
        players('karan',1,PlayerType.HUMAN,Symbol('X')),
        Bot('Rohit', 1, PlayerType.BOT, Symbol('Y'),BotDifficulty.Easy)
    ]
    winning=[]

    gc.start_game(dimension,players,winning)
