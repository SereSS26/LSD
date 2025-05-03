#Lab4-Liste
#1.
import functools
list1=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x:x%2==0,list1)))
#2.
list2=['a','aa','aaa','aaaa']
print(list(filter(lambda x:len(x)<=2,list2)))
#4.
print(sorted(list1,key=lambda x:x%10,reverse=True))
#5.
list1.append(0)
def f4(x,y):
    return x*y
print(functools.reduce(f4,list1))
#6.
list3=list(map(lambda x:x**3,list1))
print(list3)
#7.
list4=list(filter(lambda x:x%2==0,list1))
print(list4)
list1=[1,2,3,4]
#Partea 2
#1.
n = 1234
list1=[]
def f1_1(list1, n):
    if n == 0:
        return list1
    else:
        list1.append(n % 10)
        return f1_1(list1, n // 10)
print(f1_1(list1, n))
def con(x):
    if(x%2==0):
        return True
    else:
        return False
def f1_2(n,list1,con):
    if(n==0):
        return list1
    else:
        if(con(n%10)==True):
            list1.append(n%10)
        return f1_2(n//10,list1,con)
print(f1_2(n,list1,con))
list1=[1,2,3,4,5,6]
#10.
def f10(x,y):
        if(y%2==0):
            print(x)
print(functools.reduce(f10,list1))
