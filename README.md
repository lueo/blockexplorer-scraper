blockexplorer-scraper
=====================

Scraping information of received bitcoins from blockexplorer, and submit them to graphite backend - carbon.

**Why scraping web page when there's a JSON API available?**

Simple. Since JSON API will get timeout when there are too many transactions.

In addition, Web page is faster and smaller. A return with JSON format will return every transaction details to you, while web page only list the information you want.

**Why not using blockchain.info instead?**

Some blocks on blockchain.info lacks timestamps. Thus the information is unusable.

**Usage**

1. Create a local_setting.py with the value below

    # Carbon server location
    CARBON_SERVER = '192.168.1.199'
    CARBON_PORT = 2003
    
    # PIPELINE - for sending out metrices to carbon server
    ITEM_PIPELINES = ['bitex.pipelines.BitexPipeline', ]

    # Bitcoin addresses you want to monitor
    BITCOIN_ADDRS = [
                     '1LDLKSADJFOJ298798121FJFLOAJ9J0239',
                     '1LASDJFOU3289U4OGNMRKLGNDNOVGAUOQ4',
                    ]

    # Prefix for your metrices
    METRIC_PREFIX = 'test.addr'
    
2. Execute it!

    scrapy crawl bxspider
    
**Develop**

1. You can add your own pipelines to send the information to anywhere you want. Refer to Scrapy documents.
