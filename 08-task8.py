'''Create a function that takes x,y and prints all the number that can be divide by y from x to 100'''
list=[]
def div(x,y):
    for i in range(x,101):
        if i%y==0:
            list.append(i)
    print(list)

print(div(1,10))