import re
from collections import Counter

import os#读取当前目录下所有文件
import json

root = os.getcwd()+"\\json\\"
'''
#处理目录下所有文件的方法
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print("-----------")
        print(root)#os.walk()所在目录
        print(dirs)#os.walk()所在目录的所有目录名
        print(files)  #os.walk()所在目录的所有非目录文件名

file_name(root)
'''
load_dict=[]

for root, dirs, files in os.walk(root):
    for j in files:
        with open(".//json//"+j,'rb') as load_f:
            load_dict+= json.load(load_f)

    #print(load_dict)   
a=0
for obj in load_dict:
    a+=1
    #print(obj['paragraphs']) 
print(a)

dic = []
for i in load_dict:
    dic.append(str(i['paragraphs']).strip().replace('\'','').replace('\"','').replace('(','').replace(')','').replace('[','').replace(']','').replace('：','').replace('，','').replace('。','').replace('？','').replace('！','').replace('［','').replace('］',''))  #去除一些不用的符号
word = ''.join(dic)
word_str = re.sub(r"(?<=\w)","",word)  #把所有文字分开
word_list = list(word_str)
a = [v for v in word_list if not str(v).isdigit()]  #删除数字

c = Counter(a)
s = c.most_common(300)  #取了前300个最常见的汉字
tangshi = []
for i in s:
    tangshi.append(i[0])

import random
i = random.sample(tangshi,20)  #从300个最常见的汉字中拿出20个
print(i[0]+i[1]+i[2]+i[3]+i[4]+'，'+i[5]+i[6]+i[7]+i[8]+i[9]+'。'+'\n'+i[10]+i[11]+i[12]+i[13]+i[14]+'，'+i[15]+i[16]+i[17]+i[18]+i[19]+'。')

