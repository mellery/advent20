
filename = "input21.txt"
#filename = "input21_ex1.txt"

file1 = open(filename, 'r') 
lines = file1.readlines() 

ingrediants = {}
recipies = []
all_allergens = []
food_label = {}

for l in lines:
    temp = l.strip()
    foods = temp.split('(')[0].strip().split(" ")
    recipies.append(foods)
    allergens = temp.split('(contains ')[1][0:-1].split(',')

    food_label[temp.split('(')[0].strip()] = allergens

    for f in foods:
        ingrediants[f] = []
        for a in allergens:
            temp = a.strip()
            if temp not in all_allergens:
                all_allergens.append(temp)
            ingrediants[f].append(temp)

for k in ingrediants:
    ingrediants[k] = all_allergens.copy()
    print("ingrediant",k,"might contain",ingrediants[k])

for k in ingrediants:
    for f in food_label:
        parts = f.split()
        if k not in parts and len(food_label[f]) == 1:
            for i in food_label[f]:
                temp = i.strip()
                if temp in ingrediants[k]:
                    ingrediants[k].remove(temp)
    
print("")
safe = []
for k in ingrediants:
    print(k,ingrediants[k])
    if len(ingrediants[k]) == 0:
        safe.append(k)

print("SAFE")
print(safe)

#safe.sort()

total = 0
for s in safe:
    #print(s)
    for f in food_label:
        if s in f:
            total = total + 1

print(total)

#print all recipies after removing safe ingrediants

#2183 too high
