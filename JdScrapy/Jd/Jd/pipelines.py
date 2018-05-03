# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pymysql.cursors


class JingdongPipeline(object):
    # 连接登录mysql，新建数据表
    def __init__(self):
        self.conn = pymysql.connect(host="localhost",
                                    user="root",
                                    passwd="zzq123456",
                                    db="jd",
                                    charset='utf8'
                                    )
        cur = self.conn.cursor()
        cur.execute("USE jd")
        cur.execute(
            "CREATE TABLE computer(id INT PRIMARY KEY AUTO_INCREMENT,title VARCHAR(100),link VARCHAR(50),price VARCHAR(50),comment VARCHAR(50))")
        self.conn.commit()

    def process_item(self, item, jd):
        try:
            title_1 = item['title']
            link_1 = item['link']
            price_1 = item['price']
            comment_1 = item['comment']
            cur = self.conn.cursor()
            cur.execute("INSERT INTO computer(title,link,price,comment) VALUES (%s,%s,%s,%s)",
                        (title_1, link_1, price_1, comment_1))
            self.conn.commit()
        except Exception as err:
            pass
        return item



    # # 爬虫初始化时的操作
    # def __init__(self):
    #     self.f = open("jd.txt", "w")
    # def process_item(self, item, spider):
    #     with open("jd.txt","w")as f:
    #         f.write(item)
    #     return item
    # # 爬虫爬取的数据传入，每次爬虫返回item，都会执行
    # # def process_item(self,item,spider):
    # #     content = json.dumps(dict(item),ensure_asscii=False + ",\n")
    # #     self.f.write(content.encode("utf-8"))
    # #     #返回给引擎
    # #     return item
    # def close_spider(self,spider):
    #     self.f.close()
