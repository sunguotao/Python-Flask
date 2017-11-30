# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo
from  .items import ToutiaoFocusItem,ToutiaoHotVideoItem,ToutiaoHotGalleryItem,ToutiaoFeedItem


class ToutiaoPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(settings['MONGODB_HOST'],settings['MONGODB_PORT'])
        self.db = connection[settings['MONGODB_NAME']]

    def process_item(self,item,spider):
        _ = spider
        if isinstance(item,ToutiaoFocusItem):
            post = self.db[settings['MONGODB_DOCNAME']]
            post.update({'image_url':item['image_url']},{'$set':dict(item)},upsert=True)
        elif isinstance(item,ToutiaoHotVideoItem):
            post = self.db[settings['MONGODB_HOT_VIDEO_NAME']]
            post.update({'title': item['title']}, {'$set': dict(item)}, upsert=True)
        elif isinstance(item,ToutiaoHotGalleryItem):
            post = self.db[settings['MONGODB_HOT_GALLERY_NAME']]
            post.update({'title': item['title']}, {'$set': dict(item)}, upsert=True)
        elif isinstance(item, ToutiaoFeedItem):
            post = self.db[settings['MONGODB_HOT_FEED_NAME']]
            post.update({'title': item['title']}, {'$set': dict(item)}, upsert=True)
        print('update success')
        return item
