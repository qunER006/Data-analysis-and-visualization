

# data = []
goods = {}.fromkeys([line.rstrip() for line in open('goods_zh.txt','r',encoding='utf-8')])
with open('good.txt','w',encoding='utf-8') as f:
    for i in goods:
        # print(i[-1])
        if i[-1] == '1':
            f.write(" ".join(i) + "\n")   

with open('bad.txt','w',encoding='utf-8') as f:
    for i in goods:
        # print(i[-1])
        if i[-1] == '0':
            f.write(" ".join(i) + "\n") 