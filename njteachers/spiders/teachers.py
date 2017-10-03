# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from njteachers.items import NjteachersItem
import logging
from scrapy.utils.log import configure_logging

configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.INFO
)

class TeachersSpider(CrawlSpider):
    # https://medium.com/towards-data-science/using-scrapy-to-build-your-own-dataset-64ea2d7d4673
    name = 'teachers'
    # allowed_domains = ['http://php.app.com/']
    start_urls = ['http://php.app.com/agent/educationstaff/search']

    number_of_pages = 13873

    # This mimics getting the pages using the next button. 
    for i in range(2, number_of_pages + 1):
        start_urls.append('http://php.app.com/agent/educationstaff/search/page:' + str(i))

    rules = (
        Rule(LinkExtractor(allow=('details\/\d+')), callback='parse_teacher_data'),
        )

    def parse_teacher_data(self, response):
        page_elements = response.css('div[class="col-md-8 details-field-value"]>p::text').extract()
        item = NjteachersItem()

        item['first_name'] = page_elements[0]
        item['last_name'] = page_elements[1]
        item['salary'] = int(re.sub("\$|,", "", page_elements[2]))
        item['county'] = page_elements[3]
        item['district'] = page_elements[4]
        item['experience_district'] = page_elements[5]
        item['school'] = page_elements[6]
        item['experience_nj'] = page_elements[7]
        item['primary_job'] = page_elements[8]
        item['experience_total'] = page_elements[9]
        item['experience_total'] = page_elements[9]
        item['fte'] = page_elements[10]
        item['subcategory'] = page_elements[11]
        item['certificate'] = page_elements[12]
        item['highly_qualified'] = page_elements[13]
        item['teaching_route'] = page_elements[14]

        yield item