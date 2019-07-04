# Dict.py

s = {'1','2'} # 集合, 空集合定义用set()
print(s)


d = {'CHINA' : 'BEIJING', 'FRANCE': 'PAIRS'}
print(d)
print(d["CHINA"])


#print(type(s))
#print(type(d))
print('CN' in d) # 判断key
print(d.keys())
print(d.values())
print(d.items())

print(d.popitem()[0])


# setdefault
# If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.
d.setdefault('CHINA', 'TOKYO') 

print(d)
