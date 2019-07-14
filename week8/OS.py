#OS.py
import os.path as op
import os

txt = 'C:\d2f42068.ini'
print(op.basename(txt))
print(op.getatime(txt))
print(op.exists(txt))


print(op.isfile(txt))
print(op.isdir(txt))


print(op.getatime(txt)) # access time
print(op.getmtime(txt)) # modify time
print(op.getctime(txt)) # create time

print(op.getsize(txt))

 
#os.system('eclipse.exe')

#os.system('mspaint.exe   C:\\Users\\K\\Pictures\\test1\\5.png')
 
print(os.cpu_count()) # cpu core count
