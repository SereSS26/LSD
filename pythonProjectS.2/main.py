set1={1,3,1,4,8,9}
def subset(set1,con):
    el=set1.pop()
    if(con(el)==False):
        return subset(set1,con)
    else:
        set1.add(el)
        return set1
print(subset(set1,lambda x:x>3))

import functools
set2=set()
def subset(set1,con):
    def f2(acc,el):
        if(con(el)==True):
            set2.add(el)
        return acc
    return functools.reduce(f2,set1,set2)
print(subset(set1,lambda x:x>3))
