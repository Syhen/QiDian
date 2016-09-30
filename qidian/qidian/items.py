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
	c_id = scrapy.Field()
	statu = scrapy.Field()
	# relate_id = scrapy.Field()
	refresh_time = scrapy.Field()
	source = scrapy.Field()
	first_time = scrapy.Field()

class JJWXInfo(scrapy.Item):
	# title = scrapy.Field()
	# author = scrapy.Field()
	# author_url = scrapy.Field()
	# title_url = scrapy.Field()
	# bid = scrapy.Field()
	# relate_id = scrapy.Field()
	# source = scrapy.Field()
	# first_time = scrapy.Field()
	# introduce = scrapy.Field()
	# img_url = scrapy.Field()
	# c_type = scrapy.Field()
	# c_style = scrapy.Field()
	# update_statu = scrapy.Field()
	# all_count = scrapy.Field()
	# download_num = scrapy.Field()
	# score = scrapy.Field()
	# click_num = scrapy.Field()
	# comment_num = scrapy.Field()
	# collect_num = scrapy.Field()
	# update_time = scrapy.Field()
	# new_charpter = scrapy.Field()
	# new_charpter_url = scrapy.Field()

	# today = scrapy.Field()
	# scrapy_time = scrapy.Field()

	# pass_statu = scrapy.Field()

	# follow_people = scrapy.Field()
	# read_rate = scrapy.Field()
	# zhuishu_count = scrapy.Field()
	# zhuishu_id = scrapy.Field()
	
	bid = scrapy.Field()
	img_url = scrapy.Field()
	title = scrapy.Field()
	author = scrapy.Field()
	introduce = scrapy.Field()
	url = scrapy.Field()
	#分男女
	sex_type = scrapy.Field()
	
	#书号
	book_num = scrapy.Field()
	#签约状态
	signed = scrapy.Field()
	#总点击
	all_clicks = scrapy.Field()
	#总字数
	all_count = scrapy.Field()
	#小说最后更新时间
	update_time = scrapy.Field()
	#今日打赏
	money_people = scrapy.Field()
	#小说状态
	update_status = scrapy.Field()
	#小说类型
	c_type = scrapy.Field()
	#上架时间
	first_time = scrapy.Field()
	#抓取时间
	scrapy_time = scrapy.Field()
	#总推荐
	all_suggest = scrapy.Field()
	#追书人数
	follow_people = scrapy.Field()
	#留存率
	read_rate = scrapy.Field()
	#追书的小说总字数
	zhuishu_count = scrapy.Field()
	#日更新字数
	update_day_num = scrapy.Field()
	#章节列表入口
	charpter_url = scrapy.Field()
	#小说在追书神器中的ID
	zhuishu_id = scrapy.Field()
	#今日推荐
	day_suggest = scrapy.Field()
	#今日点击
	day_click = scrapy.Field()
	#追书的日更新字数
	zhuishu_day_num = scrapy.Field()
	#追书的所有标签
	zhuishu_tags = scrapy.Field()
	#人气
	popular = scrapy.Field()
	#来源
	source = scrapy.Field()
	#总收藏
	all_collect = scrapy.Field()
	#评论数
	all_comments = scrapy.Field()
	#月票
	month_tickts = scrapy.Field()
	#网易标签
	tags = scrapy.Field()
	#网易评分人数
	comment_people = scrapy.Field()
	#晋江文学城
	#作者链接
	author_url = scrapy.Field()
	#标题链接
	title_url = scrapy.Field()
	#作品类型
	c_type = scrapy.Field()
	#作品风格
	c_style = scrapy.Field()
	#进度
	percent = scrapy.Field()
	#分数
	score = scrapy.Field()
	#下载次数
	download_count = scrapy.Field()
	#标签名称
	con_label = scrapy.Field()
	#最新章节名称
	new_capture = scrapy.Field()
	#最新章节链接
	new_capture_url = scrapy.Field()
	#是否完成
	is_finished = scrapy.Field()
	#是否含有vip
	isvip = scrapy.Field()
	#书籍id（不含平台）
	c_id = scrapy.Field()
	#追书中是否有数据标记
	zhuishu_statu = scrapy.Field()
	#update_time
	crawl_time = scrapy.Field()
	#图片是否验证
	img_url_sign = scrapy.Field()
	#书籍标记
	statu = scrapy.Field()
	return_status = scrapy.Field()
	#作者id
	author_id = scrapy.Field()
	#抓取日期
	today = scrapy.Field()
	#索引更新时间
	refresh_time = scrapy.Field()


class JJWXALLIndex(scrapy.Item):
	title = scrapy.Field()
	url = scrapy.Field()
	author = scrapy.Field()
	source = scrapy.Field()
	recommend_num = scrapy.Field()





