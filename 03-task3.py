'''Create a python function that takes 2 numbers x,y and prints the multiplication table from x to y'''

def multi(x,y): 
   for i in range(x,y+1):
      print("multiplication table for :",i)
      for j in range(1,11):
        print(i,'x',j,'=',i*j)

        
print(multi(3,5))
