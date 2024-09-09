from src.Models.Cell import Cell


class board:
    def __init__(self,board_size):
        self.board_size=board_size
        self.grid=[[Cell(i,j) for j in board_size] for i in board_size]


    def print_board(self):
        for row in self.grid:
            for cell in row:
                cell.display()
            print()
