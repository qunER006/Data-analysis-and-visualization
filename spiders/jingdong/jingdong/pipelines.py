# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from pymysql.converters import escape_string


class JingdongPipeline:

    conn = None
    cursor = None
    def open_spider(self,spider):
        #连接数据库
        self.conn = pymysql.Connect(host='47.94.95.145',user = 'root',port = 3306,password = '123456',db = 'Jingdong',charset = 'utf8')
        # print(1)
    def process_item(self,item,spider):
        #创建cursor对象
        self.cursor = self.conn.cursor()
        #错误判断
        try:
            #通过excute用sql语句操作数据库
            print(spider.name)
            if spider.name == "comments":
                self.cursor.execute('insert into `jd comments`(user_id,phone_id,user_content,user_score,user_time) values("%s","%d",\"%s\","%d","%s")'%(item["userID"],item["phoneID"],escape_string(item["userComments"]),item["userScore"],item["commTime"]))
                self.conn.commit()
            elif spider.name == "info":
                self.cursor.execute('delete from `jd info `(phone_id,phone_name,phone_intro,phone_price,phone_primid) values("%s",\"%s\",\"%s\","%s","%s")'%(item["phoneID"],escape_string(item["phoneName"]),escape_string(item["phoneIntroduction"]),item["phonePrice"],item["phonePrimid"]))
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
