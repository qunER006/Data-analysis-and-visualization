import scrapy
from selenium.webdriver import common
from jingdong.items import JingdongItem
import re
from selenium import webdriver
import json
#scrapy crawl info

class InfoSpider(scrapy.Spider):
    name = 'info'
    start_urls = ['https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&pvid=dbcd8b016d5e4163bf37489ef0096c9f&psort=3']
    new_urls = []
    deep_urls = []
    id = []
    url = "https://item.jd.com/%s.html#comment"

    def parse(self, response):
        li_list = response.xpath('//*[@id="J_goodsList"]/ul/li')
        # p = response.xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[3]/strong/i/text()').extract()
        # print(p)
        for li in li_list:
            url = li.xpath('./div/div[@class="p-name p-name-type-2"]/a/@href').extract_first()
            # print(url)
            url = url.replace('/','',1)
            detail_url = 'https://item.jd.com/' + url + '#product-detail'
            # print(detail_url)
            id = re.findall(r"\d+\.?\d*",url)
            id = ''.join(id)
            id = id.replace('.','')
            # print(id)
            self.id.append(id)
        num = 1
        self.page_num = 0
        for i in self.id:
            item = JingdongItem()
            item["phoneID"] = num
            m = str(i)
            item["phonePrimid"] = i
            new_url = (self.url%m)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse_detail,meta={'item':item})
            num += 1


    def parse_detail(self, response):
        item = response.meta["item"]
        name = response.xpath('/html/body/div[6]/div/div[2]/div[1]/text()').extract()
        name = ''.join(name)
        print(name)
        base = response.xpath('/html/body/div[10]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]//text()').extract()
        base = ''.join(base)
        print(base)
        price = response.xpath('/html/body/div[6]/div/div[2]/div[4]/div/div[1]/div[2]/span[1]/span[2]//text()').extract()
        price = ''.join(price)
        print(price)
        item["phoneName"] = name
        item["phoneIntroduction"] = base
        item["phonePrice"] = price
        yield item