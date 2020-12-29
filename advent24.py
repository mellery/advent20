import copy
#1 = black
#0 = white (default)

#filename = "input24.txt"
filename = "input24_ex1.txt"

file1 = open(filename, 'r') 
lines = file1.readlines() 


directions = ['e', 'se', 'sw', 'w', 'nw', 'ne']
floor_map = {}

def expand_floor(floor_map):
    new_floor = copy.deepcopy(floor_map)
    for k,v in floor_map.items():
        
        cur_x = k[0]
        cur_y = k[1]

        if (cur_x+1,cur_y) not in floor_map:
            new_floor[(cur_x+1,cur_y)] = 0
        
        if (cur_x+0.5,cur_y+1) not in floor_map:
            new_floor[(cur_x+0.5,cur_y+1)] = 0

        if (cur_x-0.5,cur_y+1) not in floor_map:
            new_floor[(cur_x-0.5,cur_y+1)] = 0
        
        if (cur_x-1,cur_y) not in floor_map:
            new_floor[(cur_x-1,cur_y)] = 0
        
        if (cur_x-0.5,cur_y-1) not in floor_map:
            new_floor[(cur_x-0.5,cur_y-1)] = 0
        
        if (cur_x+0.5,cur_y-1) not in floor_map:
            new_floor[(cur_x+0.5,cur_y-1)] = 0

    return new_floor


def get_adj_black(pos):
    black = 0

    cur_x = pos[0]
    cur_y = pos[1]

    if floor_map[(cur_x+1,cur_y)] == 1:
        black += 1

    if floor_map[(cur_x+0.5,cur_y+1)] == 1:
        black += 1

    if floor_map[(cur_x-0.5,cur_y+1)] == 1:
        black += 1
    
    if floor_map[(cur_x-1,cur_y)] == 1:
        black += 1
        
    if floor_map[(cur_x-0.5,cur_y-1)] == 1:
        black += 1

    if floor_map[(cur_x+0.5,cur_y-1)] == 1:
        black += 1

    return black

def split_instructions(line):
    instructions = []
    while len(line) > 0:
        for d in directions:
            if line.startswith(d):
                instructions.append(d)
                line = line.replace(d,'',1)
    
    return instructions

def get_last_tile(path):
    cur_x = 0
    cur_y = 0
    #print("start at",(cur_x,cur_y))
    for p in path:
        if p == 'e':
            cur_x += 1

        elif p == 'se':
            cur_y += 1
            cur_x += 0.5
            
        elif p == 'sw':
            cur_y += 1
            cur_x -= 0.5
            
        elif p == 'w':
            cur_x -= 1

        elif p == 'nw':
            cur_y -= 1
            cur_x -= 0.5
            
        elif p == 'ne':
            cur_y -= 1
            cur_x += 0.5

        #print("now at",(cur_x,cur_y))
    #print("end at",(cur_x,cur_y))
    return (cur_x,cur_y)

#path = split_instructions('esenee')
#print(path)

for l in lines:
    path = split_instructions(l.strip())
    tile = get_last_tile(path)
    if tile not in floor_map:
        floor_map[tile] = 1 #
    else:
        #print("existing tile")
        if floor_map[tile] == 0:
            floor_map[tile] = 1
        else:
            floor_map[tile] = 0

    #print("now at",tile)

black = 0
white = 0
for k,v in floor_map.items():
    #print(k,v)
    if v == 1:
        black += 1
    else:
        white += 1

new_floor = expand_floor(floor_map)

for k,v in new_floor.items():
    print(k,v,get_adj_black(k))

#print(get_adj_black((0,0)))

print("black tiles:",black)
print("white tiles:",white)
    
#print(get_last_tile(split_instructions('nwwswee')))