import random   

#size = int(input("give me a size for your random size list"))

random_list = [2,1,2,3,7]
value = 0
#random_list = [ random.randrange(size) for x in range(size)]
def rec_check():
    value = random_list.pop()
    if len(random_list) !=0:
            
        for x in random_list:
            if value >= x:
                pass
            else :
                return False
        if (rec_check() ==False):
            print("not sorted ")
            exit()
            
            
    else:
        print("sorted")




if "__main__":
    rec_check()



