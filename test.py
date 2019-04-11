import os
import re
filepath="C:\\Users\\Administrator\\Desktop\\Python\\demolist"
demolist=os.listdir(filepath)     #储存文件夹目录下所有文件名到demolist中
print(demolist)

for demo in demolist:
    mapname=re.findall(r'(.+?)\_shNz',demo)
    print(mapname)