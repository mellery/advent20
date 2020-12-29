
#input is clockwise

def cupgame(input,moves, part):
    print(input,"moves",moves, "part",part)
    cups = []
    for i in input:
        cups.append(int(i))

    if part == 2:
        index = max(cups)
        while len(cups) < 1000000:
            index = index+1
            cups.append(index)

    for m in range(0,moves):
        
        if m == 0:
            current = cups[0]
        else:
            nextcup = cups.index(current)+1
            if nextcup > len(cups)-1:
                nextcup = 0
            current = cups[nextcup]
        
        
        #print("-- move:",m+1,"--")
        #print("current cup ", current)

        #print("cups:",cups)
        
        pickup = cups[cups.index(current)+1:cups.index(current)+4]
        while len(pickup) < 3:
            pickup.append(cups[0])
            cups.pop(0)

        for p in pickup:
            if p in cups:
                cups.remove(p)
        
        #print("pickup:",pickup)
        
        destination = current - 1
        while destination not in cups:
            destination = destination - 1
            if destination < min(cups):
                destination = max(cups)
        #print("destination",destination)

        #cups.insert(cups.index(destination)+1,pickup)
        cups[cups.index(destination)+1:cups.index(destination)+1] = pickup

    nextcup = cups.index(current)+1
    if nextcup > len(cups)-1:
        nextcup = 0
    current = cups[nextcup]

    print('\n-- final --') 
    print('current',current)
    print('cups:',cups)

    oneloc = cups.index(1)
    #print(cups[oneloc+1])
    #print(cups[oneloc+2])
    #print(cups[oneloc+1]*cups[oneloc+2])
    #ans = ""
    #for x in range(oneloc+1,len(cups)):
    #    ans = ans + str(cups[x])
    #for x in range(0,oneloc):
    #    ans = ans + str(cups[x])

    #print(ans)

    #1. crab picks up 3 times clockwise of the current cup
    #2. crab selects destination cup with label equal to current cup -1, or -1 till cup found, or wraps around
    #3. crab inserts the cups clockwise of destination cup
    #4. get new current cup


cupgame(list('389125467'), 10, 1)
cupgame(list('389125467'), 100, 1)
cupgame(list('784235916'), 100, 1)

#cupgame(list('389125467'), 10000000, 2)
#cupgame(list('784235916'), 10000000, 2)