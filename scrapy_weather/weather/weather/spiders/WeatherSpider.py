# -*- coding:utf-8 -*-
"""
@author:aGreysky
@file:WeatherSpider.py
@time:2018/5/8 16:32
"""
import scrapy
from bs4 import BeautifulSoup

from weather.items import WeatherItem


class WeatherSpider(scrapy.Spider):
    name = "weather"
    allowed_domains = ["sina.com.cn"]
    start_urls = ['http://weather.sina.com.cn']

    def parse(self, response):
        html_doc = response.body
        #html_doc = html_doc.decode('utf-8')
        soup = BeautifulSoup(html_doc)
        item_temp = {}
        item_temp['city'] = soup.find(id='slider_ct_name')
        #信息根节点
        ten_day = soup.find(id='blk_fc_c0_scroll')
        item_temp['date'] = ten_day.findAll("p", {"class": 'wt_fc_c0_i_date'})
        item_temp['day_desc'] = ten_day.findAll("p", {"class": 'wt_fc_c0_i_tip'})
        item_temp['day_temp'] = ten_day.findAll('p', {"class": 'wt_fc_c0_i_temp'})
        #print(all_day_temp)
        item = WeatherItem()
        for att in item_temp:
            item[att] = []
            if att == 'city':
                item[att] = item_temp.get(att).text
                continue
            for obj in item_temp.get(att):
                item[att].append(obj.text)
        return item