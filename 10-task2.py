'''Get the names that contains ‘a’ in a list using [normal list - list comprehension - functional programing
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
'''
#normal list
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha','reem']
result=[]
for name in Names:
    if 'a' in name:
        result.append(name)
print(result)

#list comprehension
result1=[name for name in Names if 'a' in name]
print(result1)

#functional programing
def contain (name):
    if 'a'in name:
        return name
result2=list(filter(contain,Names))
print(result2)