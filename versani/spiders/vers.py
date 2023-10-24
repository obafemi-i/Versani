import scrapy
from ..items import VersaniItem

class VersSpider(scrapy.Spider):
    name = "vers"
    allowed_domains = ["versani.com"]
    start_urls = ["https://versani.com/?page=search&subcat=&coll=&size=&brand=&stonetype=&stonecolor=&metl=&clsp=&plat=&colr=&avail=&prange=&sort=&display=&gender=ladies&cat=&m=108&pagenum=1"]
    base_url = 'https://versani.com/'

    def parse(self, response):
        all_links = response.css("a::attr(href)").extract()
        filter = []

        for link in all_links:
            if 'detail' in link:
                filter.append(link)
        
        product_links = [self.base_url+prod for prod in filter]

        for product_link in product_links:
            yield scrapy.Request(product_link, callback=self.get_info)

    def get_info(self, response):
        name = response.css('font::text').extract()[1]
        product_link = response.url
        
        all = response.css('font *::text').extract()

        for any in all:
            if '#' in any:
                style = any

        for some in all:
            if '$' in some:
                price = some
                break

        size = response.css('select#ringsize option::text').extract()
        metal = response.css('select#metalcolor option::text').extract()
        finish = response.css('select#finish option::text').extract()
        collection = response.css('font a::text').extract()[0]

        versanis = VersaniItem()
        versanis['name'] = name
        versanis['price'] = price
        versanis['style'] = style
        versanis['size'] = size
        versanis['metal'] = metal
        versanis['finish'] = finish
        versanis['collection'] = collection
        versanis['product_link'] = product_link

        yield versanis


        for x in range(2, 7):
            url = f"https://versani.com/?page=search&subcat=&coll=&size=&brand=&stonetype=&stonecolor=&metl=&clsp=&plat=&colr=&avail=&prange=&sort=&display=&gender=ladies&cat=&m=108&pagenum={x}"
            yield scrapy.Request(url, callback=self.parse)