from math import gcd

filename = "input13.txt"
#filename = "input13_ex1.txt"

file1 = open(filename, 'r') 
lines = file1.readlines() 

for l in lines:
    temp = l.strip()
    print(temp)

time = int(lines[0])
buses = lines[1].split(',')
#buses = [17,'x',13,19] #3417
#buses = [67,7,59,61] #754018
#buses = [67,'x',7,59,61] #779210
#buses = [67,7,'x',59,61] #1261476
#buses = [1789,37,47,1889] #1202161486


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def bus_dept(ts,bus):
    if ts%int(bus) == 0:
        return True
    else:
        return False

t = time
found = False
while found == False:
    for b in buses:
        if b != 'x':
            if bus_dept(t,b):
                print(t,b,time%int(b))
                print("wait",t-time,'minutes')
                print(int(b)*(t-time))
                found = True
    t = t + 1

def part2(buses):
    valid = []
    for b in buses:
        if b != 'x':
            valid.append(int(b))
    print(buses)
    slowest = max(valid)
    offset = buses.index(slowest)
    print(slowest,offset)
    t = slowest
    
    all_found = False
    while all_found == False:
        #print(t)
        all_found = True
        for b in range(0,len(buses)):
            if buses[b] != 'x' and bus_dept(t+b-offset,buses[b]) == False:
                all_found = False
        if all_found == True:
            print("all_found",t-offset)
                
            return True,t-offset
            
        t = t + slowest #int(buses[0])
        
temp = lines[1].split(',')
buses = []
for t in temp:
    if t != 'x':
        buses.append(int(t))
    else:
        buses.append(t)

x = 'x'
print('---')
#print(part2([17,x,13,19])) #3417
#print(part2([67,7,59,61])) #754018
#print(part2([67,x,7,59,61])) #779210
#print(part2([67,7,x,59,61])) #1261476
#print(part2([1789,37,47,1889])) #1202161486
#print(part2([13,x,x,41,x,x,x,x,x,x,x,x,x,641,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,661,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23]))

import numpy as np
from math import prod

with open("input13.txt") as f:
    lines = [x.strip() for x in f]

arrival = int(lines[0])
buses = [(i, int(e)) for i, e in enumerate(lines[1].split(",")) if e.isdigit()]

times = [t for _, t in buses]
b = [e - (arrival % e) for e in times]
print(np.min(b) * times[np.argmin(b)])

def crt(ns, bs):
    # Chinese Remainder Theorem
    # https://brilliant.org/wiki/chinese-remainder-theorem/
    N = prod(ns)
    x = sum(b * (N // n) * pow(N // n, -1, n) for b, n in zip(bs, ns))
    return x % N

offsets = [time-idx for idx, time in buses]
print(crt(times, offsets))