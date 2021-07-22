import jieba
import sys

from pymysql import NULL
sys.path.append(".")
# print(sys.path)
from model import mysql
import re

res = mysql.get_comment_data()
data = []
stopwords = {}.fromkeys([line.rstrip() for line in open('stopword.txt','r',encoding='utf-8')])
with open('comment.txt','w') as f:
    for i in res:
        s = ''
        m = re.split(r'\t|\n|\r|\\s|&hellip|&ldquo|&rdquo|&nbsp|&bull|&nbsp',i[1])
        n = i[3]
        for j in m:
            s = s + str(j)
        seg_list = jieba.lcut(s)
        # print(seg_list)
        s = ''
        for w in seg_list:
            if w not in stopwords and w != ' ':
                s = s + str(w)
        if s == '':
            s = '差不好 '
        print(s)
        # f.write(" ".join(jieba.lcut(s)) + "\n")    # 精简模式，返回一个列表类型的结果
        f.write(" ".join(m) + "\n")

# print("/".join(jieba.lcut(seg_str, cut_all=True)))      # 全模式，使用 'cut_all=True' 指定 
# print("/".join(jieba.lcut_for_search(seg_str)))     # 搜索引擎模式
