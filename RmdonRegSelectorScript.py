import sys
import random
#print("Hello, World")
#print(sys.version)

stdReg = {
    0:'FA17-BSE-(103,131,160)',
    1:'FA17-BSE (106,108,142)',
    2:'FA17-BSE-(104,081)',
    3:'FA17-BSE-(105,109,138)',
    4:'FA17-BSE-(130,107)',
    5:'Fa17-BSE-(137,123)',
    6:'FA17-BSE-(102,149)',
    7:'FA17-BSE-(145,152,143)',
    }

def printStd(dic):
    for item in dic:
        print(dic[item])
print('Orignal List')
printStd(stdReg)


print('-------------------------')
print('Randomly generated LIST : ')
randomList =(random.sample(range(0, len(stdReg)), len(stdReg)))
num = 0
for i in randomList:
    print("Serial number : "+str(num)+"\n \t"+stdReg[i])
    num+=1
