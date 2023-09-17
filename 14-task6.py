'''Unpack the list in  a=the first index, b=rest of the list
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
'''
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
a,*b=Names
print(a,'...',b)