# -*- coding: utf-8 -*-
import os
import re
import scrapy
import json
import urllib
from datetime import datetime, date
import csv
import pandas as pd
__author__ = 'Timo'


class HrryItem(scrapy.Item):
    cardname = scrapy.Field()
    hrryprice = scrapy.Field()
    hrrystock = scrapy.Field()
    hrryurl = scrapy.Field()


class HRRYSpider(scrapy.Spider):
    website = u'HRRY'
    type = 'card'
    name = 'hareruya'
    source_type = u'primary'


    def start_requests(self):
        yield scrapy.Request('https://www.mtgjson.com/json/AllCards.json', self.first_page)


    def first_page(self, response):
        f = open("hrry.txt", "r")
        contents = f.read()
        mtgjson = json.loads(response.body) #### DO NOT OPEN THIS
        cardlist = contents.split('\n')
        del cardlist[-1]
        for card in cardlist:
            if mtgjson[card]:
                print(card)
                deets = {}
                if 'purchaseUrls' in mtgjson[card].keys():
                    for market in mtgjson[card]['purchaseUrls']:
                        deets[market] = mtgjson[card]['purchaseUrls'][market]
                deets['cardname'] = card
                url = 'https://www.hareruyamtg.com/en/products/search?product={}&search_x=Search&sort=price&order=ASC&page=1'.format(urllib.parse.quote(card))
                response.meta['deets'] = deets
                yield scrapy.Request(url, self.hrrycardprice, meta = response.meta)
            else:
                print('{} does not exist in MTGJSON. Please check spelling.'.format(card))


    def hrrycardprice(self, response):
        hrrystock = 0
        for i in range(1, len(response.xpath('//*[@id="category_item"]/div[3]/ul/li')) + 1):
            for j in range(0, 4):
                if response.xpath('//*[@id="category_item"]/div[3]/ul/li[{}]/div[1]/div[{}]/div[3]/text()'.format(i, 5 - j)).get() is not None:
                    hrrystock = response.xpath('//*[@id="category_item"]/div[3]/ul/li[{}]/div[1]/div[{}]/div[3]/text()'.format(i, 5 - j)).get()
                else:
                    hrrystock = 0
                hrryprice = response.xpath('//*[@id="category_item"]/div[3]/ul/li[{}]/div[1]/div[{}]/div[2]/text()'.format(i, 5 - j)).get()
                hrryurl = "https://www.hareruyamtg.com" + response.xpath('//*[@id="category_item"]/div[3]/ul/li[{}]/a/@href'.format(i)).get()
                if int(hrrystock) > 0:
                    break
            if int(hrrystock) > 0:
                break
        deets = response.meta['deets']
        deets['hrryprice'] = hrryprice
        deets['hrrystock'] = hrrystock
        deets['hrryurl'] = hrryurl
        item = HrryItem()
        item['cardname'] = deets['cardname']
        item['hrryprice'] = deets['hrryprice']
        item['hrrystock'] = deets['hrrystock']
        item['hrryurl'] = deets['hrryurl']
        yield item
