import scrapy
from vehicle_data_crawler.items import BrandItem

# Copied from:
# https://github.com/LittleLory/codePool/blob/master/python/autohome_spider/autohome_spider/spiders/brand_spider.py


class BrandSpider(scrapy.Spider):
    name = 'brand'
    allowed_domains = 'autohome.com.cn'
    # start_urls = ['http://www.autohome.com.cn/grade/carhtml/%s.html' % chr(ord('A') + i) for i in range(26)]
    start_urls = ['http://www.autohome.com.cn/grade/carhtml/A.html']

    def parse(self, response):
        for brandPart in response.xpath('body/dl'):
            brand = BrandItem()
            brand['id'] = brandPart.xpath('@id')[0].extract()
            brand['url'] = brandPart.xpath('dt/a/@href')[0].extract()
            brand['name'] = brandPart.xpath('dt/div/a/text()')[0].extract()
            brand['pic'] = brandPart.xpath('dt/a/img/@src')[0].extract()
            yield brand
