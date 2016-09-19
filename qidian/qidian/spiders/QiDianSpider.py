# -*- coding:utf-8 -*-

import scrapy
from scrapy.selector import Selector
from qidian.items import QidianItem
import time
import math

class QiDianSpider(scrapy.Spider):
	"""
	"""
	name = 'qidianindex'

	start_urls = [
		'http://a.qidian.com/?size=-1&sign=-1&tag=-1&chanId=-1&subCateId=-1&orderId=&page=1&month=3&style=1&action=-1&vip=-1'
	]

	def parse(self, response):
		print response.url
		sel = Selector(text = response.body)
		pages = int(math.ceil(int(sel.xpath('//*[@class="count-text"]/span/text()').extract()[0]) / 20))#总页数
		print u'总页数', pages
		for i in range(1, pages + 1):
			yield scrapy.FormRequest(
				'http://a.qidian.com/?size=-1&sign=-1&tag=-1&chanId=-1&subCateId=-1&orderId=&page={0}&month=3&style=1&action=-1&vip=-1'.format(i),
				dont_filter = True,
				meta = {
					'page': i
				},
				callback = self.getUrls
			)

	def getUrls(self, response):#解析页面，获取索引信息
		print response.url
		sel = Selector(text = response.body)
		meta_info = response.meta
		lis = sel.xpath('//*[@class="all-img-list cf"]/li')#小说基本信息模块
		if lis:
			for li in lis:
				item = QidianItem()
				item['title'] = li.xpath('.//h4/a/text()').extract()[0]
				print u'小说标题：', item['title']
				item['title_url'] = li.xpath('.//h4/a/@href').extract()[0]
				print u'小说链接：', item['title_url']
				item['author'] = li.xpath('.//p/a/text()').extract()[0]
				print u'小说作者', item['author']
				item['bid'] = item['title_url'].split('/')[-1].split('.')[0]
				print u'小说id：', item['bid']
				item['relate_id'] = 'qidian%s'%item['bid']
				item['refresh_time'] = time.strftime('%Y-%m-%d %H:%M:%S')
				yield item