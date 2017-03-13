# -*- coding: utf-8 -*-
import scrapy
from youshu.items import YoushuItem


class NameSpider(scrapy.Spider):
    name = "NameSpider"
    # allowed_domains = ["mydomain.com"]
    # start_urls = (
    #     'http://www.yousuu.com/category/all?page=2',
    # )

    start_url = 'http://www.yousuu.com/category/all?page=2'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        yield scrapy.Request(self.start_url, headers=self.headers)

    def parse(self, response):
        books = response.xpath('//div[@class="booklist-item"]')
        for book in books:
            item = NameSpider.build_item(book)
            yield item

    @staticmethod
    def build_item(book):
        item = YoushuItem()
        item['name'] = book.xpath('.//div[@class="title"]/a/text()').extract()[0]
        item['link'] = book.xpath('.//div[@class="title"]/a/@href').extract()[0]
        info = book.xpath('.//div[@class="abstract"]/text()').extract()
        item['author'] = info[0]
        item['words'] = info[1]
        item['last_time'] = info[2]
        return item
