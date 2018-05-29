# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os


class WeatherPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        if not os.path.exists("./data/weather.csv"):
            with open('./data/weather.csv', 'w', newline='') as header_file:
                header_writer = csv.writer(header_file)
                header_writer.writerow(['城市', '日期', '天气描述', '白天温度/°C', '夜间温度/°C'])
        with open('./data/weather.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            city = item['city']
            for i in range(len(item['date'])):
                date = item['date'][i]
                desc = item['day_desc'][i]

                #温度处理
                temp = item['day_temp'][i].split('/')
                day_temp = temp[0].replace('°C', '')
                night_temp = ""
                if len(temp) > 1:
                    if temp[1] == ' °C':
                        night_temp = day_temp
                    else:
                        night_temp = temp[1].replace('°C', '')
                writer.writerow(
                            [city, date, desc, day_temp, night_temp])
            return item
