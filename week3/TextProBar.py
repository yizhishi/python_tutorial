# TextProBar.py

# V1
import time as tm

scale = 10
'''
print('--start--')
for i in range(scale + 1):
    print('{}% \t [ {} -> {} ]'.format(i * 10, '*' * i, (scale - i) * '.'))
    tm.sleep(1 * 0.1)
print('--end--')
'''
# result
'''
--start--
0% 	 [  -> .......... ]
10% 	 [ * -> ......... ]
20% 	 [ ** -> ........ ]
30% 	 [ *** -> ....... ]
40% 	 [ **** -> ...... ]
50% 	 [ ***** -> ..... ]
60% 	 [ ****** -> .... ]
70% 	 [ ******* -> ... ]
80% 	 [ ******** -> .. ]
90% 	 [ ********* -> . ]
100% 	 [ ********** ->  ]
--end--
'''


# V2
'''
for i in range(101):
    print('\r{:3}%'.format(i), end = '')
    tm.sleep(1 * 0.1)
'''


# V3
start = tm.perf_counter()

for i in range(scale + 1):
    dur = tm.perf_counter() - start
    print('\r{}% \t [ {} -> {} ] {:.2f}s'.format(i * 10, '*' * i, (scale - i) * '.', dur), end = '')
    tm.sleep(1 * 0.1)

