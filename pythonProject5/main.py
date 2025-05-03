#Lab5.
#1.
set1={1,2,3}
import functools
def f1(acc,el):
    acc.add(el)
    return acc
print(functools.reduce(f1,set1,set()))
#2.
list2=[(1,2),(3,4)]
def f2(acc,el):
    acc.add(el[0])
    return acc
print(functools.reduce(f2,list2,set()))
#3.
def con(x):
    if(x%2==0):
        return True
    else:
        return False
set3={1,2,3,4}
print(set(filter(con,set3)))
#4.
list5=[{1, 2, 3}, {1, 2, 3, 4}, {3, 5, 6, 7}]
R=set()
I=list5[0]
def f5(list5,R):
    if(len(list5)==0):
        return R
    else:
        return f5(list5[1:],R|list5[0])
print(f5(list5,R))
def f5_1(list5,I):
    if(len(list5)==0):
        return I
    else:
        return f5_1(list5[1:],I&list5[0])
print(f5_1(list5,I))
