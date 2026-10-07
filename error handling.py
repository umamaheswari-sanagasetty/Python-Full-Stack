#error handling
#syntax error
'''for i in range(10) #syntax error expected :
print(i)'''

'''for i in range(10): 
print(i)''' #syntax error indentation 

'''for i in range(10):
    print(i''' #syntax error ( was never closed

'''for i in range(10):
    print(i)'''
    
#run_time error
'''Print(5+9)''' #name error

'''a=int(input("a value"))
b=int(input("b value"))
print(a//b)''' #type error, value error, 0 division error

#logical error
'''a=10
b=20
print(a-b)'''

'''a=4
b=8
if a<b:
    print("less")'''
