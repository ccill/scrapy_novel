# -*- coding: utf-8 -*-
import scrapy
from novel.items import NovelItem


class PapaPySpider(scrapy.Spider):
    name = 'papa.py'
    #allowed_domains = ['597txt.com']
    start_urls = ['https://www.597txt.com/files/article/html/108/108025/index.html']

    def parse(self, response):
        url_list=response.xpath('//div[@id="readerlist"]/ul/li/a/@href').extract()
        for url in url_list:
            yield scrapy.Request(url=response.urljoin(url),callback=self.after_parse)

    def after_parse(self,response):
        item=NovelItem()
        item['title']=response.xpath('//div[@class="title"]/h1/text()').extract_first()
        print(item['title'])
        item['text']=''.join(response.xpath('//div[@id="content"]/text()').extract()).replace('\xa0','').replace('\r\n','')
        #print(item['text'])        
        yield item
