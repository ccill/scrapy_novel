# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NovelPipeline(object):
    def process_item(self, item, spider):
        self.file.write(item['title']+'\n')
        self.file.write(item['text']+'\n')
        return item

    def open_spider(self,spider):
        self.file=open('乡村小坏蛋.txt','a',encoding='utf-8')

    def close_spider(self,spider):
        self.file.close()
