#exception handling
#if we give float value in run time then it will raise error becoz we give int in user input before try block
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    try:
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exceptions")
    finally:
        print("program ends")'''

#if we give float value in run time then it will not raise error becoz we give it in try block so it will take float value also
'''while True:
    try:
        a=int(input("a value"))
        b=int(input("b value"))
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exceptions")
    finally:
        print("program ends")'''
        
#file handling
#write() mode
'''a=open("uma.txt","w")
a.write("python full stack")
a.close()'''

'''a=open("uma.txt","w")
a.write("vijayawada")
a.close()'''

#append() mode
'''a=open("uma.txt","a")
a.write("\thyd")
a.close()'''

#using run time
'''a=open("uma.txt","w")
a.write(input("data"))
a.close()'''

'''a=open("uma.txt","w")
b=input("data")
a.write(b)
a.close()'''

#read()
#readlines()
#a=open("uma.txt")
#print(a.read()) #display entire content
#print(a.readline()) #display 1st line
#print(a.readlines()) #display with \n-new line
#print(a.read(35)) #display no. of characters

#writelines()->it makes every object side by side
'''a=open("python.txt","w")
b=["Priya","sowmya","bhavika","uma","himaja"]
a.writelines(b)
a.close()'''

'''a=open("python.txt","w")
b=["Priya","sowmya","bhavika","uma","himaja"]
a.writelines("\n".join(b))
a.close()'''

#open add.py file with out path
'''a=open("add.py")
print(a.read())'''

#open add.py file with path
'''a=open("C:\\Users\\PRADEEP\\OneDrive\\Desktop\\python")
print(a.read()) #error '''

'''a=open("C:\\Users\\PRADEEP\\OneDrive\\Desktop\\python\\add.py")
print(a.read())'''
