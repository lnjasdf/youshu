# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YoushuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_id = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    words = scrapy.Field()
    last_time = scrapy.Field()


if __name__ == '__main__':
    item = YoushuItem()
    item['book_id'] = 111
    item['name'] = 'aaa'
    item['author'] = 'bbb'
    item['words'] = 'ccc'
    item['last_time'] = 'ddd'
    print item
    print dict(item)

