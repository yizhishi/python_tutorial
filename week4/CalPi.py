# CalPi.py 

import random
import time

'''print(random.seed(10))

for i in range(10):
    print(random.random())
print('--------------')

random.seed(10)
for i in range(10):
    print(random.random())

for i in range(10):
    print(random.randrange(10,31,10))
'''

# 公式计算
max = 1000 # 1, 000
start = time.perf_counter()

pi = 0
for k in range(max):
    pi += 1 / pow(16, k) \
            * \
                ( \
                    4/ (8 * k + 1) - 2/ (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6) \
                )

print('公式方法计算的PI: {}'.format(pi))
print('公式方法计算耗时: {}'.format(time.perf_counter() - start))


# 蒙特卡洛方法. 撒点, 落在单位圆内, 与落在x=±1, y=±1围成的正方形
max = 1000 * 1000 * 10 # 1, 000, 000
start = time.perf_counter()
inCircle = 0
for i in range(max):
    # 获取x, y坐标
    x = random.random()
    y = random.random()
    s = pow( (pow(x, 2) + pow(y, 2)) , 0.5)
    if s<= 1:
        inCircle = inCircle + 1
pi = (inCircle / max) * 4
print('蒙特卡洛方法计算的PI: {}'.format(pi))
print('蒙特卡洛方法计算耗时: {}'.format(time.perf_counter() - start))
