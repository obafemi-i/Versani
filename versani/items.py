# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VersaniItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    product_link = scrapy.Field()
    price = scrapy.Field()
    style = scrapy.Field()
    size = scrapy.Field()
    metal = scrapy.Field()
    collection = scrapy.Field()
    finish = scrapy.Field()
    
