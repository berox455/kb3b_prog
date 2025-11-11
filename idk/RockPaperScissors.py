import random



while 1==1:
    player = input("Type [r] for rock, [p] for paper, [s] for scissors: ") [0]

    values = ["r", "p", "s"]

    if player not in values:
        print("Bad input")
    else:
        ai = random.choice(values)
        print("Opponent played", ai)
        if ai == player:
            print("It's a draw!")
        elif (ai == "r" and player == "p") or (ai == "p" and player == "s") or (ai == "s" and player == "r"):
            print("You win!!")
        else:
            print("You lose!!")