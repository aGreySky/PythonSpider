# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    #城市名<h4 class：slider_ct_name>
    city = scrapy.Field()
    #日期<div id：blk_fc_c0_scroll>/<p class:wt_fc_c0_i_date>
    date = scrapy.Field()
    #天气描述<div id：blk_fc_c0_scroll>/<img class:icons0_wt>
    dayDesc = scrapy.Field()
    # 温度<div id：blk_fc_c0_scroll>/<p class:wt_fc_c0_i_temp>
    dayTemp = scrapy.Field()
    pass
