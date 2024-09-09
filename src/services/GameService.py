from src.Models.Game import Game


class GameService:

    def start_game(self,size,players,winning_stg):
        game=Game.gameBuilder().set_players().set_dimension().set_winning_strategies().build()

    def display_game(self,game):
        game.Board.print_board()

    def take_move(self,game):
        current_player=game.players