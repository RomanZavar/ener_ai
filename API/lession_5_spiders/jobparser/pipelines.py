# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class JobparserPipeline:
    def __init__(self):
        client = MongoClient(host='localhost', port=27017)
        self.mongo_base = client.vacancy02042024

    def process_item(self, item, spider):

        # item.get('salary')
        # item['min_salary'] = item.get('min_salary)[1]
        colections = self.mongo_base[spider.name]
        colections.insert_one(item)

        return item
