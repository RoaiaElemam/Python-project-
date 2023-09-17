'''Get the names that contains 2 or more ‘a’ letter using [normal list - list comprehension - functional
programming]
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
'''
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
RESULT=[]
char='a'
#normal list
for name in Names:
    if name.count(char) == 2:
        RESULT.append(name)
print (RESULT)

#list comprehension
result1=[name for name in Names if name.count(char)==2]
print(result1)

#functional programing

def contain (name):
    if name.count(char) == 2:
        return name
result2=list(filter(contain,Names))
print(result2)
