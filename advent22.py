filename = "input22.txt"
#filename = "input22_ex1.txt"
filename = "input22_ex2.txt"

file1 = open(filename, 'r') 
lines = file1.readlines() 

p1deck = []
p2deck = []

p1found = False
p2found = False

games = []

def calc_score(deck):
    size = len(deck)
    score = 0
    for c in deck:
        score = score + c*size
        size = size - 1
    return score

def play_round(d1,d2):
    #print('P1 deck',d1)
    #print('P2 deck',d2)
    #print('P1 plays',d1[0])
    #print('P2 plays',d2[0])

    if d1[0] > d2[0]:
        #print("P1 wins")
        d1.append(d1[0])
        d1.append(d2[0])
        d1.pop(0)
        d2.pop(0)

    elif d2[0] > d1[0]:
        #print("P2 wins")
        d2.append(d2[0])
        d2.append(d1[0])
        d1.pop(0)
        d2.pop(0)

    result = (calc_score(p1deck),calc_score(p2deck))
    if result not in games:
        games.append(result)
    else:
        print("stop!")
        return False, d1.copy(), d2.copy()

    print("P1",result[0])
    print("P2",result[1])
    return True, d1.copy(), d2.copy()

for l in lines:
    temp = l.strip()
    #print(temp)
    if temp == '\n':
        continue
    elif 'Player 1' in temp:
        p1found = True
    elif p1found == True and p2found == False:
        
        if 'Player 2' in temp:
            p2found = True
        elif temp.isdigit():
            p1deck.append(int(temp))  

    elif temp.isdigit():
        #print(l)
        p2deck.append(int(temp))

round = 0
run = True
while len(p1deck) > 0 and len(p2deck) > 0 and run == True:

    round = round + 1
    #print("\n---Round",round,"---")
    run, p1deck, p2deck = play_round(p1deck.copy(),p2deck.copy())


print("--Post game results")
print("P1",p1deck)
print("P2",p2deck)

print("P1",calc_score(p1deck))
print("P2",calc_score(p2deck))