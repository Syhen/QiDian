# -*- coding:utf-8 -*-

import scrapy
from qidian.items import JJWXInfo
from qidian.settings import db
import time
import json

class JJWXZhuishuSpider(scrapy.Spider):
	"""
	"""
	name = 'jjwxzs'

	def start_requests(self):
		datas = [j for j in db.qidianinfo.find({'source': 7})]

		for d in datas:
			if d.has_key('title') and d.has_key('author') and d.has_key('all_count') and d.has_key('crawl_time'):
				if d['all_count'] >= 30000:
					item = JJWXInfo()
					item['bid'] = d['bid']
					item['crawl_time'] = d['crawl_time']
					yield scrapy.FormRequest(
						'http://api.zhuishushenqi.com/book/fuzzy-search?query={0}&start=0&limit=100'.format(d['title'],),
						dont_filter = True,
						meta = {
							'title': d['title'],
							'author': d['author'],
							'item': item
						},
						callback = self.parse
					)

	def parse(self, response):
		data = json.loads(response.body)
		meta_info = response.meta
		item = meta_info['item']
		item['follow_people'] = 0
		item['read_rate'] = 0.0
		item['zhuishu_count'] = 0
		if (data['ok']) and (data['books']):
			for i in data['books']:
				if (i['author'] == meta_info['author']) and (i['title'] == meta_info['title']):
					# print i['author']
					# print meta_info['author']
					# print i['title']
					# print meta_info['title']
					item['follow_people'] = i['latelyFollower']
					if item['follow_people'] == None:
						item['follow_people'] = 0
					else:
						item['follow_people'] = int(i['latelyFollower'])
					# print u'追书人数:%s' % item['follow_people']
					item['read_rate'] = i['retentionRatio']
					if item['read_rate'] == None:
						item['read_rate'] = float()
					else:
						item['read_rate'] = float(i['retentionRatio'])
					# print u'留存率:%s' % item['read_rate']
					# item['update_day_num'] = i['']
					
					item['zhuishu_count'] = i['wordCount']
					if item['zhuishu_count'] == None:
						item['zhuishu_count'] = 0
					else:
						item['zhuishu_count'] = int(i['wordCount'])
					# print u'更新字数:%s' % item['zhuishu_count']
					item['zhuishu_id'] = i['_id']
					break
		yield item








