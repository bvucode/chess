print("\x1b[2J", end = "")
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
while True:
    print('\x1b[H', end='')
    print("\nChess\n")
    for i in board:
        print(" ".join(i))
    print("\n")
    choose = input("It's your move. Type like e2. ")
    step = input("Move to. Type like e3. ")
    m = ""
    for x, i in enumerate(board[0]):
        if choose[0] == i:
            m = board[int(choose[1])][x]
            board[int(choose[1])][x] = "x" 
    for x, i in enumerate(board[0]):
        if step[0] == i:
            board[int(step[1])][x] = m
    print('\x1b[H', end='')
        
