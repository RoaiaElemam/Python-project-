'''Get the names that starts with ‘t’ in a list using [normal list - list comprehension - functional
programming]
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
'''
#normal list
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
result=[]
check='t'
for name in Names:
     if(name.find(check) == 0 or name.find(check.lower()) == 0):
        result.append(name)
print("the list of names start with of 't' :", result)


#list comprehension 
result1=[name for name in Names  if(name.find(check) == 0 or name.find(check.lower()) == 0) ]
print("the list of names start with of 't' :", result1)

# functional programming
def Find (name):
    if(name.find(check) == 0 or name.find(check.lower()) == 0):
        return name
        
result2=list(filter(Find,Names))
print("the list of names start with of 't' :", result2)
