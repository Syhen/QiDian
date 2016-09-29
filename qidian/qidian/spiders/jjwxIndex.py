# -*- coding:utf-8 -*-

import scrapy
from scrapy.selector import Selector
from qidian.items import JJWXIndex
import time

class JJWXIndexSpider(scrapy.Spider):
	"""
	"""
	name = 'jjwxindex'

	start_urls = ['http://www.jjwxc.net/bookbase.php?fw0=0&fbsj=3&ycx0=0&xx0=0&sd0=0&lx0=0&fg0=0&sortType=0&isfinish=0&collectiontypes=ors&searchkeywords=&page=1&sortType=3']
	def parse(self, response):
		sel = Selector(text = response.body.decode('gbk', 'ignore'))
		try:
			pages = int(sel.xpath('//*[@class="controlbar1"]/font[1]/text()').extract()[0])
		except IndexError:
			yield scrapy.FormRequest(
				response.url,
				dont_filter = True,
				callback = self.parse
			)
		for p in range(1, pages + 1):
			yield scrapy.FormRequest(
				'http://www.jjwxc.net/bookbase.php?fw0=0&fbsj=3&ycx0=0&xx0=0&sd0=0&lx0=0&fg0=0&sortType=0&isfinish=0&collectiontypes=ors&searchkeywords=&page=%s&sortType=3'%p,
				dont_filter = True,
				meta = {'page': p},
				callback = self.parse_index
			)

	def parse_index(self, response):
		p = response.meta['page']
		print p
		sel = Selector(text = response.body.decode('gbk', 'ignore'))
		datas = sel.xpath('//*[@class="cytable"]//tr')[1:]
		for data in datas:
			item = JJWXIndex()
			try:
				item['author'] = data.xpath('./td[1]/a/text()').extract()[0]
				# print item['author']
				item['author_url'] = 'http://www.jjwxc.net/' + data.xpath('./td[1]/a/@href').extract()[0]
				# print item['author_url']
			except IndexError:
				item['author'] = u'此作品无作者'
				item['author_url'] = u'此作品无作者链接'
			
			item['title'] = data.xpath('./td[2]/a/text()').extract()[0]
			# print item['title']
			item['title_url'] = 'http://www.jjwxc.net/' + data.xpath('./td[2]/a/@href').extract()[0]
			# print item['title_url']
			item['refresh_time'] = time.strftime('%Y-%m-%d %H:%M:%S')
			# print item['refresh_time']
			item['bid'] = item['title_url'].split('=')[-1]
			# print item['bid']
			item['relate_id'] = 'jjwx_%s'%item['bid']
			# print item['relate_id']
			item['source'] = 7
			# print item['source']
			try:
				item['first_time'] = data.xpath('./td[last()]/text()').extract()[0]
			except IndexError:
				item['first_time'] = u'此作品无首发时间'
			# print item['first_time']
			yield item