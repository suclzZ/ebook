# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class QidianPipeline(object):
#     def process_item(self, item, spider):
#         return item

from elasticsearch import Elasticsearch
import uuid

# 存储es
class ElasticsearchPipeline(object):
    def __init__(self,node):
        self.node = node

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            node=crawler.settings.get('ES_NODE')
        )

    def open_spider(self,spider):
        self.es = Elasticsearch([self.node])

    def process_item(self,item,spider):
        index = item.index
        type = item.type
        self.es.create(index=index, doc_type=type,id=uuid.uuid1(), body=dict(item))
        return item

    def close_spider(self,spider):
        pass
