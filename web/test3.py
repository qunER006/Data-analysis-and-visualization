import pymysql
#连接数据库
conn = pymysql.connect(host="47.94.95.145",
                           user="root",
                           password="123456",
                           db="Jingdong",
                           port=3306,
                           charset="utf8")
cursor = conn.cursor()
# l = {}.fromkeys([line.rstrip() for line in open('test1.txt','r',encoding='utf-8')])
# l = {}.fromkeys([line.rstrip() for line in open('score.txt','r',encoding='utf-8')])
f = open('test.txt', "r",encoding = 'utf-8')
# while True:
#逐行读取
    # line = f.readlines()
    # print(line)
    # print(1)
# f = open("score.txt","r",encoding='utf-8')   #设置文件对象

l = f.readlines()  #直接将文件中按行读到list里，效果与方法2一样

id = 1
for line in l:
#处理每行\n
    line = "".join(line)
    # line = line.strip('\n')
    # line = line.split(",")
    cont = line
    print(cont)
    print(2)
    
    cursor.execute(
        'update `jd comments` set user_senti = ("%s") where id = ("%d")'%(cont,id)
        # 'update `jd comments` set user_senti2 = ("%s") where id = ("%d")'%(cont,id)
    # 'insert into `exhibition info table`(muse_ID,exhib_Name) values("%s")'%(item["museumID"])
    )
    conn.commit()
    id += 1

 
# f.close()

conn.close()
cursor.close()
