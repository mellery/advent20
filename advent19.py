#filename = "input19.txt"
filename = "input19_ex1.txt"
#filename = "input19_ex2.txt"

file1 = open(filename, 'r') 
lines = file1.readlines() 

rules = {}
messages = []
for l in lines:
    temp = l.strip()
    print(temp)
    if ':' in temp:
        rules[int(temp.split(':')[0])] = temp.split(':')[1].strip()
    elif len(temp) > 1:
        messages.append(temp)

def contains_digit(rule):
    temp = rule.split(' ')
    for t in temp:
        if t.isdigit():
            return True
    return False

def substitute_rule(rule):
    temp = rule.split(' ')
    newrule = ""

    for t in temp:
        if t.isdigit():
            newrule = newrule + ' ( ' + rules[int(t)] + " ) "
        else:
            newrule = newrule + t
    newrule = newrule.replace('"','')
    newrule = newrule.replace("(a)",'a')
    newrule = newrule.replace("(b)",'b')
    newrule = newrule.replace("( a )",'a')
    newrule = newrule.replace("( b )",'b')
    newrule = newrule.replace("( b )",'b')
    return newrule


temp = rules[0]

print(temp)

while contains_digit(temp):
    temp = substitute_rule(temp)
    #print(temp)
temp = temp.replace(' ','')
#temp = temp.replace("(aa)","aa")
#temp = temp.replace("(ab)","ab")
#temp = temp.replace("(ba)","ba")
#temp = temp.replace("(bb)","bb")
print(temp)

outer = temp[temp.find('(')+1:temp.rfind(')')]
#temp = temp.replace('('+outer+')',c)
valid = []
valid.append('a'+outer.split('|')[0])
valid.append('a'+outer.split('|')[1])
print(valid)

