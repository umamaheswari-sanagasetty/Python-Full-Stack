#sys module
'''import sys
print(sys.path)'''

#1 by 1
'''for i in sys.path:
    print(i)'''
'''print(sys.version)'''

#os module
#import os
#print(os.path)
#print(os.getcwd())
#print(os.listdir())
#print(os.mkdir("oct5"))
#print(os.listdir())
#print(os.chdir("C:\\Users\\PRADEEP\\Downloads"))
#print(os.listdir())

#random module
#sample
'''import random
a=random.range(10,50)
print(a) #error'''

'''import random
a=random.sample(range(10,50),41)
print(a) #error'''

'''import random
a=random.sample(range(10,50),5)
print(a)'''

#randint() - to generate randomly single no.
'''import random
a=random.randint(5,12)
print(a)'''

#choice
'''import random
a=[10,20,30,40,50]
b=random.choice(a)
print(b)'''

#task-dice
'''import random
while True:
    input("enter the roll of dice: ")
    a=random.randint(1,6)
    print(a)
    option=input("enter your option: 1.Yes\n 2.No")
    if option=="1":
        continue
    elif option=="2":
        break'''
    
'''import random
while True:
    input("enter the roll of dice")
    a=random.randint(1,6)
    print(a)
    option=input("roll again?(y/n)")
    if option=="y":
        continue
    elif option=="n":
        break'''

#calndar module
'''import calendar
year=2026
month=10
print(calendar.month(year,month))'''

'''import calendar
year=2027
print(calendar.calendar(year))'''

'''import calendar
a=int(input("enter the year"))
b=int(input("enter the month"))
print(calendar.month(a,b))'''

#date & time
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

#epoch time
'''import time
a=time.time()
print(a)

#to convert epoch time into local time
b=time.localtime(a)
print(b)

#to display human readbale time
print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"today time is {b.tm_hour}-{b.tm_min}-{b.tm_sec}")
print(f"overall {b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")'''

#task - by using time and random module
'''import random
import time
for i in range(0,11):
    b=random.randint(0,11)
    print(b)
    c=time.sleep(2)'''

'''import random
import time
for i in range(10):
    a=random.randint(30,60)
    print(a)
    time.sleep(2)'''

#regular expressions(regex)- re
'''a="codegnan is in vij"
print(a)'''

'''a="codegnan\nis\tin\nvij"
print(a)'''

#raw string
'''a=r"codegnan\nis\tin\nvij"
print(a)'''

#compile(), search(), findall(), split(), sub()
#sequence characters
'''\w->it matches alphanumeric
\W->it matches non-alphanumeric
\d->it matches any digit
\D->it matches non-digits
\s->it represents white spaces
\S->it represents non-white spaces - remove white spaces'''

#compile()-just run the code whatever we write in print
import re
'''a="code map money cash cap maths cup cat mug mat"'''
'''b=re.compile(r"m\w\w\w\w\w") #1stw-2 letters next single \w-1 letter
print(b)'''

#search()- to print a word
'''c=b.search(a)
print(c)'''

'''c=re.search(r"m\w+",a) #to overcome \w\w\w\w\w we can use \w+ & search 1 m word
print(c)'''

#findall() - to print all the words
'''b=re.findall(r"m\w+",a) #to overcome \w\w\w\w\w we can use \w+ & search all m words
print(b)'''

'''b=re.findall(r"c\w+",a) #to overcome \w\w\w\w\w we can use \w+ & search all c words
print(b)'''

#split()
'''c=re.split(r"m",a)
print(c)'''

'''c=re.split(r"m\s",a)
print(c)'''

'''c=re.split(r"\s",a)
print(c)'''

#sub()-substitute the letters & words
'''e=re.sub(r"maths","science",a)
print(e)'''

'''f=re.sub(r"m","n",a)
print(f)'''

#digits
'''a="code 10 gnan 20 30 man 40 map 50 cup 60 70"
b=re.findall(r"\d+",a) #+ print with merge all the numbers
print(b)'''

'''a="code 10 gnan 20 30 man 40 map 50 cup 60 70"
b=re.findall(r"\d",a)  #print in single quotes with single no  
print(b)'''
