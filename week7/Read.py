'''f= open('hamlet.txt' , 'rt')

for line in f. readlines():
    print(line)
f.close
'''



f = open('test.txt', 'w+')

ls = ['A', '2']

f.writelines(ls) # TypeError: write() argument must be str, not int
                        # write() argument must be str, not list

f.seek(0)
for line in f:
    print(line)

f.close()
