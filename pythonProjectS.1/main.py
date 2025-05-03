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
