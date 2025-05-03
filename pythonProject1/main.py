#Lab1.
#1.
a=34
def f1(a):
    return a%10
print(f1(a))
#2.
c=1
h=1
o=1
def f2(c,h,o):
    return c*12+h*1+o*16
print(f2(c,h,o))
#3.
a=1
b=2
c=1
import math
def f3(a,b,c):
    if(math.sqrt((b**2)-4*a*c)>=0):
        return (-b+math.sqrt((b*b)-4*a*c))/(2*a),(-b-math.sqrt((b*b)-4*a*c))/(2*a)
    else:
        return "NU"
print(f3(a,b,c))
#4.
an=2012
def f4(an):
    if(an%4==0):
        if(an%100==0):
            if(an%400==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(f4(an))
#5.
x=0
def f5(x):
    if(x<-3):
        return 2*x+1
    if(x==-3):
        return 0
    if(x>-3):
        return 3*(x**2)+(6*x)-5
print(f5(x))
#6.
a=2
b=5
c=4
def f6(a,b,c):
    return max(a,b,c),max(min(a,b),min(b,c)),min(a,b,c)
print(f6(a,b,c))
#7.
def f7(a,b,c):
    return a<=c<=b
print(f7(a,b,c))
#8.
h1="08:00:00"
h2="08:10:01"
def f8(h1,h2):
    return (int(h2[0:2])-int(h1[0:2]))*3600+(int(h2[3:5])-int(h1[3:5]))*60+int(h2[6:8])-int(h1[6:8])
print(f8(h1,h2))
#9.
r=1
def f9(r):
    return 2*3.14*r,3.14*(r**2)
print(f9(r))
#10.
an1=2012
an2=2020
s=0
def f10(an1,an2,s):
    if(an1==an2):
        return s
    else:
        if(f4(an1==True)):
            return f10(an1+1,an2,s+366)
        else:
            return f10(an1+1,an2,s+365)
print(f10(an1,an2,s))