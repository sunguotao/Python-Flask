# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ToutiaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ToutiaoFocusItem(scrapy.Item):
    title = scrapy.Field()
    display_url = scrapy.Field()
    has_video = scrapy.Field()
    image_url = scrapy.Field()
    has_image = scrapy.Field()
    group_id = scrapy.Field()
    media_url =scrapy.Field()


class ToutiaoHotVideoItem(scrapy.Item):
    title = scrapy.Field()
    display_url = scrapy.Field()
    pc_image_url = scrapy.Field()
    comment_count = scrapy.Field()
    video_play_count = scrapy.Field()
    video_duration_format = scrapy.Field()
    video_duration =scrapy.Field()


class ToutiaoHotGalleryItem(scrapy.Item):
    title = scrapy.Field()
    gallary_flag = scrapy.Field()
    article_url = scrapy.Field()
    cover_image_url = scrapy.Field()
    gallery_image_count = scrapy.Field()
    image_list = scrapy.Field()

class ToutiaoFeedItem(scrapy.Item):
    single_mode = scrapy.Field()
    abstract = scrapy.Field()
    middle_mode = scrapy.Field()
    more_mode = scrapy.Field()
    tag = scrapy.Field()
    label = scrapy.Field()
    comments_count = scrapy.Field()
    tag_url = scrapy.Field()
    title = scrapy.Field()
    chinese_tag = scrapy.Field()
    source = scrapy.Field()
    group_source = scrapy.Field()
    has_gallery = scrapy.Field()
    media_url = scrapy.Field()
    media_avatar_url = scrapy.Field()
    image_list = scrapy.Field()
    source_url = scrapy.Field()
    article_genre = scrapy.Field()
    is_feed_ad = scrapy.Field()
    behot_time = scrapy.Field()
    image_url = scrapy.Field()
    group_id = scrapy.Field()
    middle_image = scrapy.Field()

