# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs,json
from datetime import datetime


class LianjiaBlocksPipeline(object):
    def open_spider(self,spider):
        filen = '/media/gumoha/资料/Scrapy/lianjia_blocks/{0}.json'.format('Chengdu_blocks')
        self.file = codecs.open(filen,'w')

    def close_spider(self,item,spider):
        self.file.close()

    def process_item(self, item, spider):
        #time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        line = '{0}\n'.format(json.dumps(dict(item)))
        self.file.write(line)

        return item
