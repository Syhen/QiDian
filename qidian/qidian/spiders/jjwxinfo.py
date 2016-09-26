# -*- coding:utf-8 -*-

import scrapy
from scrapy.selector import Selector
from qidian.items import JJWXInfo
from qidian.settings import db
import time

class JJWXInfoSpider(scrapy.Spider):
	"""
	"""
	name = 'jjwxinfo'

	def start_requests(self):
		datas = [d for d in db.bookIndex.find({'source': 7})]
		for i in datas:
			yield scrapy.FormRequest(
				i['title_url'],
				dont_filter = True,
				meta = {
					'first_time': i['first_time'], 
					'author': i['author'],
					'author_url': i['author_url'], 
					'title': i['title'], 
					'bid': i['bid']
				},
				callback = self.parse
			)

	def parse(self, response):
		print response.url
		sel = Selector(text = response.body.decode('gbk', 'ignore'))
		meta_info = response.meta
		item = JJWXInfo()
		basic_infos = sel.xpath('//*[@style="table-layout:fixed "]')
		update_infos = sel.xpath('//*[@id="oneboolt"]')
		if basic_infos:
			item['source'] = 7
			item['first_time'] = meta_info['first_time']
			item['author'] = meta_info['author']
			item['author_url'] = meta_info['author_url']
			item['title'] = meta_info['title']
			item['title_url'] = response.url
			item['bid'] = meta_info['bid']
			item['relate_id'] = 'jjwx_%s'%item['bid']
			item['introduce'] = [t for t in basic_infos.xpath('.//*[@id="novelintro"]/font/text()').extract()]
			if item['introduce'] == []:
				item['introduce'] = [t for t in basic_infos.xpath('.//*[@id="novelintro"]/text()').extract()]
			# print item['introduce']
			basics = basic_infos.xpath('.//ul[@class="rightul"]/li')
			item['c_type'] = basics[0].xpath('./span[2]/text()').extract()[0].strip()
			print item['c_type']
			try:
				item['c_style'] = basics[1].xpath('./text()').extract()[0]
			except IndexError:
				item['c_style'] = u''
			print item['c_style']
			try:
				item['update_statu'] = basics[3].xpath('./span[2]/text()').extract()[0]
			except IndexError:
				item['update_statu'] = basics[3].xpath('./span[2]/font/text()').extract()[0]
			print item['update_statu']
			item['all_count'] = int(basics[4].xpath('./span[2]/text()').extract()[0].split(u'字')[0])
			print item['all_count']
		else:
			print 'NO BASIC INFO: %s'%response.url
		if update_infos:
			pass
		else:
			print 'NO UPDATE INFO: %s'%response.url