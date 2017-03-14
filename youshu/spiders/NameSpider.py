# -*- coding: utf-8 -*-
import scrapy
from youshu.items import YoushuItem
import time
import random
from youshu.logger import *
from youshu import config


class NameSpider(scrapy.Spider):
    name = "NameSpider"
    # allowed_domains = ["mydomain.com"]
    # start_urls = (
    #     'http://www.yousuu.com/category/all?page=2',
    # )

    start_url = 'http://www.yousuu.com/category/all?page='

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        yield scrapy.Request(self.start_url + str(config.START_PAGE), headers=self.headers)

    def parse(self, response):
        logger.info(response.url)
        books = response.xpath('//div[@class="booklist-item"]')
        for book in books:
            item = NameSpider.build_item(book)
            yield item
        url = NameSpider.next_url(response)
        if url is not None:
            yield scrapy.Request(url, headers=self.headers)

    @staticmethod
    def build_item(book):
        item = YoushuItem()
        item['name'] = book.xpath('.//div[@class="title"]/a/text()').extract()[0]
        link = book.xpath('.//div[@class="title"]/a/@href').extract()[0]
        item['book_id'] = int(link[6:])
        info = book.xpath('.//div[@class="abstract"]/text()').extract()
        item['author'] = info[0]
        item['words'] = info[1]
        item['last_time'] = info[2]
        return item

    @staticmethod
    def next_url(response):
        next_script = response.xpath('//ul[@class="pagination pull-right"]/li[last()]/a/@onclick').extract()[0]
        last_page = int(next_script[next_script.find(',') + 1:next_script.find(')')])
        current_page = int(response.url[response.url.find('=') + 1:])
        if current_page == 5:  # TODO 测试5页
            return None
        if current_page < last_page:
            second = random.randint(2, 10)  # 爬一页随机休息
            logger.info("sleep: %d" % (second,))
            time.sleep(second)
            return NameSpider.start_url + str(current_page + 1)
        return None
