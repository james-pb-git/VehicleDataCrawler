import os
import scrapy
from vehicle_data_crawler.items import *


class ModelSpider(scrapy.Spider):

    name = 'auto_data_generation'
    allowed_domains = 'auto-data.net/en'
    root = 'https://www.auto-data.net'

    def __init__(self):
        super().__init__()
        self.start_urls = ModelSpider.get_start_urls()

    @staticmethod
    def get_start_urls():
        root = os.getcwd()
        brand_file_name = root + '/vehicle_data_crawler/data/auto_data_model.csv'
        url_list = []
        first_line = True
        line_no = 0

        # Total number: 2662 (excluding first line)
        begin_line = 1001
        end_line = 2662

        with open(brand_file_name, 'r') as brand_file:
            for line in brand_file.readlines():
                if first_line:
                    first_line = False
                    continue
                url_list.append(line.strip('\r\n').split(',')[3])
                if not first_line:
                    line_no += 1
                    if line_no < begin_line:
                        continue
                    if line_no == end_line:
                        break
        return url_list

    def parse(self, response):
        for gen in zip(response.xpath('//table[@class="generr"]//th/a'),
                       response.xpath('//table[@class="generr"]//td/a')):
            gen_item = AutoDataGenItem()
            gen_item['parent_url'] = response.url
            gen_item['name'] = gen[0].xpath('@title')[0].extract().split("-")[0].strip()
            gen_item['url'] = self.root + gen[0].xpath('@href')[0].extract()
            gen_item['img'] = self.root + gen[0].xpath('img/@src')[0].extract()

            years = ''
            tmp1 = gen[1].xpath('strong[@class="cur"]/text()')
            tmp2 = gen[1].xpath('strong[@class="end"]/text()')
            if len(tmp1) > 0:
                years = tmp1[0].extract()
            elif len(tmp2) > 0:
                years = tmp2[0].extract()
            gen_item['years'] = years

            chassis = ''
            tmp = gen[1].xpath('strong[@class="chas"]/text()')
            if len(tmp) > 0:
                chassis = tmp[0].extract()
            gen_item['chassis']  = chassis

            desc = ''
            for item in gen[1].xpath('span/text()'):
                desc += (' | ' if len(desc) > 0 else '') + item.extract()
            gen_item['desc'] = desc

            yield gen_item
