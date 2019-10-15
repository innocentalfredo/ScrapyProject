
import scrapy
from ..items import HarrierItem

class Toyota(scrapy.Spider):
    name = 'harrier'
    allowed_urls = ['https://www.tradecarview.com']
    start_urls = [
        'https://www.tradecarview.com/used_car/toyota/harrier/?gfr=topsidemenu'
    ]

    def parse(self, response):

        #allveh = response.css('div.vehicle-item-pic-block')
        allveh = response.css('div.vehicle-list-area')
        for vehicle in allveh:
            year = vehicle.css('div.main-info-body::text').extract()
            # year = vehicle.css('div.main-info-body::text')[0].extract()
            engine = vehicle.css('div.main-info-body::text').extract()
            mileage = vehicle.css('div.main-info-body::text').extract()
            fob_price = vehicle.css('div.main-info-body::text').extract()

            items = HarrierItem()

            items['year'] = year
            items['engine'] = engine
            items['mileage'] = mileage
            items['fob_price'] = fob_price
            yield items





