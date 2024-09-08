from CellStatus import CellStatus
class Cell:
    def __init__(self,row,column):
        self.row=row
        self.column=column
        self.status=CellStatus.EMPTY
        self.player=None
