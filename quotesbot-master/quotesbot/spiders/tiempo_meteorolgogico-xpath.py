# -*- coding: utf-8 -*-
import scrapy

class TiempoMeteoSpider(scrapy.Spider):
    name = 'tiempoMeteo'
    
    def start_requests(self):
        base_url = "https://www.transfermarkt.es/laliga/startseite/wettbewerb/ES1/saison_id/2018/plus/1"
        yield scrapy.Request(url=(base_url))
        
    def parse(self, response):

        resumen = {
        
        'tabla': response.xpath('//*[@id="yw1_c0"]').extract_first()
        }
        
        yield resumen