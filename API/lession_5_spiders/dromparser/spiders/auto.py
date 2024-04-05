import scrapy
from scrapy.http import HtmlResponse
from dromparser.items import DromparserItem


class AutoSpider(scrapy.Spider):
    name = "auto"
    allowed_domains = ["auto.ru"]
    start_urls = ["https://auto.ru/chelyabinsk/cars/all"]

    def parse(self, response: HtmlResponse):

        next_page = response.xpath("//link[@rel='next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath(
            "//a[@class='Link ListingItemTitle__link']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.auto_parse)

    def auto_parse(self, response: HtmlResponse):
        name = response.xpath("//h3/text()").get()
        yers = respone.xpath("//div[@class='ListingItem__year']/text()").get()
        price = response.xpath(
            "//div[@class='ListingItemPrice__content']']//text()").getall()
        url = response.url
        yield JobparserItem(name=name, yers=yers, price=price, url=url)
