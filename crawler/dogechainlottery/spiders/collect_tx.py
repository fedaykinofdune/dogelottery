from scrapy.spider import Spider
from scrapy.selector import Selector
from dogechainlottery.items import TxItem

class CollectTransaction(Spider):
    name = "collect_tx"
    allowed_domains = ["http://dogechain.info"]
    
    def __init__(self, address):
        self.start_urls = ["http://dogechain.info/address/" + address]

    def parse(self, response):
        sel = Selector(response)
        ## skip the first, its the table header
        transactions_tr = sel.xpath("//div[@class='table-responsive']/table/tbody/tr")[1:]
        trs = []

        for tr in transactions_tr:
            item = TxItem()
            item["url"] = tr.xpath(".//td")[0].xpath(".//a/@href")[0].extract()
            item["tx_hash"] = item["url"].split("/")[-1]
            item["amount"] = int(tr.xpath(".//td")[3].select("./text()")[0].extract())
            
            trs.append(item)

        return trs
