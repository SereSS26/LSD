#EXAMEN.
#1.
a=3
b=6
c=4
def f1(a,b,c):
    return a<=c<=b
print(f1(a,b,c))
#2.
n=13
d=2
def f2(n,d):
    if(d==n):
        return True
    else:
        if(n%d==0):
            return False
        return f2(n,d+1)
print(f2(n,d))
#3.
a=12
b=16
def f3(a,b):
    if(a%b==0 or b%a==0):
        return min(a,b)
    else:
        if(a>b):
            return f3(a-b,b)
        else:
            return f3(a,b-a)
print(f3(a,b))
#4.
a='abc'
anou=''
def f4(a,anou):
    if(len(a)==0):
        return anou
    else:
        return f4(a[1:],a[0]+anou)
print(f4(a,anou))
#5.
n=16
nou=''
def f5(n,nou):
    if(n==0):
        return nou
    else:
        return f5(n//2,str(n%2)+nou)
print(f5(n,nou))
#6.
n=5
d=1
def f6_1(d,m):
    if(m==0):
        print(end='\n')
        return
    else:
        print(d,end=' ')
        return f6_1(d,m-1)
def f6(d,n):
    if(d<=n):
        f6_1(d,d)
        return f6(d+1,n)
print(f6(d,n))
#7.
list1=[1,2,3,4,5,6]
def f7(n):
    return n%10
print(sorted(list1,key=f7,reverse=True))
#8.
import functools
list7=[]
def f7(acc,el):
    if(el%2==0):
        list7.append((el))
    return acc
functools.reduce(f7,list1,list7)
print(list7)
#9.
list9=[(1,2), (3,4), (5,6)]
#10.
set1={1,2,3}
def f10(set1):
    print(set1)
f10(set1)
#11.
l11=[(1,2), (3,4)]
set11=set()
def f11(set11,l11):
    if(len(l11)==0):
        return set11
    else:
        set11.add(l11[0][1])
        return f11(set11,l11[1:])
print(f11(set11,l11))
#12.
s12={1,2,3,4}
print(set(filter(lambda x:x%2==0,s12)))
#13.
l13=[('a', 7), ('b', 5), ('c', 2), ('a', 3), ('b', 3)]
d13={}
def com13(l13,d13):
    def f13(acc,key_value):
        key,value=key_value
        if(key in d13):
            d13[key]=d13[key]+value
        else:
            d13[key]=value
        return acc
    return functools.reduce(f13,l13,d13)
print(com13(l13,d13))
#14.
l14=["aaa", "bbb", "aabbb"]
d14={}
def com14(l14,d14):
    def f14(acc,value):
        if(len(value)==0):
            return acc
        else:
            if(value[0] in d14):
                d14[value[0]]=d14[value[0]]+1
            else:
                d14[value[0]]=1
            value=value[1:]
            return f14(acc,value)
    return functools.reduce(f14,l14,d14)
print(com14(l14,d14))
#15.
def con15(x):
    if(x>=5):
        return True
    else:
        return False
d15={'a': 5, 'b': 7, 'c': 1}
d15nou={}
def com15(con15,d15,d15nou):
    def f15(acc,key_value):
        key,value=key_value
        if(con15(value)==True):
            d15nou[key]=value
        return acc
    return functools.reduce(f15,d15.items(),d15nou)
print(com15(con15,d15,d15nou))
#16.
d16={'aa': 5, 'bb': 7, 'ca': 6}
l16=['aa', 'bb', 'c']
set16=set()
def com16(d16,l16,set16):
    def f16(acc,el):
        if(el in d16.keys()):
            set16.add(d16[el])
        return acc
    return functools.reduce(f16,l16,set16)
print(com16(d16,l16,set16))
#17.
arbore_binar={
    "value":1,
    "left":{
        "value":2,
        "left":{
            "value":3,
            "left":None,
            "right":None
        },
        "right":None
    },
    "right":{
        "value":4,
        "left":None,
        "right":None
    }
}
print(arbore_binar)
list17=[]

def f17(arbore_binar,list17):
    if(arbore_binar!=None):
        list17.append(arbore_binar["value"])
        return f17(arbore_binar["left"],list17)+[arbore_binar["value"]]+f17(arbore_binar["right"],list17)
    else:
        return []
print(f17(arbore_binar,list17))
print(list17)
#18.
list18=[]
n=0
def f18(arbore_binar,list18,n):
    if(arbore_binar["value"]!=None):
        if(arbore_binar["left"]==None and arbore_binar["right"]==None):
            list18.append(arbore_binar["value"])
    if(arbore_binar["right"]!=None):
        f18(arbore_binar["right"],list18,n)
    if(arbore_binar["left"]!=None):
        f18(arbore_binar["left"],list18,n)
    return n
f18(arbore_binar,list18,n)
print(list18)
#19.
list19=[0]
el=0
print("MA CAC")
def f19(arbore_binar,el):
    if(arbore_binar["left"]!=None):
        f19(arbore_binar["left"],el+1)
    if(arbore_binar["right"]!=None):
        f19(arbore_binar["right"],el+1)
    if(arbore_binar["value"]!=None):
        print(arbore_binar["value"],el)
f19(arbore_binar,el)
#20.
def f20(arbore_binar):
    if(arbore_binar!=None):
        arbore_binar["left"]=arbore_binar["right"]
        arbore_binar["right"]=arbore_binar["left"]
        f20(arbore_binar["left"])
        f20(arbore_binar["right"])
print(arbore_binar)
f20(arbore_binar)
print(arbore_binar)
#21.
def f21(arbore_binar):
    if(arbore_binar!=None):
        if(arbore_binar["right"]==None):
            arbore_binar["value"]=None
            arbore_binar["left"]=None
            arbore_binar["right"]=None
        f21(arbore_binar["right"])
        f21(arbore_binar["left"])
f21(arbore_binar)
print(arbore_binar)