# CalHamlet.py

def getText():
    txt = open('hamlet.txt', 'r').read() #打开文件
    txt = txt.lower() #lowercase

    #for ch in '!"#$%()*+,-./:;<=>@[]\\^_{|}~'
    for ch in '~!@#$%^&*()_+-=[]{}|\\;:\'",<.>/?':
        txt = txt.replace(ch, ' ')
    return txt

hamlet = getText()
words = hamlet.split() # split 默认以空格切分

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

items = list(counts.items())
items.sort(key = lambda x:x[1], reverse = True)

for i in range(10):
    word, count = items[i]
   # print('{0:<10}{1:>5}'.format(word,count))
    print('{}\t{}'.format(word, count))
