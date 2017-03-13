# -*- coding: utf-8 -*-

from scrapy import cmdline

# spider name
name = "NameSpider"
# save to mysql
cmd = "scrapy crawl {0}".format(name)
# save to file
cmd2 = "scrapy crawl {0} -o {0}.csv".format(name)

cmdline.execute(cmd2.split())
