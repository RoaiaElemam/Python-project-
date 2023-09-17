'''Transform all names to uppercase using [normal list - list comprehension - functional programming]
Names = [‘mahmoud’,’farida’,’ali’,’hassan’,’mohamed’,’khaled’,’taha’] 
'''
#Normal list
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
result=[] 
for name in Names:
    result.append(name.upper()) 
print(result)

#list comprehension
result1=[name.upper() for name in Names]
print(result1)

#functional programing
def Upper (n):
    return n.upper()

result2=list(map(Upper,Names))
print(result2)