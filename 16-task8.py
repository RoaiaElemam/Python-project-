'''Unpack the list in a = the first index , b = the second index
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
'''
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
#a=Names[0]
#b=Names[1]
a,b,*_=Names
print(a,"....",b)