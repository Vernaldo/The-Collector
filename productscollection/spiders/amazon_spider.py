import scrapy
from ..items import ProductscollectionItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    #allowed_domains = ['amazon.com'] 
    start_urls = [
        'https://www.amazon.com/s?k=Last+30+days&i=computers-intl-ship&crid=1RU46EGJR29T6&sprefix=last+30+days+i%2Ccomputers-intl-ship%2C838&ref=nb_sb_noss'
        ]

    def parse(self, response):
        items = ProductscollectionItem()
        
        all_div_products = response.css('.a-spacing-medium')
        
        for products in all_div_products:
            product_name = products.css('.a-color-base.a-text-normal').css('::text').extract()
            product_price = products.css('.a-price span span::text').extract()
            product_imagelink = products.css('.s-image::attr(src)').extract()
            yield{
                'product_name' : product_name, 
                'product_price' : product_price,
                'product_imagelink' : product_imagelink
            }
    
        
