# -*- coding:utf-8 -*-

import scrapy
from scrapy.selector import Selector
from qidian.items import QiDianInfo
from qidian.settings import db
import time

class QiDianInfoSpider(scrapy.Spider):
	"""
	"""
	name = 'qidianinfo'

	def start_requests(self):
		datas = [i for i in db.bookIndex.find({'source':1})]
		print '[START]'
		show_time = time.strftime('%Y/%m/%d %H:%M:%S')
		for d in datas:
			item = QiDianInfo()
			item['source'] = 1
			item['title_url'] = d['title_url']
			item['title'] = d['title']
			item['author'] = d['author']
			item['bid'] = d['bid']
			item['relate_id'] = d['relate_id']
			yield scrapy.FormRequest(
				item['title_url'],
				dont_filter = True,
				meta = {
					'item': item,
					'show_time': show_time
				},
				callback = self.parse
			)

	def parse(self, response):
		print response.url
		item = response.meta['item']
		show_time = response.meta['show_time']
		sel = Selector(text = response.body)
		item['type_main'] = sel.xpath('//*[@class="page_site"]/a[2]/text()').extract()[0].strip()
		item['type_sec'] = sel.xpath('//*[@class="page_site"]/a[3]/text()').extract()[0].strip()
		item['statu'] = sel.xpath('//*[@itemprop="updataStatus"]/text()').extract()[0]
		item['introduce'] = '\n'.join(sel.xpath('//*[@itemprop="description"]/text()').extract())
		item['img_url'] = sel.xpath('//*[@itemprop="image"]/@src').extract()[0]
		item['charpter_url'] = sel.xpath(u'//*[text()="点击阅读"]/@href').extract()[0]
		data = sel.xpath('//*[@class="data"]')
		item['all_clicks'] = int(data.xpath('.//td[1]/text()[2]').extract()[0].strip())
		item['all_suggests'] = int(data.xpath('.//td[3]/text()[2]').extract()[0].strip())
		item['all_counts'] = int(data.xpath('.//td[4]/text()[2]').extract()[0].strip())
		try:
			item['day_month_ticket'] = int(sel.xpath('//*[@class="txt tab_bkmain tab_bkitem1"]/b/text()').extract()[0])
		except IndexError:
			item['day_month_ticket'] = 0
		try:
			item['day_dashang'] = int(sel.xpath('//*[@class="txt tab_bkmain tab_bkitem2"]/b/text()').extract()[0])
		except IndexError:
			item['day_dashang'] = 0
		try:
			item['day_cuigeng'] = int(sel.xpath('//*[@class="txt tab_bkmain tab_bkitem3"]/b/text()').extract()[0])
		except IndexError:
			item['day_cuigeng'] = 0
		item['statu_qianyue'] = sel.xpath('//*[@class="info_box"]//tr[last()]/td[3]/strong/text()').extract()[0].strip()
		item['update_time'] = sel.xpath('//*[@class="tabs"]//span/text()').extract()[0].strip()
		item['scrapy_time'] = time.strftime('%Y/%m/%d %H:%M:%S')
		item['show_time'] = show_time
		yield item