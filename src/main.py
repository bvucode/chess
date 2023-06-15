from src.chessengine import ChessEngine
print("\x1b[2J", end = "")
flag = 0
while True:
    print('\x1b[H', end='')
    print("\nChess\n")
    while flag == 0:
        ce = ChessEngine()
        cel = ce.load()
        for i in cel:
            print(" ".join(i))
        flag = 1
        print('\x1b[H', end='')
    else:
        choose = input("It's your move. Type like e2. ")
        step = input("Move to. Type like e3. ")
        ceu = ce.upload(choose, step)
        for i in ceu:
            print(" ".join(i))
        print('\x1b[H', end='')
        
