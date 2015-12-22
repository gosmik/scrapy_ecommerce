from scrapy.spiders import Spider
from scrapy.selector import Selector

from gitti.items import gittiItem


class DmozSpider(Spider):
    name = "gitti"
    allowed_domains = ["gittigidiyor.com"]
    start_urls = [
        "http://www.gittigidiyor.com/arama/?satici=koyuncular"
    ]

    def parse(self, response):

        sel = Selector(response)
        sites = sel.select('//h4')
        items = []

        for site in sites:
            item = gittiItem()
            #item['name'] = site.select('a/text()').extract()
			# this is the first comment
            item['name'] = site.xpath('a/@href').extract()
            #item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(item)

        return items
