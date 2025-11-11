def kiwi(hist, my_moves, opp_moves):
    d = 0
    h = 0
    
    if opp_moves == []:
        return "H"
    elif len(my_moves) < 3200:
        for i in opp_moves:
            if i == "H":
                h += 1
            else:
                d += 1

        if opp_moves[0] == "D":
            if opp_moves[-1] == "D":
                Zlej = 30
                Hodnej = 35
            else:
                Zlej = 15
                Hodnej = 50
        elif opp_moves[0] == "H":
            if opp_moves[-1] == "H":
                Zlej = 0
                Hodnej = 65
            else:
                Zlej = 15
                Hodnej = 50
        else:
            Zlej = 0
            Hodnej = 65
    
        if h <= d:
            Zlej += 35
        else:
            Hodnej += 35
        
        if Zlej > Hodnej:
            return "H"
        else:
            return "D"
    else:
        return "D"
