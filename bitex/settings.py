# Scrapy settings for bitex project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'bitex'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['bitex.spiders']
NEWSPIDER_MODULE = 'bitex.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

### All SETTINGS BELOW COULD BE OVERRIDED in local_settings.py

# Carbon server location
CARBON_SERVER = '127.0.0.1'
CARBON_PORT = 2003

# PIPELINE - for sending out metrices to carbon server
ITEM_PIPELINES = []
# Bitcoin addresses you want to monitor
BITCOIN_ADDRS = []
# Prefix for your metrices
METRIC_PREFIX = ''

try:
    from local_settings import *
except ImportError:
    pass