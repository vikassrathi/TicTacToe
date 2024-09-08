from board import board
from src.Models.GameStatus import GameStatus


class Game:
    def __init__(self,dimension,players,winning_strategies):
        self.players=players
        self.winning_strategies=winning_strategies
        self.board=board(dimension)
        self.moves=[]
        self.next_turn=0
        self.winner=None
        self.gameStatus=GameStatus.INPROGRESSED
