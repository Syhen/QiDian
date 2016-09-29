# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QidianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()#小说名称
    author = scrapy.Field()#小说作者
    title_url = scrapy.Field()#小说链接
    bid = scrapy.Field()#小说id
    relate_id = scrapy.Field()#小说存储主键
    refresh_time = scrapy.Field()#索引更新时间
    source = scrapy.Field()

class QiDianInfo(scrapy.Item):
	title = scrapy.Field()#小说名称
	author = scrapy.Field()#小说作者
	title_url = scrapy.Field()#小说链接
	bid = scrapy.Field()#小说id
	relate_id = scrapy.Field()#小说存储主键
	
	type_main = scrapy.Field()#小说主要类型
	type_sec = scrapy.Field()#小说次要类型
	statu = scrapy.Field()#小说写作进度
	introduce = scrapy.Field()#小说简介
	img_url = scrapy.Field()#封面链接
	charpter_url = scrapy.Field()#章节链接

	all_clicks = scrapy.Field()#总点击
	all_suggests = scrapy.Field()#总推荐
	all_counts = scrapy.Field()#总字数
	day_month_ticket = scrapy.Field()#今日月票
	day_dashang = scrapy.Field()#今日打赏
	day_cuigeng = scrapy.Field()#今日催更
	statu_qianyue = scrapy.Field()#签约状态
	update_time = scrapy.Field()#更新时间
	scrapy_time = scrapy.Field()#抓取时间
	show_time = scrapy.Field()#展示日期
	source = scrapy.Field()

class QidianInfo(scrapy.Item):
	source = scrapy.Field()
	bid = scrapy.Field()
	today = scrapy.Field()

	follow_people = scrapy.Field()
	read_rate = scrapy.Field()
	zhuishu_count = scrapy.Field()
	zhuishu_id = scrapy.Field()

class JJWXIndex(scrapy.Item):
	title = scrapy.Field()
	author = scrapy.Field()
	author_url = scrapy.Field()
	title_url = scrapy.Field()
	bid = scrapy.Field()
	relate_id = scrapy.Field()
	refresh_time = scrapy.Field()
	source = scrapy.Field()
	first_time = scrapy.Field()

class JJWXInfo(scrapy.Item):
	title = scrapy.Field()
	author = scrapy.Field()
	author_url = scrapy.Field()
	title_url = scrapy.Field()
	bid = scrapy.Field()
	relate_id = scrapy.Field()
	source = scrapy.Field()
	first_time = scrapy.Field()
	introduce = scrapy.Field()
	img_url = scrapy.Field()
	c_type = scrapy.Field()
	c_style = scrapy.Field()
	update_statu = scrapy.Field()
	all_count = scrapy.Field()
	download_num = scrapy.Field()
	score = scrapy.Field()
	click_num = scrapy.Field()
	comment_num = scrapy.Field()
	collect_num = scrapy.Field()
	update_time = scrapy.Field()
	new_charpter = scrapy.Field()
	new_charpter_url = scrapy.Field()

	today = scrapy.Field()
	scrapy_time = scrapy.Field()

	pass_statu = scrapy.Field()

	follow_people = scrapy.Field()
	read_rate = scrapy.Field()
	zhuishu_count = scrapy.Field()
	zhuishu_id = scrapy.Field()


class JJWXALLIndex(scrapy.Item):
	title = scrapy.Field()
	url = scrapy.Field()
	author = scrapy.Field()
	source = scrapy.Field()
	recommend_num = scrapy.Field()





