# -*- coding: utf-8 -*-
import scrapy
import json
from  ..items import ToutiaoFocusItem,ToutiaoHotVideoItem,ToutiaoHotGalleryItem,ToutiaoFeedItem


class ToutiaoSpider(scrapy.Spider):
    name = 'toutiao'
    allowed_domains = ['toutiao.com']
    start_urls = ['https://www.toutiao.com/']
    # 推荐, 视频
    urls = ['api/pc/focus/','api/pc/hot_video/?widen=1','api/pc/hot_gallery/?widen=1',
            'api/pc/feed/?min_behot_time=0&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as=A1851AF10FF64D9&cp=5A1F3634FDE96E1&_signature=-d8D8xARo8p59kCMliNDOfnfAu']

    headers = {
    'Accept': 'text / javascript, text / html, application / xml, text / xml, * / *',
    'Accept - Encoding': 'gzip, deflate, br',
    'Accept - Language': 'zh - CN, zh;q = 0.9, en;q = 0.8',
    'Cache - Control': 'no - cache',
    'Connection': 'keep - alive',
    'Content - Type': 'application / x - www - form - urlencoded',
    'Cookie': 'uuid = "w:f69d4cc8f5d3408195208602f335fd6a";__utma = 24953151.832223188.1453357457.1453357457.1453357457.1;csrftoken = 9a271402b808c289a47036afd16405c7;UM_distinctid = 15cc4727ce7c67 - 0c98f8a6689331 - 30637509 - 1fa400 - 15cc4727ce8b03;_ga = GA1.2.832223188.1453357457;_gid = GA1.2.251360549.1511941268;CNZZDATA1259612802 = 1481427958 - 1478222989 - https % 253A % 252F % 252Fwww.baidu.com % 252F % 7C1512005777;__tasessionId = ys9yi8b1e1512005999436;tt_webid = 6433622443994826242;tt_webid = 6433622443994826242;WEATHER_CITY = % E5 % 8C % 97 % E4 % BA % AC',
    'Host': 'www.toutiao.com',
    'Pragma': 'no - cache',
    'Referer': 'https: // www.toutiao.com /',
    'X - Requested - With': 'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    def start_requests(self):
        yield scrapy.Request(self.start_urls[0]+self.urls[0],callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)['data']['pc_feed_focus']
        for d in data:
            item = ToutiaoFocusItem()
            item['title'] = d.get('title')
            item['display_url'] = d.get('display_url')
            item['has_video'] = d.get('has_video')
            item['image_url'] = d.get('image_url')
            item['has_image'] = d.get('has_image')
            item['group_id'] = d.get('group_id')
            item['media_url'] = d.get('media_url')
            yield item
        yield scrapy.Request(self.start_urls[0]+self.urls[1],callback=self.parse_hot_video)

    def parse_hot_video(self,response):
        data = json.loads(response.text)['data']
        for d in data:
            item = ToutiaoHotVideoItem()
            item['title'] = d.get('title')
            item['display_url'] = d.get('display_url')
            item['pc_image_url'] = d.get('pc_image_url')
            item['comment_count'] = d.get('comment_count')
            item['video_play_count'] = d.get('video_play_count')
            item['video_duration_format'] = d.get('video_duration_format')
            item['video_duration'] = d.get('video_duration')
            yield item
        yield scrapy.Request(self.start_urls[0] + self.urls[2], callback=self.parse_hot_gallery)

    def parse_hot_gallery(self,response):
        data = json.loads(response.text)['data']
        for d in data:
            item = ToutiaoHotGalleryItem()
            item['title'] = d.get('title')
            item['gallary_flag'] = d.get('gallary_flag')
            item['image_list'] = d.get('image_list')
            item['article_url'] = d.get('article_url')
            item['cover_image_url'] = d.get('cover_image_url')
            item['gallery_image_count'] = d.get('gallery_image_count')
            yield item
        yield scrapy.Request(self.start_urls[0]+self.urls[3],callback=self.parse_feed,headers=self.headers)

    def parse_feed(self,response):
        print('data', response.text)
        data = json.loads(response.text)['data']
        for d in data:
            item = ToutiaoFeedItem()
            item['single_mode'] = d.get('single_mode')
            item['abstract'] = d.get('abstract')
            item['middle_mode'] = d.get('middle_mode')
            item['more_mode'] = d.get('more_mode')
            item['tag'] = d.get('tag')
            item['label'] = d.get('label')
            item['comments_count'] = d.get('comments_count')
            item['tag_url'] = d.get('tag_url')
            item['title'] = d.get('title')
            item['chinese_tag'] = d.get('chinese_tag')
            item['source'] = d.get('source')
            item['group_source'] = d.get('group_source')
            item['has_gallery'] = d.get('has_gallery')
            item['media_url'] = d.get('media_url')
            item['media_avatar_url'] = d.get('media_avatar_url')
            item['image_list'] = d.get('image_list')
            item['source_url'] = d.get('source_url')
            item['article_genre'] = d.get('article_genre')
            item['is_feed_ad'] = d.get('is_feed_ad')
            item['behot_time'] = d.get('behot_time')
            item['image_url'] = d.get('image_url')
            item['group_id'] = d.get('group_id')
            item['middle_image'] = d.get('middle_image')
            yield item





























