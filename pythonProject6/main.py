#Lab6.
#1.
list1=[('a', 7), ('b', 5), ('c', 2), ('a', 3), ('b', 3)]
d1={}
def f1(list1,d1):
    if(len(list1)==0):
        return d1
    else:
        if(list1[0][0] in d1):
            d1[list1[0][0]]=d1[list1[0][0]]+list1[0][1]
        else:
            d1[list1[0][0]]=list1[0][1]
        return f1(list1[1:],d1)
print(f1(list1,d1))
#2.
list2=["aaa", "bbb", "aabbb"]
d2={}
def f2(list2,d2):
    if(len(list2)==0):
        return d2
    else:
        if(len(list2[0])==0):
            return f2(list2[1:],d2)
        else:
            if(list2[0][0] in d2):
                d2[list2[0][0]]=d2[list2[0][0]]+1
            else:
                d2[list2[0][0]]=1
            list2[0]=list2[0][1:]
            return f2(list2,d2)
print(f2(list2,d2))
#3.
import functools
d3={'a': 5, 'b': 7, 'c': 1}
d3nou={}
def con(x):
    if(x>5):
        return True
    else:
        return False
def filter(con,d3,d3nou):
    def f3(acc,key_value):
        key,value=key_value
        if(con(value)==True):
            acc[key]=value
        return acc
    return functools.reduce(f3,d3.items(),d3nou)
print(filter(con,d3,d3nou))
#4.
d4={'a': 6, 'b': 1, 'c': 8}
d4nou={}
def exists(con,d4,d4nou):
    def f4(acc,key_value):
        key,value=key_value
        if(con(value)==True):
            return True
        return acc
    return functools.reduce(f4,d4.items(),False)
print(exists(con,d4,d4nou))
def for_all(con,d4,d4nou):
    def f4_1(acc,key_value):
        key,value=key_value
        if(con(value)==False):
            return False
        return acc
    return functools.reduce(f4_1,d4.items(),True)
print(for_all(con,d4,d4nou))
#5.
d5={'a': 5, 'b': 7, 'c': 6}
d5nou={}
def con5(x):
    return x+1
def map(con5,d5,d5nou):
    def f5(acc,key_value):
        key,value=key_value
        acc[key]=con5(value)
        return acc
    return functools.reduce(f5,d5.items(),d5nou)
print(map(con5,d5,d5nou))
#7.
