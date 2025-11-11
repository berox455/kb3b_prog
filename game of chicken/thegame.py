import random
import matplotlib.pyplot as plt

V = 2    # Hodnota výhry
C = 4   # Cena za souboj jestřábů

class Agent:
    def __init__(self, strategy):
        self.strategy = strategy
        self.history_moves = []  # Moje celková historie
        self.history_opponents = {}  # Oponent -> tahy oponenta
        self.history_interactions = {}   # Oponent -> moje tahy

    def decide(self, opponent_id):
        return self.strategy(
            self.history_moves,
            self.history_interactions.get(opponent_id, []),
            self.history_opponents.get(opponent_id, [])
        )

    def update_history(self, opponent_id, own_move, opponent_move):
        self.history_moves.append(own_move)
        if opponent_id not in self.history_opponents:
            self.history_opponents[opponent_id] = []
            self.history_interactions[opponent_id] = []
        self.history_opponents[opponent_id].append(opponent_move)
        self.history_interactions[opponent_id].append(own_move)


class Population:
    def __init__(self, strategies):
        s_number = 20 # počet agentů ze strategií
        self.agents = [Agent(strategy) for strategy in strategies for _ in range(s_number)]

    def play_game(self, agent1, agent2):
        move1 = agent1.decide(id(agent2))
        move2 = agent2.decide(id(agent1))
        agent1.update_history(id(agent2), move1, move2)
        agent2.update_history(id(agent1), move2, move1)

        if move1 == "H" and move2 == "H":
            return (V-C)/2, (V-C)/2  # Souboj
        elif move1 == "H" and move2 == "D":
            return V, 0  # H vyhraje, D nemá nic
        elif move1 == "D" and move2 == "H":
            return 0, V  # H vyhraje, D nemá nic
        elif move1 == "D" and move2 == "D":
            return V/2, V/2  # D sdílí zdroj

    def tournament(self):
        scores = {agent: 0 for agent in self.agents}

        for _ in range(len(self.agents)*10):  # iterace v rámci turnaje
            agent1, agent2 = random.sample(self.agents, 2)
            score1, score2 = self.play_game(agent1, agent2)
            scores[agent1] += score1
            scores[agent2] += score2

        # Selekce: půlka zemře, přeživší se zdvojnásobí
        sorted_agents = sorted(self.agents, key=lambda a: scores[a], reverse=True)
        self.agents = sorted_agents[:len(self.agents)//2] * 2

    def run_evolution(self, generations=20):
        history = []
        for _ in range(generations):
            population_count = {strategy: sum(1 for a in self.agents if a.strategy == strategies[strategy]) for strategy in strategies}
            history.append(population_count)
            self.tournament()
        self.print_population_counts(history[-1])
        return history

    def print_population_counts(self, population_count):
        print("Finální rozložení strategií:")
        for strategy, count in population_count.items():
            print(f"{strategy}: {count}")
        print("-----------------")


def jestrab(cela_historie, moje_tahy, oponent_tahy):
  # cela_historie: pole veškerých strategií, které hráč provedl
  # moje_tahy: moje tahy při předešlých soubojích s tímto hráčem
  # oponent_tahy: tahy oponenta při předešlých soubojích se mnou
    return "H"

def holubice(cela_historie, moje_tahy, oponent_tahy):
    return "D"


# todo: sem vlož funkce
def chicken(cela_historie, moje_tahy, oponent_tahy):
  if 1 == 1:
      return "D"

def crow(whole_history, my_moves, oponent_moves):
    if len(oponent_moves) == 0 or len(my_moves) == 0:
      return "D"

    opponent_d = 0
    opponent_h = 0

    for i in oponent_moves:
        if i == "D":
            opponent_d += 1
        else:
            opponent_h += 1

    my_d = 0
    my_h = 0

    for i in my_moves:
        if i == "D":
            my_d += 1
        else:
            my_h += 1

    diff_d = opponent_d - my_d
    diff_h = opponent_h - my_h

    if diff_h > diff_d:
        if opponent_d > my_d:
            return "H"
        else:
            return "D"
    else:
        if opponent_h > my_h:
            return "D"
        else:
            return "H"

def heryho_chicken(cela_historie, moje_tahy, oponent_tahy):
    oponent_H = 0
    oponent_D = 0
    for i in range(len(oponent_tahy)-1):
        if i == "H":
            oponent_H += 1
        elif i == "D":
            oponent_D += 1

    if oponent_D > oponent_H:
        hodnej = True
        for i in oponent_tahy[-3:]:
            if i != "D":
                hodnej = False

        if hodnej == True:
            return "D"
    elif oponent_D < oponent_H:
        return "H"

    if len(oponent_tahy) == 0:
        return "H"
    return "H"

def penkava(cela_historie, moje_tahy, oponent_tahy):
    hacka = 0
    decka = 0

    if len(cela_historie) == 0:
        return "D"
    else:
        for i in cela_historie:
            if i == "H":
                hacka += 1
            else:
                decka += 1

        if hacka > decka:
            return "H"
        elif decka >= hacka:
            return "D"
        else:
            return "D"
        
def pomer_jan(tahy):
    celkove_h = 0
    celkove_d = 1
    for i in tahy:
        if i == "D":
            celkove_d += 1
        elif i == "H":
            celkove_h += 1
    pomer = celkove_h / celkove_d
    if pomer > 1.5:
        return "H"
    elif pomer < 0.5:
        return "D"
    else:
        return "D"


def jan(cela_historie, moje_tahy, oponent_tahy):
    if not moje_tahy:
        return "D"
    else:
        pomer = pomer_jan(oponent_tahy)
        if pomer == "D":
            return "D"
        if pomer == "H":
            return pomer_jan(cela_historie)
        else:
            return "H"


def dodo(cela_historie, moje_tahy,oponent_tahy):
    if len(cela_historie) == 0 or len(moje_tahy) == 0:
        return "H"
    if oponent_tahy[-1] == "H":
        return "H"
    elif moje_tahy[-1] == "D":
        return "D"
    return "H"


def konipas_horsky(cela_historie, moje_tahy, oponent_tahy):
    if(len(cela_historie) > 3 and len(cela_historie) < 7):
        return "H"
    return "D"


#beta kiwi
#def scarecrow(cela_hisrorie, moje_tahy, opponent_tahy):
#    d = 0
#    h = 0
#    Chance_wheel = []
#
#    if opponent_tahy == []:
#        return "H"
#    elif len(moje_tahy) < 3200:
#        for i in opponent_tahy:
#            if i == "H":
#                h += 1
#            else:
#                d += 1
#
#        if opponent_tahy[0] == "D":
#            if opponent_tahy[-1] == "D":
#                Zlej = 30
#                Hodnej = 35
#            else:
#                Zlej = 15
#                Hodnej = 50
#        elif opponent_tahy[0] == "H":
#            if opponent_tahy[-1] == "H":
#                Zlej = 0
#                Hodnej = 65
#            else:
#                Zlej = 15
#                Hodnej = 50
#        else:
#            Zlej = 0
#            Hodnej = 65
#    
#        
#        if h <= d:
#            Zlej += 35
#        else:
#            Hodnej += 35
#        
#        for x in range(Zlej):
#            Chance_wheel.append("H")
#        for y in range(Hodnej):
#            Chance_wheel.append("D")
#
#        return Chance_wheel[random.randint(0, Hodnej + Zlej - 1)]
#    else:
#        return "D"
#
#
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





# todo: do slovníku přidej funkce
strategies = {"jestrab": jestrab, "holubice": holubice, "kiwi": kiwi, "crow": crow,
              "jan": jan, "dodo": dodo,
              "konipas_horsky": konipas_horsky, "penkava": penkava,
              "heryho_chicken": heryho_chicken,
              "chicken": chicken
              }

population = Population(strategies.values())
history = population.run_evolution()

# Plotování populací:
labels = list(strategies.keys())
generations = list(range(len(history)))
data = {label: [hist.get(label, 0) for hist in history] for label in labels}

plt.figure(figsize=(10, 5))
for label in labels:
    plt.plot(generations, data[label], label=label)
plt.xlabel("Generace")
plt.ylabel("Počet jedinců")
plt.title("Evoluce v Game of chicken")
plt.legend()
plt.show()