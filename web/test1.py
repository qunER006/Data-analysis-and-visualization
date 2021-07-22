from nltk.probability import  FreqDist,ConditionalFreqDist
  
from nltk.metrics import  BigramAssocMeasures

import nltk
  
from nltk.collocations import  BigramCollocationFinder
  
from nltk.metrics import  BigramAssocMeasures

import jieba

import sklearn
  
from nltk.classify.scikitlearn import  SklearnClassifier
  
from sklearn.svm import SVC, LinearSVC,  NuSVC
  
from sklearn.naive_bayes import  MultinomialNB, BernoulliNB
  
from sklearn.linear_model import  LogisticRegression
  
from sklearn.metrics import  accuracy_score

from random import shuffle

import pickle
  
#获取文本字符串
  
def text():
  
    f1 = open('good.txt','r',encoding='utf-8')

    f2 = open('bad.txt','r',encoding='utf-8')

    line1 = f1.readline()

    line2 = f2.readline()

    str = ''

    while line1:

        str += line1

        line1 = f1.readline()

    while line2:

        str += line2

        line2 = f2.readline()

    f1.close()

    f2.close()

    return str
    

def read_file(filename):
  
    stop = [line.strip() for line in  open('stopword.txt','r',encoding='utf-8').readlines()]#停用词

    f = open(filename,'r',encoding='utf-8')

    line = f.readline()

    str = []

    while line:

        s = line.split('\t|\n')

        fenci = jieba.lcut(s[0])#False默认值：精准模式

        str.append(list(set(fenci)-set(stop)))

        line = f.readline()

    return str
  
def jieba_feature(number):   
  
     posWords = []
  
     negWords = []
  
     for items in read_file('good.txt'):#把集合的集合变成集合
  
         for item in items:
  
            posWords.append(item)
  
     for items in read_file('bad.txt'):
  
         for item in items:
  
            negWords.append(item)
  
  
     word_fd = FreqDist() #可统计所有词的词频
  
     cond_word_fd = ConditionalFreqDist() #可统计积极文本中的词频和消极文本中的词频
  
     for word in posWords:
  
         word_fd[word] += 1
  
         cond_word_fd['pos'][word] += 1
  
     for word in negWords:
  
         word_fd[word] += 1
  
         cond_word_fd['neg'][word] += 1
  
  
     pos_word_count = cond_word_fd['pos'].N() #积极词的数量
  
     neg_word_count = cond_word_fd['neg'].N() #消极词的数量
  
     total_word_count = pos_word_count + neg_word_count
  
  
     word_scores = {}#包括了每个词和这个词的信息量
  
     for word, freq in word_fd.items():
  
         pos_score = BigramAssocMeasures.chi_sq(cond_word_fd['pos'][word],  (freq, pos_word_count), total_word_count) #计算积极词的卡方统计量，这里也可以计算互信息等其它统计量
  
         neg_score = BigramAssocMeasures.chi_sq(cond_word_fd['neg'][word],  (freq, neg_word_count), total_word_count) #同理
  
         word_scores[word] = pos_score + neg_score #一个词的信息量等于积极卡方统计量加上消极卡方统计量
  
  
     best_vals = sorted(word_scores.items(), key=lambda item:item[1],  reverse=True)[:number] #把词按信息量倒序排序。number是特征的维度，是可以不断调整直至最优的
  
     best_words = set([w for w,s in best_vals])
  
     return dict([(word, True) for word in best_words])
  
  
def build_features():
  
    feature = jieba_feature(300)#结巴分词

    posFeatures = []

    for items in read_file('good.txt'):

        a = {}

        for item in items:

            if item in feature.keys():

                a[item]='True'

        posWords = [a,'pos'] #为积极文本赋予"pos"

        posFeatures.append(posWords)


    negFeatures = []

    for items in read_file('bad.txt'):

        a = {}

        for item in items:

            if item in feature.keys():

                a[item]='True'

        negWords = [a,'neg'] #为消极文本赋予"neg"

        negFeatures.append(negWords)
    
    noFeatures = []

    for items in read_file('comment.txt'):

        a = {}

        for item in items:

            if item in feature.keys():

                a[item]='True'

        noWords = [a,'no'] #为积极文本赋予"pos"

        noFeatures.append(noWords)


    return posFeatures,negFeatures,noFeatures

  
posFeatures,negFeatures,noFeatures =  build_features()#获得训练数据
  
  

  
shuffle(posFeatures) #把文本的排列随机化
  
shuffle(negFeatures) #把文本的排列随机化
  
  
train =  posFeatures[20000:]+negFeatures[20000:]#训练集(80%)
  
test = posFeatures[:20000]+negFeatures[:20000]#预测集(验证集)(20%)
  
data,tag = zip(*test)#分离测试集合的数据和标签，便于验证和测试

data,tag = zip(*noFeatures)#分离测试集合的数据和标签，便于验证和测试


  
  
def score(classifier):
  
    classifier = SklearnClassifier(classifier) #在nltk中使用scikit-learn的接口

    classifier.train(train) #训练分类器


    # pred = classifier.classify_many(data) #对测试集的数据进行分类，给出预测的标签

    pred = classifier.classify_many(data) #对测试集的数据进行分类，给出预测的标签

    n = 0

    s = len(pred)

    for i in range(0,s):

        # print(pred[i],tag[i])

        if pred[i]==tag[i]:

            n = n+1
    # print(n)

    return n/s #对比分类预测结果和人工标注的正确结果，给出分类器准确度
  
  
# print('BernoulliNB`s accuracy is %f'  %score(BernoulliNB()))
  
# print('MultinomiaNB`s accuracy is %f'  %score(MultinomialNB()))
  
# print('LogisticRegression`s accuracy is  %f' %score(LogisticRegression()))
  
# print('SVC`s accuracy is %f'  %score(SVC()))
  
# print('LinearSVC`s accuracy is %f'  %score(LinearSVC()))
  
# print('NuSVC`s accuracy is %f'  %score(NuSVC()))




trainset = posFeatures[0:]+negFeatures[0:]

LinearSVC_classifier = SklearnClassifier(LinearSVC())
# LinearSVC_classifier = SVC(kernel='linear',probability=True)
LinearSVC_classifier.train(trainset)
pickle.dump(LinearSVC_classifier, open('classifier.pkl','wb'))


clf = pickle.load(open('classifier.pkl','rb')) #载入分类器

# pred = clf.prob_classify_many(data) #该方法是计算分类概率值的
pred = clf.classify_many(data)
p_file = open('score1.txt','w') #把结果写入文档
for i in pred:
    # print(i)
    # p_file.write(str(i.prob('pos')) + ' ' + str(i.prob('neg')) + '\n')
    p_file.write(str(i) + '\n')
p_file.close()