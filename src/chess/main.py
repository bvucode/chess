from move import Move

print("\nChess\n")
flag = 0
ce = Move()
cel = ce.load()
for i in cel:
    print(" ".join(i))
while True:
    chnst = input("\nIt's your move. Type like e2 e3. ")
    print("\n")
    choose, step = chnst.split(" ")
    ceu = ce.upload(choose, step)
    for i in ceu:
        print(" ".join(i))
        
