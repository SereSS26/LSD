#Lab3.
#1.
n=5
def f1(n):
    if(n==0):
        return 0
    else:
        return f1(n-1)+2
print(f1(n))
#2.
n=5
def f2(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    if(n>1):
        return f2(n-1)+f2(n-2)
print(f2(n))
#3.
def f3(n):
    if(n==0):
        return 0
    else:
        return f3(n-1)+n
print(f3(n))
#4.
n=123
def f4a(n):
    if(n==0):
        return 1
    else:
        return n%10*f4a(n//10)
print(f4a(n))
def f4b(n):
    if(n==0):
        return 0
    else:
        return 1+f4b(n//10)
print(f4b(n))
n=715326
def f4c(n):
    if(n==0):
        return 0
    else:
        return max(f4c(n//10),n%10)
print(f4c(n))
def f4d(n):
    if(n==0):
        return 0
    else:
        if(n%2==0):
            return 1+f4d(n//10)
        else:
            return f4d(n//10)
print(f4d(n))
#5.
n=4
a=2
def f5(n):
    if(n==0):
        return 1
    else:
        return a*f5(n-1)
print(f5(n))
#6.
n=4
d=n-1
def f6(d):
    if(d==1):
        return True
    else:
        if(n%d==0):
            return False
    return f6(d-1)
print(f6(d))
#7.
a=12
b=10
def f7(a,b):
    if(a%b==0 or b%a==0):
        return min(a,b)
    else:
        if(a>=b):
            return f7(a%b,b)
        else:
            return f7(a,b%a)
print(f7(a,b))
#8.
sir="Bat colegii rai"
def f8(sir):
    if(len(sir)==0):
        return ''
    else:
        return (sir[-1])+(f8(sir[0:len(sir)-1]))
print(f8(sir))
#10
n=5235465
c=5
def f10a(n):
    if(n==0):
        return False
    if(n%10==c):
        return True
    return f10a(n//10)
print(f10a(n))
def f10b(n):
    if(n==0):
        return 0
    if(n%10==c):
        return f10b(n//10)+1
    else:
        return f10b(n//10)
print(f10b(n))
#11.
n=123321
n2=str(n[::-1])
print(n2)

def f11(n):
    if(n==0):
        return True

