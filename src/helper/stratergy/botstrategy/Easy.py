from src.Models.CellStatus import CellStatus
from src.helper.stratergy.botstrategy.BotStrategy import BotStrategy


class Easy(BotStrategy):

    def decide_move(self, board: object) -> object:
        print('THis is', board)
        for row in board.grid:
            for cell in row:
                if cell.status == CellStatus.EMPTY:
                    return cell
        return None
