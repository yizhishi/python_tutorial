#Test.py

'''
1
'''
'''
str = input()
print(str.replace(' ', ''))
'''

'''
2
关键行指一个文件中包含的不重复行。关键行数指一个文件中包含的不重复行的数量。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
统计附件文件中与关键行的数量
'''
'''
f = open('latex.log')
s = set()
for line in f.readlines():
    s.add(line)
else:
    print('共{}关键行'.format(len(s)))
'''

'''
3
读入一个字典类型的字符串，反转其中键值对输出。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
即，读入字典key:value模式，输出value:key模式。
用户输入的字典格式的字符串，如果输入不正确，提示：输入错误。
{"a": 1, "b": 2}                  {1: 'a', 2: 'b'}
'''
'''
#str = input()
str = '{"a": 1, "b": 2}'
newDict = {}
try:
    d = eval(str)
    for key in d.keys():
        newDict[d.get(key, '')] = key
    else:
        print(newDict)
except:
    print('输入错误')
'''

'''
4
附件是《沉默的羔羊》中文版内容，请读入内容，分词后输出长度大于2且最多的单词。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
如果存在多个单词出现频率一致，请输出按照Unicode排序后最大的单词。
'''
import jieba

f = open('沉默的羔羊.txt', 'rt', encoding='UTF-8')

s = f.read()
counts = {}

lt = jieba.cut(s)
#print(lt)
for i in lt:
    if len(i) > 2:
        counts[i] = counts.get(i, 0) + 1

else:
    lt = list(counts.items())
lt.sort(key = lambda x: x[1], reverse = True)

print(lt[0][0])








