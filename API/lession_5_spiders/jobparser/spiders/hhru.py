import scrapy
from scrapy.http import HtmlResponse

from jobparser.items import JobparserItem
# API.lession_5_spiders.jobparser.spiders


class HhruSpider(scrapy.Spider):
    name = "hhru"
    allowed_domains = ["hh.ru"]
    start_urls = ["https://hh.ru/search/vacancy?text=Python&from=suggest_post&salary=&ored_clusters=true&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line"]
# шесть строк кода с помощью которого можно обработать любой сайт

    def parse(self, response: HtmlResponse):

        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath("//a[@class='bloko-link']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        name = response.xpath("//h1/text()").get()
        salary = response.xpath(
            "//div[@data-qa='vacancy-salary']//text()").getall()
        url = response.url
        yield JobparserItem(name=name, salary=salary, url=url)
