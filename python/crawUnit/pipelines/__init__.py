from crawUnit.db import col
from crawUnit.utils import save_item_mongo
from crawUnit.utils.config import get_task_id


class CrawlabMongoPipeline(object):
    def process_item(self, item, spider):
        item_dict = dict(item)
        item_dict['task_id'] = get_task_id()
        save_item_mongo(item_dict)

        return item
