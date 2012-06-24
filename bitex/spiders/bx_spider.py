from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.conf import settings
from bitex.items import BitexItem
import re
import time

class BXSpider(BaseSpider):
    name = "bxspider"
    urls = "http://blockexplorer.com/address/%s"
    
    start_urls = [urls % addr for addr in settings['BITCOIN_ADDRS']]
    
    def parse(self, response):
        addr = re.search(r'http://.*/.*/(.*$)', response.url).group(1)

        hxs = HtmlXPathSelector(response)
        txs = hxs.select('//table/tr[position()>1]')
        items = []
        for tx in txs:
            if 'Received' in tx.select('./td[4]/text()').extract()[0]:
                item = BitexItem()
                item['addr'] = addr
                t = tx.select('./td[2]/text()').re(r'\((.+)\)')[0]
                item['time'] = time.mktime(time.strptime(t, '%Y-%m-%d %H:%M:%S'))
                item['value'] = float(tx.select('./td[3]/text()').extract()[0])
                items.append(item)
        return items