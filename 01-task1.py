#Create a python function that takes 2 numbers x,y and prints 2 list containing the odd and even numbers in x,y range
x=int(input("Enter the start number....."))
y=int(input("Enter the end number....."))
list1=[]
list2=[]
for i in range(x,y+1):
    if i%2 == 0:
        list1.append(i)
    else:
        list2.append(i)
print(list1,list2)

