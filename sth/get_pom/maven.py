# 遍历生成maven的gav
# C:\Users\K\Desktop\xwiki10.11.3\xip

# python大法好!
import os
import urllib.parse

def list_all_files(rootdir):
    li = []

    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
        l = []

        temp = urllib.parse.unquote(list[i]).split(':') # 'get group:artifact'
        artifactId = temp[1]
        groupId = temp[0]

        l.append('<groupId>{}</groupId>'.format(groupId))
        l.append('<artifactId>{}</artifactId>'.format(artifactId))
        path = os.path.join(rootdir,list[i])
        version = urllib.parse.unquote(os.listdir(path)[0])
        l.append('<version>{}</version>'.format(version))
 
        li.append(l)
    return li

def wirte_list(li):
    f = open('pom.xml', 'w+')
    # 生成 部分 pom.xml
    for l in li:
        f.writelines('\t<dependency>\r')
        for j in l:
            f.writelines('\t\t{}\r'.format(j))
        f.writelines('\t</dependency>\r')


li = list_all_files('C:\\Users\\K\\Desktop\\xwiki10.11.3\\xip')
wirte_list(li)
