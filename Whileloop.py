it = 10
#WHILE will run till condition is false
while it>1:
    if it != 3:
        print(it)
    if it == 9:
        it = it -1
        continue
    if it == 3:
        break
    print(it)
    it = it - 1
        #4-1=3
        #3-1=2
        #2-1=1
    print('while loop execution is done')