filename = "input12.txt"
#filename = "input12_ex.txt"
#filename = "input12_ex2.txt"
file1 = open(filename, 'r') 
lines = file1.readlines() 

mv = []
dist = []

for l in lines:
    temp = l.strip()
    mv.append(temp[0])
    dist.append(int(temp[1:]))

x = 0
y = 0

heading = 'E'

#  N
# W E
#  S

def turn_boat(heading,turn,deg):
    print("facing",heading,"turning",turn,deg,"degrees")
    if deg == 270:
        deg = 90
        if turn == 'L':
            turn = 'R'
        elif turn == 'R':
            turn = 'L'

    if deg == 180:
        if heading == 'N':
            return 'S'
        if heading == 'E':
            return 'W'
        if heading == 'S':
            return 'N'
        if heading == 'W':
            return 'E'

    elif deg == 90:
        if heading == 'N':
            if turn == 'L':
                return 'W'
            if turn == 'R':
                return 'E'

        if heading == 'E':
            if turn == 'L':
                return 'N'
            if turn == 'R':
                return 'S'    

        if heading == 'S':
            if turn == 'L':
                return 'E'
            if turn == 'R':
                return 'W'

        if heading == 'W':
            if turn == 'L':
                return 'S'
            if turn == 'R':
                return 'N'
    else:
        print("degree error",deg)

def move_boat(x,y, mv,dist):
    print("moving ",mv, dist)
    if mv == 'N':
        y = y - dist

    if mv == 'E':
        x = x + dist

    if mv == 'S':
        y = y + dist

    if mv == 'W':
        x = x - dist

    return x,y

for i in range(0, len(mv)):
    print(mv[i],dist[i])

    if mv[i] in ['N','E','S','W']:
        x,y = move_boat(x,y,mv[i],dist[i])    

    if mv[i] in ['L','R']:
        heading = turn_boat(heading,mv[i],dist[i])
        
    if mv[i] == 'F':
        x,y = move_boat(x,y,heading,dist[i])

    if y < 0:
        lat = 'north'
    else:
        lat = 'south'
    if x < 0:
        lon = 'west'
    else:
        lon = 'east'

    print("boat at ",x,lon,',',y,lat,"hdg",heading)

print(abs(x)+abs(y))
