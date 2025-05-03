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