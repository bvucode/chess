
class ChessEngine:
    """ класс шахматного движка """
    def __init__(self):
        board = [[" ", "a", "b", "c", "d", "e", "f", "g", "h", " "],
                 ["8", "R1", "N1", "B1", "Q1", "K1", "B1", "N1", "R1", "8"],
                 ["7", "p1", "p1", "p1", "p1", "p1", "p1", "p1", "p1", "7"],
                 ["6", "x", "x", "x", "x", "x", "x", "x", "x", "6"],
                 ["5", "x", "x", "x", "x", "x", "x", "x", "x", "5"],
                 ["4", "x", "x", "x", "x", "x", "x", "x", "x", "4"],
                 ["3", "x", "x", "x", "x", "x", "x", "x", "x", "3"],
                 ["2", "p2", "p2", "p2", "p2", "p2", "p2", "p2", "p2", "2"],
                 ["1", "R2", "N2", "B2", "Q2", "K2", "B2", "N2", "R2", "1"],
                 [" ", "a", "b", "c", "d", "e", "f", "g", "h", " "]]
        self.board = board
    def load(self):
        return self.board

    def upload(self, choose, step):
        self.choose = choose
        self.step = step
        m = ""
        for x, i in enumerate(self.board[0]):
            if choose[0] == i:
                if self.board[int(choose[1])][x].endswith("1"):
                    m = self.board[int(choose[1])][x]
                    self.board[int(choose[1])][x] = "x" 
        for x, i in enumerate(self.board[0]):
            if step[0] == i:
                self.board[int(step[1])][x] = m
        return self.board
