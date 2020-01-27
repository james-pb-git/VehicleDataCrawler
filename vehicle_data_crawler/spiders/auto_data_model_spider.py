import os
import scrapy
from vehicle_data_crawler.items import *


class ModelSpider(scrapy.Spider):

    name = 'auto_data_model'
    allowed_domains = 'auto-data.net/en'
    root = 'https://www.auto-data.net'

    def __init__(self):
        super().__init__()
        self.start_urls = ModelSpider.get_start_urls()

    @staticmethod
    def get_start_urls():
        root = os.getcwd()
        brand_file_name = root + '/vehicle_data_crawler/data/auto_data_brand.csv'
        url_list = []
        first_line = True
        with open(brand_file_name, 'r') as brand_file:
            for line in brand_file.readlines():
                if first_line:
                    first_line = False
                    continue
                url_list.append(line.strip('\r\n').split(',')[2])
        return url_list

    def parse(self, response):
        for model in response.xpath('//a[@class="modeli"]'):
            model_item = AutoDataModelItem()
            model_item['parent_url'] = response.url
            model_item['name'] = model.xpath('@title')[0].extract().split("-")[0].strip()
            model_item['url'] = self.root + model.xpath('@href')[0].extract()
            model_item['img'] = self.root + model.xpath('img/@src')[0].extract()

            yield model_item
