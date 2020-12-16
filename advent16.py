
filename = "input16.txt"
#filename = "input16_ex1.txt"
#filename = "input16_ex2.txt"

file1 = open(filename, 'r') 
lines = file1.readlines() 

fields = {}

your_ticket_found = False
nearby_tickets_found = False

myticket = []
tickets = []

for l in lines:
    temp = l.strip()
    
    #print(len(temp),temp)
    
    if len(temp) == 0:
        continue
    
    elif 'your ticket' in temp:
        your_ticket_found = True
    elif 'nearby tickets' in temp:
        nearby_tickets_found = True

    elif your_ticket_found == False and nearby_tickets_found == False:
        field = temp.split(':')[0]
        rulestr = temp.split(':')[1]
        rules = rulestr.split(' or ')
        fields[field] = rules

    elif your_ticket_found == True and nearby_tickets_found == False:
        myticket = temp.split(',')
    
    else:
        ticket = temp.split(',')
        tickets.append(ticket)

    #print(temp)

#for f,v in fields.items():
#    print(f,v)

#print("\nmy ticket",myticket)
#print('\nnearby')
#for t in tickets:
#    print(t)

def validate_ticket(ticket):
    invalid = []
    for x in ticket:
        n = int(x)
        #print(n)
        any_field = False
        invalid_count = 0
        for field, rule in fields.items():
            #print(field)
            #for r in rule:
            low = int(rule[0].split('-')[0])
            hi = int(rule[0].split('-')[1])
            low2 = int(rule[1].split('-')[0])
            hi2 = int(rule[1].split('-')[1])
            #print(low,n,hi)
            
            if ((n >= low and n <= hi) or (n >= low2 and n <= hi2)) == False:
                #print(n,'not valid for',field)
                invalid_count = invalid_count + 1
        #print(x,invalid_count,len(fields))
        if invalid_count == len(fields):
            invalid.append(n)
    return sum(invalid)
        
ans = 0
#print("#stating tickets",len(tickets))
good_tickets = []
for t in tickets:
    #print(t)
    result = validate_ticket(t)
    #print(result,t)
    if result == 0:
        good_tickets.append(t)
    ans = ans + result    
print("answer",ans)

good_tickets.append(myticket)
#print("#valid tickets",len(good_tickets))

#for t in good_tickets:
#    print(t,validate_ticket(t))

for field, rule in fields.items():
    print(field)
    for col in range(0,len(myticket)):
        valid_count = 0

        for t in good_tickets:
            #print(t)
            
            n = int(t[col])
            low = int(rule[0].split('-')[0])
            hi = int(rule[0].split('-')[1])
            low2 = int(rule[1].split('-')[0])
            hi2 = int(rule[1].split('-')[1])
            #print(low,n,hi)
            
            if ((n >= low and n <= hi) or (n >= low2 and n <= hi2)) == True:
                #print(n,'valid for',field)
                valid_count = valid_count + 1
    
        if valid_count == len(good_tickets):
            print("col",col,"valid for",field)

#manually figured out columns based on process of elimination of which columns were valid for which fields
#1    departure location
#3    departure station
#8    departure platform
#7    departure track
#14    departure date
#0    departure time

print(int(myticket[1])*int(myticket[3])*int(myticket[8])*int(myticket[7])*int(myticket[14])*int(myticket[0]))

    
