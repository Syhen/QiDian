# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from qidian.settings import db
from scrapy.mail import MailSender
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class QidianPipeline(object):
    def close_spider(self, spider):
        if spider.__class__.name == 'qidianindex':
            today = time.strftime('%Y-%m-%d')
            cnt_today = db.bookIndex.find({'refresh_time':{'$regex':today}}).count()
            cnt_all = db.bookIndex.find({}).count()
            rate = cnt_today * 1.0 / cnt_all
            mailer = MailSender(
                smtphost = 'smtp.qq.com', 
                mailfrom = '', 
                smtpuser = '', 
                smtppass = ''
            )
            mailer.send(
                to = [''], 
                subject = '黑马-起点爬虫抓取结果', 
                body = '共有<strong>{0}</strong>条索引，其中：\n\n\r\r\r\r今日更新<strong>{1}</strong>条，占总索引比例为：<strong>{2}%</strong>。'.format(cnt_all, cnt_today, '%.2f'%(rate * 100)), 
                mimetype = 'text/html'
            )

    def process_item(self, item, spider):
    	if spider.__class__.name == 'qidianindex':
        	db.bookIndex.update({'_id': item['relate_id']}, {'$set': item}, True)
        elif spider.__class__.name == 'qidianinfo':
        	data_history = {}
        	data_history['title_url'] = item['title_url']
        	data_history['bid'] = item['bid']
        	data_history['relate_id'] = item['relate_id']
        	data_history['statu'] = item['statu']

        	data_history['all_clicks'] = item['all_clicks']
        	data_history['all_suggests'] = item['all_suggests']
        	data_history['day_month_ticket'] = item['day_month_ticket']
        	data_history['day_dashang'] = item['day_dashang']
        	data_history['day_cuigeng'] = item['day_cuigeng']
        	data_history['statu_qianyue'] = item['statu_qianyue']
        	data_history['update_time'] = item['update_time']
        	data_history['scrapy_time'] = item['scrapy_time']
        	data_history['show_time'] = item['show_time']
        	data_history['source'] = item['source']
        	data_history['source'] = item['source']

        	data_history['c_id'] = item['relate_id']+'-'+item['show_time'].split(' ')[0]
        	db.bookInfo.update({'_id': data_history['relate_id']}, {'$set': item}, True)
        	db.bookInfoHistory.update({'_id': data_history['c_id']}, {'$set': data_history}, True)

        elif spider.__class__.name == 'jjwxindex':
            db.bookIndex.update({'_id': item['relate_id']}, {'$setOnInsert': item}, True)#不存在则插入，存在则忽略
