class GameController:


    def __init__(self,gameService):
        self.gameService=gameService

    def  start_game(self,size,players,winning_stg):
        #validations
        self.gameService.start_game(size,players,winning_stg)

    def display_board(self,game):
        self.gameService.display_game(game)

    def take_move(self,game):
        self.gameService.take_move(game)

    def undo_move(self,game):
        self.gameService.undo(game)