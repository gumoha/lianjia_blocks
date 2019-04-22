import scrapy
import time,random
from lianjia_blocks.items import LianjiaBlocksItem


class LjBlocks(scrapy.Spider):
    name = 'lj_blocks'
    allowed_domains = ['lianjia.com']
    lj_url = 'https://cd.lianjia.com'

    def start_requests(self):
        cd_esf_url =  'https://cd.lianjia.com/ershoufang/'
        yield scrapy.Request(cd_esf_url,callback=self.parse_district)

    # 获取区域
    def parse_district(self, response):
        # ['/ershoufang/jinjiang/', '/ershoufang/qingyang/']
        districts = response.xpath('//div[contains(@data-role,"ershoufang")]/div/a/@href').extract()
        dinums = 1
        for di in districts:
            di_url = self.lj_url + di
            time.sleep(random.random()*5)
            print('获取大区域链接', dinums, di_url)
            dinums += 1
            yield scrapy.Request(di_url, callback=self.parse_block)

    def parse_block(self, response):
        blocks = response.xpath('//div[contains(@data-role,"ershoufang")]/div/a/@href').extract()

        blnums = 1
        for bl in blocks:
            item = LianjiaBlocksItem()
            bl_url = self.lj_url + bl
            time.sleep(random.random() * 5)
            print('获取区域——街区链接', blnums, bl_url)
            blnums += 1
            item['block_url'] = bl_url
            yield item