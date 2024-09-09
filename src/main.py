from src.Models.Bot import Bot
from src.Models.BotDifficulty import BotDifficulty
from src.Models.GameStatus import GameStatus
from src.Models.PlayerType import PlayerType
from src.Models.Symbol import Symbol
from src.Models.players import players
from src.controller.GameController import GameController
from src.helper.stratergy.WinningStrategy.diagonalWS import DiagonalWS
from src.services.GameService import GameService

if __name__=='__main__':
    Gs=GameService()
    gc=GameController(Gs)
    dimension=3
    players=[
        players('karan',1,PlayerType.HUMAN,Symbol('X')),
        Bot(2, 'Rohit', Symbol('Y'),BotDifficulty.EASY)
    ]
    winning=[DiagonalWS()]

    game=gc.start_game(dimension,players,winning)
    #displayBoard
    gc.display_board(game)
    #until game in progress take input
    while game.gameStatus==GameStatus.INPROGRESSED:
        gc.take_move(game)
        gc.display_board(game)
        undo_answer=input('Do You Want to Undo? if Yes,Press 1:')
        if undo_answer=='1':
            print('Undo....')
            gc.undo_move(game)
            gc.display_board(game)
    if game.gameStatus==GameStatus.COMPLETED:
        print(f'Winner:{game.winner}')
    elif game.gameStatus==GameStatus.DRAW:
        print(f'DRAW!')
    #

    #show end msg