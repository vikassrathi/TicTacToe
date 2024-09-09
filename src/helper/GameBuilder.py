from src.CustomExceptions.InvalidPlayerException import InvalidPlayerException



class GameBuilder:
    def __init__(self):
        self.dimension=None
        self.players=None
        self.winning_strategies=None

    def set_dimension(self,dimension):
        self.dimension=dimension
        return self

    def set_players(self,players):
        self.players=players
        return self

    def set_winning_strategies(self,winning_strategies):
        self.winning_strategies=winning_strategies
        return self
    def validate(self):
        if len(self.players)>self.dimension-1:
            raise InvalidPlayerException
    def build(self):
        self.validate()
        from src.Models.Game import Game
        return Game(self.dimension,self.players,self.winning_strategies)