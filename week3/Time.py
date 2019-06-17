# Time.py
import time as tm


t = tm.time()
print(t)
print(tm.ctime())
print(tm.gmtime())

t = tm.gmtime()
print(tm.strftime('%Y-%m-%d %H:%M:%S',t)) # gmtime to string

timeStr = '2019-06-17 14:15:34'
print(tm.strptime(timeStr, '%Y-%m-%d %H:%M:%S')) # string to gmtime


# time counter
start = tm.perf_counter()

tm.sleep(5) # 休眠 单位s

end = tm.perf_counter()

print(end - start)  # 计时 5s

