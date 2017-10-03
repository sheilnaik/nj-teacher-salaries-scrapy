# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NjteachersItem(scrapy.Item):
    first_name = scrapy.Field()
    last_name = scrapy.Field()
    salary = scrapy.Field()
    county = scrapy.Field()
    district = scrapy.Field()
    experience_district = scrapy.Field()
    school = scrapy.Field()
    experience_nj = scrapy.Field()
    primary_job = scrapy.Field()
    experience_total = scrapy.Field()
    experience_total = scrapy.Field()
    fte = scrapy.Field()
    subcategory = scrapy.Field()
    certificate = scrapy.Field()
    highly_qualified = scrapy.Field()
    teaching_route = scrapy.Field()
    
