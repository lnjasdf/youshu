# -*- coding: utf-8 -*-
from youshu.items import YoushuItem
from youshu.db import sql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class YoushuPipeline(object):

    def process_item(self, item, spider):
        if type(item) is YoushuItem:
            session = sql.DBSession()
            info = sql.Info(book_id=item['book_id'], name=item['name'], author=item['author'],
                            words=item['words'], last_time=item['last_time'])
            session.add(info)
            session.commit()
            session.close()
        return item

