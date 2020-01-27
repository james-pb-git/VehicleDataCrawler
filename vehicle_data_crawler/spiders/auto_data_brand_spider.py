import scrapy
from vehicle_data_crawler.items import *


class BrandSpider(scrapy.Spider):
    name = 'auto_data_brand'
    allowed_domains = 'auto-data.net/en'
    # start_urls = ['http://www.autohome.com.cn/grade/carhtml/%s.html' % chr(ord('A') + i) for i in range(26)]
    start_urls = ['https://www.auto-data.net/en/allbrands']
    root = 'https://www.auto-data.net'

    def parse(self, response):
        for brand in response.xpath('/html/body/div[2]/div/a[@class="marki_blok"]'):
            brand_item = AutoDataBrandItem()
            brand_item['name'] = brand.xpath('@title')[0].extract().split(" ")[0]
            brand_item['url'] = self.root + brand.xpath('@href')[0].extract()
            brand_item['img'] = self.root + brand.xpath('img/@src')[0].extract()

            yield brand_item
