'''Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 than can be divided on x,y'''
x=int(input("Enter the value of x...."))
y=int(input("Enter the value of y...."))

list=[]
for i in range(1,101):
    if i%x==0 and i%y==0 :
        list.append(i)
        
print(list)
