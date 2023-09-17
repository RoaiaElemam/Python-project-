''' Print a list contains the len of each word in the list using [normal list - list comprehension -
functional programming]
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
'''
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
result=[]
#normal list
for name in Names:
    Len_str=len(name)
    result.append(Len_str)
print(result)

#list comprehension
result1=[len(name) for name in Names]
print(result1)

#functional programming
def len_st(name):
    L=len(name)
    return L
result2=list(map(len_st,Names))
print(result2)
