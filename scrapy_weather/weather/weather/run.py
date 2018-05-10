from scrapy import cmdline

from weather.spiders import WeatherSpider

if __name__ =="__main__":
    WeatherSpider.start_urls =["http://weather.sina.com.cn"]
    cmdline.execute("scrapy crawl weather".split())