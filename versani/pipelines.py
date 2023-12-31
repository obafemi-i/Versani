# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class VersaniPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # remove white space from value of price
        value = adapter.get('price')
        adapter['price'] = value.strip()

        # style cleanup
        value = adapter.get('style')
        adapter['style'] = value.replace('Style # ', '')

        # finish cleanup
        value = adapter.get('finish')
        if len(value) == 0:
            adapter['finish'] = 'None'

        # size cleanup
        value = adapter.get('size')
        if len(value) == 0:
            adapter['size'] = 'None'

        return item
