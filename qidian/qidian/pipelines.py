# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from qidian.settings import db
from scrapy.mail import MailSender
import time
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class QidianPipeline(object):
    def open_spider(self, spider):
        self.t2 = datetime.datetime.now()

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
        print (datetime.datetime.now() - self.t2)
            

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

        elif spider.__class__.name == 'jjwxallindex':
            ids = item['url'].split('=')[-1] + '_7'
            db.bh_all_data.update({'_id': ids}, {'$set':item}, True)

        elif spider.__class__.name == 'flallindex':
            ids = item['url'].split('/')[-1].split('.')[0]+'_10'
            db.bh_all_data.update({'_id': ids}, {'$set': item}, True)

        elif spider.__class__.name == 'csallindex':
            ids = item['url'].split('/')[-1].split('.')[0]+'_8'
            db.bh_all_data.update({'_id': ids}, {'$set': item}, True)

        elif spider.__class__.name =='sqkallindex':
            ids = item['url'].split('/')[-1].split('.')[0]+'_9'
            db.bh_all_data.update({'_id': ids}, {'$set': item}, True)

        elif spider.__class__.name == 'sqkallclick':
            ids = item['url'].split('/')[-1].split('.')[0]+'_9'
            db.bh_all_data.update({'_id': ids}, {'$set': item}, True)
        elif spider.__class__.name == 'jjwxinfo':
            # print item['title_url']
            if item['pass_statu'] == 'ok':
                # print item['pass_statu']
                dict_update = {}
                dict_update['all_clicks'] = item['click_num']
                dict_update['all_count'] = item['all_count']
                dict_update['author_url'] = item['author_url']
                dict_update['bid'] = item['bid']
                dict_update['relate_id'] = item['relate_id']
                dict_update['source'] = item['source']
                dict_update['first_time'] = item['first_time']
                dict_update['update_statu'] = item['update_statu']
                dict_update['download_num'] = item['download_num']
                dict_update['score'] = item['score']
                dict_update['comment_num'] = item['comment_num']
                dict_update['collect_num'] = item['collect_num']
                dict_update['update_time'] = item['update_time']
                dict_update['new_charpter'] = item['new_charpter']
                dict_update['new_charpter_url'] = item['new_charpter_url']
                dict_update['today'] = item['today']
                dict_update['scrapy_time'] = item['scrapy_time']
                dict_update['flag_id'] = dict_update['relate_id'] + dict_update['today'].split(' ')[0].replace('-', '/')
                db.bookInfo.update({'_id': item['relate_id']}, {'$set': item}, True)
                db.bookInfoHistory.update({'_id': dict_update['flag_id']}, {'$set': dict_update}, True)

        elif spider.__class__.name == 'jjwxzs':
            db.bookInfo.update({'_id': 'jjwx_'+item['bid']}, {'$set': item}, True)
            db.bookInfoHistory.update({'_id': 'jjwx_'+item['bid']+'-'+item['today'].split(' ')[0]}, {'$set': item}, True)









