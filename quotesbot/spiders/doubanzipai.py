# -*- coding: utf-8 -*-
import scrapy


from quotesbot.items import DoubanZipai


class DoubanZipaiSpider(scrapy.Spider):
    name = "doubanzipai"

    start_urls = [
        'https://www.douban.com/group/duqi/discussion?start=50',
    ]

    def parse(self, response):

        paths = response.xpath("//td[@class='title']/a/@href").extract()
        if len(paths) > 0:
            for path in paths:
                yield scrapy.Request(response.urljoin(path))
        else:
            urls = []
            for url in response.xpath("//div[@class='topic-figure cc']/img/@src").extract():
                urls.append(url)
            if len(urls) > 0:
                item = DoubanZipai()
                item['urls'] = urls
                item['name'] = response.xpath("//span[@class='from']/a/text()").extract_first()
                item['title'] = response.xpath("//div[@id='content']/h1/text()").extract_first()
                print("name"+item['name']+"\ntitle:"+ item['title'])
                # item['name'] = self.decodestr(item['name'])
                # item['title'] = self.decodestr(item['title'])
                yield item

    def decodestr(self, strs):

        if strs.startswith('\\u'):
            return strs.encode('utf-8').decode('unicode_escape')
        else:
            return strs