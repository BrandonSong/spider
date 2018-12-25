# -*- coding: utf-8 -*-

# Scrapy settings for book project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import datetime

BOT_NAME = 'book'

SPIDER_MODULES = ['book.spiders']
NEWSPIDER_MODULE = 'book.spiders'


# LOG_ENCODING 默认使用 'utf-8'
# LOG-ENABLED 默认True 启用logging

# 设置log等级
# LOG_LEVEL = "WARNING"
# 设置LOG的保存位置
# to_day = datetime.datetime.now()
# LOG_FILE = "log/scrapy_{}_{}_{}.log".format(to_day.year, to_day.month, to_day.day)

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'

# 此处添加分布式爬虫的配置项
# 配置此项 可以使用scrapy-redis的去重类替换scrapy的去重类
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 配置此项 使用scrapy-redis的调度器的类替换scrapy的调度器的类
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 配置持久化
SCHEDULER_PERSIST = True

# 配置数据管道
# 默认开启redis的管道
# 也可以自定义数据管道，在此处开启即可
# ITEM_PIPELINES = {
    # 'example.pipelines.ExamplePipeline': 300,
    # scrapy-redis自带的数据管道类  将抓取的数据存储至redis数据库中
    # 'scrapy_redis.pipelines.RedisPipeline': 400,
# }

# Configure redis
# First method like this
REDIS_URL = "redis://192.168.56.101:6379"

# Second method like this
# REDIS_HOST =  '127.0.0.1'
# REDIS_PORT =  6379
# if your redis must use password to authenticity, you can configure the REDIS_PASSWORD
# REDIS_PASSWORD =  'your password'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'book.middlewares.JdbookSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'book.middlewares.JdbookDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'book.pipelines.JdbookPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
