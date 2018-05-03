from scrapy import cmdline

from Jd.spiders.Jd import JdSpider

if __name__ =="__main__":
    JdSpider.start_urls =["http://jd.com/"]
    cmdline.execute("scrapy crawl jd".split())