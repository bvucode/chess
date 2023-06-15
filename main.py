
print("\x1b[2J", end = "")
while True:
    print('\x1b[H', end='')
    print("\n")
    print("\nchess with computer\n")
    board = [[" ", "a", "b", "c", "d", "e", "f", "g", "h", " "],
         ["8", "R", "N", "B", "Q", "K", "B", "N", "R", "8"],
         ["7", "p", "p", "p", "p", "p", "p", "p", "p", "7"],
         ["6", "x", "x", "x", "x", "x", "x", "x", "x", "6"],
         ["5", "x", "x", "x", "x", "x", "x", "x", "x", "5"],
         ["4", "x", "x", "x", "x", "x", "x", "x", "x", "4"],
         ["3", "x", "x", "x", "x", "x", "x", "x", "x", "3"],
         ["2", "p", "p", "p", "p", "p", "p", "p", "p", "2"],
         ["1", "R", "N", "B", "Q", "K", "B", "N", "R", "1"],
         [" ", "a", "b", "c", "d", "e", "f", "g", "h", " "]]
    for i in board:
        print(" ".join(i))
    print("\n")
    step = input("It's your move. Type row and column like e3. ")
    for i in board[0]:
        if step[0] in i:
            pass
                
    print('\x1b[H', end='')
        
