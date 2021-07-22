# from test import score
from flask import Flask, render_template
import jieba
import pymysql
# from gevent import pywsgi
from flask import request
import time
from wsgiref.simple_server import make_server
from collections import Counter
from flask import render_template
from flask import jsonify
from model import mysql
import logging
from gensim import corpora, models, similarities

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/l2')
def get_l2_data():
    words = []
    f = open("comments.txt","r",encoding='utf-8')   #设置文件对象
    l = f.readlines()
    for i in l:
        list = i.split()
        for j in list:
            words.append(j)
    c=Counter(words)
    common=c.most_common(15)
    d=dict(common)
    m = []
    for i in d:
        m.append(d[i])
    k = d.keys()
    n = []
    for i in k:
        n.append(i)
    # print(n)
    # print(m)
    return jsonify({"data": n,"count":m})   
    # data = utils.get_l2_data()
    # day, confirm_add, suspect_add = [], [], []
    # for a, b, c in data[7:]:
    #     day.append(a.strftime("%m-%d"))  # a是datatime类型
    #     confirm_add.append(b)
    #     suspect_add.append(c)
    # return jsonify({"day": day, "confirm_add": confirm_add, "suspect_add": suspect_add})

@app.route('/r2')
def get_r2_data():
    words = []
    f = open("comments.txt","r",encoding='utf-8')   #设置文件对象
    l = f.readlines()
    for i in l:
        list = i.split()
        for j in list:
            words.append(j)
    c=Counter(words)
    common=c.most_common(50)
    d=dict(common)
    # print(d)
    m = []
    for i in d:
        m.append(d[i])
    k = d.keys()
    n = []
    for i in k:
        n.append(i)
    rws = []
    dic  = {}
    for i in range(50):
        dic = {'name': n[i], 'value': str(m[i])}
        rws.append(dic)
    # print(rws)
    return jsonify({"rws": rws})   


@app.route('/r1')
def get_r1_data():
    data = mysql.get_info_data()
    # print(data)
    name = []
    name.append("name")
    price = []
    price.append("price")
    for i in data:
        name.append(i[0])
        price.append(i[1])
    setim = mysql.get_comment_data()
    star = []
    for i in setim:
        star.append(i[2])
    # print(star)
    pos = 0
    neg = 0
    for i in star:
        if i == 5:
            pos += 1
        else:
            neg += 1
    print(pos)
    print(neg)
    pos = pos - 234
    neg = neg + 234
    dic = {}
    arr = []
    dic = {'name': "pos", 'value': pos}
    # posarr.append('pos')
    arr.append(dic)
    # negarr = []
    dic = {'name': "neg", 'value': neg}
    # negarr.append('neg')
    # arr.append(dic)
    # print(name)
    # print(price)
    return jsonify({"name": name,"price": price,"arr":arr})   


@app.route('/c1')
def get_c1_data():
    data = mysql.get_info_data()
    # print(data)
    x = []
    m = []
    for i in data:
        m.append(i[2])
        m.append(i[0])
        x.append(m)
        m = []
    # print(x)
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    e = x[4]
    f = x[5]
    g = x[6]
    h = x[7]
    i = x[8]
    j = x[9]
    print(a,b,c,d)
    return jsonify({"d0": a,"d1": b,"d2": c,"d3": d,"d4": e,"d5": f,"d6": g,"d7": h,"d8": i,"d9": j})   




@app.route("/time")
def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
@app.route("/search",methods=["post"])
def search():
    query=request.values.get('input')
    query=jieba.lcut(query)
    temp=''
    for q in query:
        temp+=q
        temp+=' '
    comments=similarity(datapath, temp, storepath)
    print(comments)
    return jsonify({"comments":comments})
# ----------------------------------------
datapath = 'comments.txt'
# querypath = 'query.txt'
storepath = 'store.txt'
def similarity(datapath, query, storepath):
    conn = pymysql.connect(
        host='47.94.95.145',
        user='root',
        password='123456',
        database='Jingdong',
        port=3306,
        autocommit=True
    )
    cur = conn.cursor()
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    class MyCorpus(object):
        def __iter__(self):
            for line in open(datapath,'rb'):
                yield line.split()

    Corp = MyCorpus()
    dictionary = corpora.Dictionary(Corp)
    corpus = [dictionary.doc2bow(text) for text in Corp]

    tfidf = models.TfidfModel(corpus)

    corpus_tfidf = tfidf[corpus]

    # q_file = open(querypath, 'rb')
    # query = q_file.readline()
    # q_file.close()
    vec_bow = dictionary.doc2bow(query.split())
    vec_tfidf = tfidf[vec_bow]

    index = similarities.MatrixSimilarity(corpus_tfidf)
    sims = index[vec_tfidf]

    similarity = list(sims)

    sim_file = open(storepath, 'w')

    mini=[]   #相似度最大的前五条评论的相似度
    n=[]    #相似度最大的评论中最低的评论的下标
    rank=[]   #相似度最大的评论的下标
    minn=0  #当前准备被替换的下标
    sum=0

    for i in similarity:
        sim_file.write(str(i)+'\n')
        if len(rank)<5:
            rank.append(sum)
            mini.append(i)
            #if i<min(mini):
             #   minn=sum
            #minn=min(mini)
            n.append(sum)
            ttmp = min(mini)
            for j in mini:
                if j == ttmp:
                    res = mini.index(j)
            minn = n[res]
        else:
            tmp=min(mini) #前五中最小的相似度
            if i>tmp:
                rank.remove(minn)
                rank.append(sum)
                for j in mini:
                    if j==tmp:
                        res=mini.index(j)
                mini[res]=i
                n[res]=sum
                ttmp=min(mini)
                for j in mini:
                    if j==ttmp:
                        res=mini.index(j)
                minn=n[res]
                #mini.remove(tmp)
                #mini.append(i)
                #minn=sum

        sum+=1
        '''print(mini)
        print(n)
        print(rank)
        print(minn)'''
    sim_file.close()
    with open(datapath, 'r',encoding='utf-8') as fi:
        docs = fi.read().splitlines()  # These are all cleaned out
        fi.close()
    comments = ''
    for i in rank:
        print(i)
        comments_sqli="select phone_id,user_content from `jd comments` where id="+str(i+1)+";"
        cur.execute(comments_sqli)
        results = cur.fetchall()
        phone_id=results[0][0]
        phone_comment=results[0][1]+'\n'
        comments_sqli = "select phone_name from `jd info` where phone_id="+str(phone_id)+";"
        cur.execute(comments_sqli)
        results=cur.fetchall()
        phone_name=results[0][0]+'\n'
        comments+=phone_name
        comments+=phone_comment
        comments+='------------------------------------------------------\n'
    conn.close()
    return comments


if __name__ == '__main__':
    #运行Flask应用(启动Flask的服务)，默认在本机开启的端口号是5000.
    #debug=True,是将当前的启动模式改为调试模式(开发环境中建议使用调试模式，生产环境中不允许使用)
    server = make_server('127.0.0.1',5000,app)
    server.serve_forever()
    app.run(debug=True)
    # get_c1_data()