# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy.conf import settings
import socket

class BitexPipeline(object):
    def process_item(self, item, spider):
        prefix = settings['METRIC_PREFIX']
        line = '%s.%s %s %s' % (
                                prefix,
                                item['addr'],
                                item['value'],
                                item['time']
                                )
        message = line + '\n'
        self._send_msg(message)
        return item

    def _send_msg(self, message):
        print 'sending message...'
        sock = socket.socket()
        sock.connect((settings['CARBON_SERVER'], settings['CARBON_PORT']))
        sock.sendall(message)
        sock.close()
        print 'done!'
    
