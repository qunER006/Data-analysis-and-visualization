# scrapy crawl comments
import scrapy
from selenium.webdriver import common
from jingdong.items import JingdongItem,CommItem
import re
from selenium import webdriver
import json

class CommentsSpider(scrapy.Spider):
    name = 'comments'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&pvid=dbcd8b016d5e4163bf37489ef0096c9f&psort=3']
    new_urls = []
    deep_urls = []
    id = []
    page_num = 0
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=%s&score=%d&sortType=5&page=%d&pageSize=10&isShadowSku=0&fold=1'



    def parse(self, response):
        li_list = response.xpath('//*[@id="J_goodsList"]/ul/li')
        # p = response.xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[3]/strong/i/text()').extract()
        # print(p)
        for li in li_list:
            url = li.xpath('./div/div[@class="p-name p-name-type-2"]/a/@href').extract_first()
            # print(url)
            # url = url.replace('/','',1)
            # detail_url = 'https://item.jd.com/' + url + '#comment'
            # print(detail_url)
            id = re.findall(r"\d+\.?\d*",url)
            id = ''.join(id)
            id = id.replace('.','')
            # print(id)
            self.id.append(id)
            # print(self.id)
            # self.deep_urls.append(detail_url)
            # yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        print(self.id)



        num = 1
        for i in self.id:
            self.page_num = 0
            m = str(i)
            while self.page_num <= 30:
                item = CommItem()
                item["phoneID"] = num
                new_url = (self.url%(m,3,self.page_num))
                self.page_num += 1
                yield scrapy.Request(new_url,callback=self.parse_detail,meta={'item':item})
            while self.page_num <= 40:
                item = CommItem()
                item["phoneID"] = num
                new_url = (self.url%(m,1,self.page_num))
                self.page_num += 1
                yield scrapy.Request(new_url,callback=self.parse_detail,meta={'item':item})
            num += 1
        # m = "100011414185"
        # num = 26
        # self.page_num = 0
        # while self.page_num <= 30:
        #     item = CommItem()
        #     item["phoneID"] = num
        #     new_url = (self.url%(m,3,self.page_num))
        #     self.page_num += 1
        #     yield scrapy.Request(new_url,callback=self.parse_detail,meta={'item':item})
        # while self.page_num <= 40:
        #     item = CommItem()
        #     item["phoneID"] = num
        #     new_url = (self.url%(m,1,self.page_num))
        #     self.page_num += 1
        #     yield scrapy.Request(new_url,callback=self.parse_detail,meta={'item':item})
        # num += 1
    
    def parse_detail(self, response):
        item = response.meta["item"]
        # comment_list = json.loads(response.text)["comments"]
        data = response.text
        jd = json.loads(data.lstrip('fetchJSON_comment98vv12345(').rstrip(');'))
        data_list = jd['comments']
        for i in data_list:
            user_id = i["id"]
            content = i["content"]
            score = i["score"]
            time = i["creationTime"]
            # print(user_id)
            # print(content)
            # print((score,time))
            item["userComments"] = content
            item["commTime"] = time
            item["userID"] = user_id
            item["userScore"] = score
            yield item
