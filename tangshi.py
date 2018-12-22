import re
from collections import Counter

import json


with open(".//json//poet.tang.15000.json",'rb') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)
#load_dict['paragraphs'] = [8200,{1:[['Python',81]]}]
#print(load_dict)

#with open(".//json//poet.tang.15000.json","w") as dump_f:
 #   json.dump(load_dict,dump_f)



dic = []
data = open('..//..//datasets//tangshi//biansaishi.txt','r')  #下载的唐诗三百首tangshi.txt

for i in data.readlines():
    dic.append(i.strip().replace('：','').replace('，','').replace('。','').replace('？','').replace('！','').replace('［','').replace('］',''))  #去除一些不用的符号
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
