filename = "input20.txt"
#filename = "input20_ex1.txt"

file1 = open(filename, 'r') 
lines = file1.readlines() 

class Piece:
    id = 0

    image = []

    def printImage(self):
        for r in self.image:
            print(r)
        print('\n')

    def sides(self):
        return [self.sideA(),self.sideB(),self.sideC(),self.sideD()]

    def sideA(self):
        return self.image[0]

    def sideB(self):
        temp = ""
        for x in range(0,len(self.image)):
            temp = temp+self.image[x][len(self.image)-1]
        return(temp)

    def sideC(self):
        temp = ""
        for x in range(0,len(self.image)):
            temp = temp+self.image[x][0]
        return(temp)

    def sideD(self):
        return self.image[len(self.image)-1]

Puzzle = {}

id = 0
tile = []

for l in lines:
    temp = l.strip()

    if 'Tile' in temp:
        print("new tile",temp)
        if id not in Puzzle and id != 0:
            p = Piece()
            p.id = id
            p.image = tile.copy()
            Puzzle[id] = p
            tile = []
            print("adding",id)
        
        id = int(temp.split(' ')[1][:-1])
        
    elif len(temp) > 1:
        tile.append(temp)

#add the last tile
if id not in Puzzle and id != 0:
    p = Piece()
    p.id = id
    p.image = tile.copy()
    Puzzle[id] = p
    tile = []
    print("adding",id)

corners = []

for k1,v1 in Puzzle.items():
    print('\n')
    matches = 0
    print(k1)
    for k2,v2 in Puzzle.items():
        if k1 != k2:
            if v1.sideA() in v2.sides():
                print(k1,'A matches',k2)
                matches = matches + 1
            if v1.sideB() in v2.sides():
                print(k1,'B matches',k2)
                matches = matches + 1
            if v1.sideC() in v2.sides():
                print(k1,'C matches',k2)
                matches = matches + 1
            if v1.sideD() in v2.sides():
                print(k1,'D matches',k2)
                matches = matches + 1
            if v1.sideA()[::-1] in v2.sides():
                print(k1,'A matches',k2)
                matches = matches + 1
            if v1.sideB()[::-1] in v2.sides():
                print(k1,'B matches',k2)
                matches = matches + 1
            if v1.sideC()[::-1] in v2.sides():
                print(k1,'C matches',k2)
                matches = matches + 1
            if v1.sideD()[::-1] in v2.sides():
                print(k1,'D matches',k2)
                matches = matches + 1
    print(k1,"matches",matches,"other pieces")
    if matches == 2:
        corners.append(k1)

print(corners)
ans = 1
for c in corners:
    ans = ans * c
print(ans)