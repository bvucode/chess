
class Move:
    """ класс хода фигур """
    def __init__(self):
        board = [[" ", "a", "b", "c", "d", "e", "f", "g", "h", " "],
                 ["8", "WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR", "8"],
                 ["7", "wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp", "7"],
                 ["6", "xx", "xx", "xx", "xx", "xx", "xx", "xx", "xx", "6"],
                 ["5", "xx", "xx", "xx", "xx", "xx", "xx", "xx", "xx", "5"],
                 ["4", "xx", "xx", "xx", "xx", "xx", "xx", "xx", "xx", "4"],
                 ["3", "xx", "xx", "xx", "xx", "xx", "xx", "xx", "xx", "3"],
                 ["2", "bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp", "2"],
                 ["1", "BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR", "1"],
                 [" ", "a", "b", "c", "d", "e", "f", "g", "h", " "]]
        self.board = board
    def load(self):
        """ метод возвращает доску """
        return self.board

    def upload(self, choose, step):
        """ метод движения фигур """
        self.choose = choose
        self.step = step
        m = ""
        for x, i in enumerate(self.board[0]):
            if choose[0] == i:
                if self.board[int(choose[1])][x].lower().startswith("w"):
                    m = self.board[int(choose[1])][x]
                    self.board[int(choose[1])][x] = "xx" 
        for x, i in enumerate(self.board[0]):
            if step[0] == i:
                self.board[int(step[1])][x] = m
        return self.board
