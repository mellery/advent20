filename = "input14.txt"
#filename = "input14_ex1.txt"

file1 = open(filename, 'r') 
lines = file1.readlines() 

def bitmask(mask,val):
    result = []
    for i in range(0,len(mask)):
        if mask[i] == 'X':
            result.append(val[i])
        else:
            result.append(mask[i])
    return "".join(result)

registers = {}

for l in lines:
    temp = l.strip()
    if 'mask' in temp:
        mask = temp.split('=')[1].strip()
        masklen = len(mask)
        print("mask = ",mask)
    else:
        
        val = bin(int(temp.split('=')[1])).split('b')[1]
        val = "0"*(masklen-len(val))+val
        #print(valt)

        reg = temp.split(']')[0].split('[')[1]
        print('[',reg,']')
        print('value:\t',val)
        print('mask:\t',mask)
        
        ans = bitmask(mask,val)
        registers[reg] = ans
        
        print('result:\t',ans,int(ans,2))
        
print(registers)

total = 0
for r,v in registers.items():
    total = total + int(v,2)
    print("reg",r,"=",int(v,2))

print("total = ",total)