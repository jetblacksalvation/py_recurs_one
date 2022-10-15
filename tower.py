import random

print("how many layers for tower? ")
num = int(input())

tower = [random.randrange(num) for x in range(num)]
tower.sort()



#tower is defined randomly, use sort func 



def body(tow_er):
    #initlialize/create vars here 
    temp = tow_er
    iters = 0
    
    
    vall_iter(temp, iters)
def vall_iter(var :list(), it):
    if it == len(tower)-1 or len(var)-1 <=1:
        return
    print(" put val ", var.pop(), "on peg 2")
    vall_iter(var, it)

    
if  "__main__":
    body(tower)
