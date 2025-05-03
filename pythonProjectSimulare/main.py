#1.
list1=[3472,490,222222,111]
list2=[]
def f1(list1,list2):
    if(len(list1)==0):
        return list2
    else:
        def com1(x, s):
            if (x == 0):
                return s
            else:
                if (x % 2 == 0):
                    return com1(x // 10, s + x % 10)
                else:
                    return com1(x // 10, s)
        list2.append(com1(list1[0],0))
        return f1(list1[1:],list2)
print(f1(list1,list2))
#2.
import functools
set1={1,3,1,4,8,9}
set2=set()
def subset(set1,con):
    def f2(acc,el):
        if(con(el)==True):
            set2.add(el)
        return acc
    return functools.reduce(f2,set1,set2)
print(subset(set1,lambda x:x>3))





#3.
import functools
dict1={'a':1,'b':2,'c':3,'d':4,'e':5}
dict2={'a':1,'d':2,'f':3,'g':4,'e':5}
dict3={}
def com3(dict1,dict2,dict3):
    def f3(acc,key_value):
        key,value=key_value
        if(key in dict2.keys()):
            dict3[key]=dict1[key]+dict2[key]
        return acc
    return functools.reduce(f3,dict1.items(),dict3)
print(com3(dict1,dict2,dict3))