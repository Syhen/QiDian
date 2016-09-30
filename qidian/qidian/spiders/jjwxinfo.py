# -*- coding:utf-8 -*-

import scrapy
from scrapy.selector import Selector
from qidian.items import JJWXInfo
from qidian.settings import db
import time
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class JJWXInfoSpider(scrapy.Spider):
	"""
	"""
	name = 'jjwxinfo'

	def start_requests(self):
		datas = [d for d in db.bookIndex.find({'source': 7})]
		today = time.strftime('%Y/%m/%d %H:%M:%S')
		for i in datas:
			if not i.has_key('author_url'):
				continue
			yield scrapy.FormRequest(
				i['title_url'],
				dont_filter = True,
				meta = {
					'first_time': i['first_time'], 
					'author': i['author'],
					'author_url': i['author_url'], 
					'title': i['title'], 
					'bid': i['bid'],
					'today': today
				},
				callback = self.parse
			)
		# yield scrapy.FormRequest(
		# 	'http://www.jjwxc.net/onebook.php?novelid=2817605',
		# 	dont_filter = True,
		# 	meta = {
		# 		'first_time': '2016-09-29 00:00:00', 
		# 		'author': u'Caeser',
		# 		'author_url': '', 
		# 		'title': u'林西', 
		# 		'bid': '2817605',
		# 		'today': '2016-09-30 00:00:00'
		# 	},
		# 	callback = self.parse
		# )
			# break

	def parse(self, response):
		print response.url
		sel = Selector(text = response.body.decode('gbk', 'ignore'))
		meta_info = response.meta
		item = JJWXInfo()
		item['crawl_time'] = meta_info['today']
		item['return_status'] = 'ok'
		item['follow_people'] = 0
		item['read_rate'] = 0.0
		item['zhuishu_count'] = 0
		item['today'] = time.strftime('%Y/%m/%d %H:%M:%S')
		item['source'] = 7
		item['first_time'] = meta_info['first_time']
		item['author'] = meta_info['author']
		item['author_url'] = meta_info['author_url']
		item['title'] = meta_info['title']
		item['title_url'] = response.url
		item['bid'] = 'jjwx_'+meta_info['bid']
		item['c_id'] = item['bid'].split('_')[-1]
		item['isvip'] = '[VIP]' in response.body.decode('gbk', 'ignore')
		basic_infos = sel.xpath('//*[@style="table-layout:fixed "]')
		update_infos = sel.xpath('//*[@id="oneboolt"]')
		if basic_infos:
			# item['relate_id'] = 'jjwx_%s'%item['bid']
			item['introduce'] = [t for t in basic_infos.xpath('.//*[@id="novelintro"]/font/text()').extract()]
			if item['introduce'] == []:
				item['introduce'] = [t for t in basic_infos.xpath('.//*[@id="novelintro"]/text()').extract()]
			item['introduce'] = ''.join(item['introduce'])
			try:
				item['img_url'] = basic_infos.xpath('.//img[@itemprop="image"]/@src').extract()[0]
			except IndexError:
				item['img_url'] = u''
			# print item['introduce']
			basics = basic_infos.xpath('.//ul[@class="rightul"]/li')
			item['c_type'] = basics[0].xpath('./span[2]/text()').extract()[0].strip()
			# print item['c_type']
			try:
				item['c_style'] = basics[1].xpath('./text()').extract()[0]
			except IndexError:
				item['c_style'] = u''
			# print item['c_style']
			try:
				item['percent'] = basics[3].xpath('./span[2]/text()').extract()[0]
			except IndexError:
				item['percent'] = basics[3].xpath('./span[2]/font/text()').extract()[0]
			
			item['is_finished'] = (u'完' in item['percent'])
			# print item['percent']
			item['all_count'] = int(basics[4].xpath('./span[2]/text()').extract()[0].split(u'字')[0])
			# print item['all_count']
		else:
			item['return_status'] = 'pass'
		if update_infos:
			info_num = 0
			if len(update_infos.xpath('.//tr[last()]//span').extract()) == 0:
				info_num = 1
			data = update_infos.xpath('.//tr[last() - '+str(info_num)+']//div')
			data_str = u''.join(data.xpath('./text()').extract())
			# print data_str
			if info_num:
				item['update_time'] = u'此作品无更新时间'
				item['new_capture'] = u'此作品无最新章节'
				item['new_capture_url'] = u'此作品无最新章节链接'
			if u'总下载数：' in data_str:
				item['download_count'] = int(data_str.split(u'非V章节总点击数：')[0].split(u'总下载数：')[1].strip())
				#http://www.jjwxc.net/onebook.php?novelid=2938416非章节类型
				# print item['download_count']
				item['score'] = int(data_str.split(u'文章积分：')[1].strip().replace(',', ''))
				# print item['score']
				item['all_comments'] = int(data.xpath('./span[@itemprop="reviewCount"]/text()').extract()[0])
				# print item['all_comments']
				item['all_collect'] = int(data.xpath('./span[@itemprop="collectedCount"]/text()').extract()[0])
				# print item['all_collect']
				if item.get('update_time', '') == '':
					item['update_time'] = update_infos.xpath('.//tr[last() - 1]/td[last()]/span[1]/text()').extract()[0].strip()
				# print item['update_time']
				cha_url_num = 1
				if item.get('new_capture', '') == '':
					try:
						item['new_capture'] = update_infos.xpath('.//tr[last() - 1]/td[2]//a/text()').extract()[0].strip()
					except IndexError:
						num = int(update_infos.xpath('.//tr[last() - 1]/td[1]/text()').extract()[0].strip())
						for i in range(2, num):
							if update_infos.xpath('.//tr[last() - '+str(i)+']/td[2]//a').extract() != []:
								try:
									item['new_capture'] = update_infos.xpath('.//tr[last() - '+str(i)+']/td[2]//a/text()').extract()[0].strip()
								except IndexError:
									item['new_capture'] = u'无章节名称'
								cha_url_num = i
								break
						else:
							item['new_capture'] = u'无最新章节'
							item['new_capture_url'] = u'无最新章节链接'
				# print item['new_capture']
				if item.get('new_capture_url', '') == '':
					try:
						item['new_capture_url'] = update_infos.xpath('.//tr[last() - '+str(cha_url_num)+']/td[2]//a/@href').extract()[0].strip()
					except IndexError:
						item['new_capture_url'] = u'VIP章节'
				# print item['new_capture_url']
			else:
				data = self.parse_none_charpter(basic_infos, item)
				item['download_count'] = data['download_count']
				item['all_comments'] = data['all_comments']
				item['all_clicks'] = data['all_clicks']
				item['all_collect'] = data['all_collect']
				item['score'] = data['score']
				item['update_time'] = data['update_time']
				item['new_capture'] = data['new_capture']
				item['new_capture_url'] = data['new_capture_url']
		else:
			# print 'NO UPDATE INFO: %s'%response.url
			item['return_status'] = 'pass'
		yield scrapy.FormRequest(
			'http://s8.static.jjwxc.net/getnovelclick.php?novelid=%s'%item['bid'],
			dont_filter = True,
			meta = {
				'item': item
			},
			callback = self.parse_clicks
		)

	def parse_none_charpter(self, basic_infos, item):
		data = {}
		info_str = basic_infos.xpath('.//tr[1]/td[1]/div[4]/text()').extract()[0].strip()
		all_clicks = int(info_str.split(u'总书评数：')[0].split(u'总点击数：')[1].strip())
		# print all_clicks
		all_comments = int(info_str.split(u'当前被收藏数：')[0].split(u'总书评数：')[1].strip())
		# print all_comments
		all_collect = int(info_str.split(u'文章积分：')[0].split(u'当前被收藏数：')[1].strip())
		# print all_collect
		score = int(info_str.split(u'文章积分：')[1].strip().replace(',', ''))
		# print score
		download_count = 0
		update_time = item['first_time']
		new_capture = u'此作品非章节类型'
		new_capture_url = item['title_url']
		data['all_clicks'] = all_clicks
		data['all_comments'] = all_comments
		data['all_collect'] = all_collect
		data['score'] = score
		data['download_count'] = download_count
		data['update_time'] = update_time
		data['new_capture'] = new_capture
		data['new_capture_url'] = new_capture_url
		return data

	def parse_clicks(self, response):
		item = response.meta['item']
		try:
			jDoc = json.loads(response.body.decode('gbk', 'ignore'))
			click_count = sum(map(lambda x:int(x), list(jDoc.values())))
		except Exception as e:
			click_count = 0
		item['all_clicks'] = click_count
		if item.get('return_status', '') == '':
			item['return_status'] = 'ok'
		yield item











