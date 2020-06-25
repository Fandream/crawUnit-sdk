from crawUnit.constants import DataSourceType
from crawUnit.utils.config import get_data_source_type
from crawUnit.utils.data import save_item_mongo, save_item_sql


def save_item(item):
    try:
        if get_data_source_type() == DataSourceType.MONGO:
            save_item_mongo(item)
        else:
            save_item_sql(item)
    except Exception as ex:
        print(ex)
        pass
