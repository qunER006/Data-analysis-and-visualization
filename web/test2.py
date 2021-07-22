from snownlp import SnowNLP

# #保存情感极性值小于等于0.3的结果为负面情感结果
# f1=open('test.txt','w',encoding='utf-8')

# #保存情感极性值大于0.3的结果为正面情感结果
f2=open('test.txt','w',encoding='utf-8')

# l = {}.fromkeys([line.rstrip() for line in open('comments.txt','r',encoding='utf-8')])


f = open("comment.txt","r",encoding='utf-8')   #设置文件对象

l = f.readlines()  #直接将文件中按行读到list里，效果与方法2一样


# m = 0

# for j in l:
#     m += 1

# print(m)
for j in l:
    s=SnowNLP(j)
    print(s.sentiments)
    # f1.write(j+'\t'+str(s.sentiments)+'\n')
    f2.write(str(s.sentiments)+'\n')
    # else:
    #     f2.write(j + '\t' + str(s.sentiments) + '\n')
# f1.close()
f.close()             #关闭文件
f2.close()