# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#手机的基础信息
class JingdongItem(scrapy.Item):
    phoneID = scrapy.Field()   
    phoneName = scrapy.Field() 
    phoneIntroduction = scrapy.Field()
    phonePrice = scrapy.Field()
    phonePrimid = scrapy.Field()


class CommItem(scrapy.Item):
    phoneID = scrapy.Field()   
    userComments = scrapy.Field()
    commTime = scrapy.Field() 
    userID = scrapy.Field()
    userScore = scrapy.Field()