# List.py

lt = []

lt +=[1,2,3,4,5] # 赋值

lt[1] = -1 # 修改第二个

lt.insert(1, 2) # 第二个位置添加元素

# 第一个位置删除元素
del lt[0]
lt.remove(lt[0]) 

lt = lt[3:] # 删除位置1~3的元素
'''
for i in range(3):
    lt.remove(lt[0])
'''

# 是否包含0
0 in lt
print('0在lt中出现的次数:{}'.format(lt.count(0)))
try:
    print(lt.index(0))
    print('包括')
except:
    print('不包括')

lt.append(0)

# 返回0的索引
lt.index(0)

print(len(lt)) # 返回长度

print(max(lt)) # 最大

lt.clear() # 清空
