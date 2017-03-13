# -*- coding: utf-8 -*-
import scrapy


class NamespiderSpider(scrapy.Spider):
    name = "NameSpider"
    allowed_domains = ["mydomain.com"]
    start_urls = (
        'http://www.mydomain.com/',
    )

    def parse(self, response):
        pass
