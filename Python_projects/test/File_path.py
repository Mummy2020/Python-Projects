
import os


fName = 'test2.txt'

fPath = 'C:\\test\\'

abPath = os.path.join(fPath, fName)
print(abPath)


print(os.listdir(fPath))
source_files = os.listdir(fPath)
for i in source_files:
    if i.endswith('.txt'):
        print(i)
        print(os.path.getmtime(abPath))


