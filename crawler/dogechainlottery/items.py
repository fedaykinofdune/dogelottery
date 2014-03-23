# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class TxItem(Item):
    url = Field()
    tx_hash = Field()
    source_address = Field()
    amount = Field()

class DogechainlotteryItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass
