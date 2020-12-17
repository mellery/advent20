import copy 

#filename = "input17_ex1.txt"
filename = "input17.txt"

file1 = open(filename, 'r') 
lines = file1.readlines() 

#room = []
world = {}

def get_active(world):
    active = 0
    
    for w,v in world.items():
        if v == '#':
            active = active + 1
    
    return active


def expand_world(world):
    state = copy.deepcopy(world)
    for w, v in world.items():
        x = w[0]
        y = w[1]
        z = w[2]
        for zi in [z-1,z,z+1]:
            for yi in [y-1,y,y+1]:
                for xi in [x-1,x,x+1]:
                    if (xi,yi,zi) not in state:
                        #print("adding",xi,yi,zi)
                        state[(xi,yi,zi)] = '.'
    world = copy.deepcopy(state)
    return world

def update_world(world):
    state = copy.deepcopy(world)
    changed = False

    for w, v in world.items():
        cur = world[w]
        adj = get_adj(world,w)
        #print(w,cur,"adj",adj)
        if cur == '#' and (adj == 2 or adj == 3):
            cur == '#'
        elif cur == '#':
            cur = '.'
            changed = True
        elif cur == '.' and adj == 3:
            cur = '#'
            changed = True
        state[w] = cur

        

        
    world = copy.deepcopy(state)
    return world, changed

def print_world(world):
    #get levels
    levels = []
    rows = []
    cols = []
    for w in world:
        if w[0] not in rows:
            rows.append(w[0])
        if w[1] not in cols:
            cols.append(w[1])
        if w[2] not in levels:
            levels.append(w[2])
    levels.sort()
    rows.sort()
    cols.sort()

    print(levels,rows,cols)

    active = 0

    for z in levels:
        print("\nz =",z)
        #for y in range(0,3):
        for y in cols:
            temp = ""
            #for x in range(0,3):
            for x in rows:
                if (x,y,z) in world:
                    temp = temp + world[(x,y,z)]
                    if world[(x,y,z)] == '#':
                        active = active + 1
            print(temp)
    #print("active =",active)

def get_adj(world, w):
    x = w[0]
    y = w[1]
    z = w[2]
        
    adj = 0
    for zi in [z-1,z,z+1]:
        for yi in [y-1,y,y+1]:
            for xi in [x-1,x,x+1]:
                if (xi,yi,zi) != (x,y,z):
                    if (xi,yi,zi) in world and world[(xi,yi,zi)] == '#':
                        adj = adj + 1
                       
    return adj

y = 0
for l in lines:
    z = 0
    temp = list(l.strip())
    print(list(temp))
    x = 0
    for t in temp:
        world[(x,y,z)] = t
        x = x + 1
    y = y + 1
    

print("initial_state")
print_world(world)

for cycles in range(0,6):

    world = expand_world(world)
    world, changed = update_world(world)
    print("cycle:",cycles+1)
    #print_world(world)
    print("active =",get_active(world))

