# -*- coding: utf-8 -*-
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
import os

class MusicsheetImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url, order in zip(item['image_urls'], item['image_order']):
            yield Request(image_url, meta={'order':order,'name':item['sheet_name']})

    def file_path(self, request, response=None, info=None):
        pg_num = request.meta['order']
        name = request.meta['name']
        return '{}/page{}.jpg'.format(name,str(pg_num).zfill(3))

class MusicsheetItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_order = scrapy.Field()
    sheet_name = scrapy.Field()
    pass

class MusicsheetSpider(scrapy.Spider):
    name = "sheetmusic"
    allowed_domains = ["m.hqgq.com"]
    custom_settings = {
        'ITEM_PIPELINES': {
            'crawlsheet.MusicsheetImagePipeline': 1
        },
        'IMAGES_STORE':os.path.join(os.getcwd(),'musicsheet','sheet_img')
    }

    def __init__(self, url='http://m.hqgq.com/qinpu/25970.html'):
        super().__init__()
        self.start_urls=[url]

    def parse(self, response):
        sheet = MusicsheetItem()
        #Image url need to be absolute path
        sheet['image_urls'] = response.xpath('//div[@class="qupucont"]/img/@src').extract()[:1]
        sheet['image_order'] = list(range(1,len(sheet['image_urls'])+1))
        sheet['sheet_name'] = response.xpath('//h1/text()').extract()[-1]
        return sheet