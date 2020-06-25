# CrawUnit 的 Python SDK


CrawUnit 的 Python SDK 主要由为与CrawUnit更好集成而开发


## Utility 工具

Utility 工具主要提供一些 `Helper` 方法来让爬虫更好的集成到 crawUnit 中，例如保存结果数据到 crawUnit 中等等。

下面是 Scrapy 和一般 Python 爬虫与 crawUnit 集成的方式。


##### Scrapy 集成

在 `settings.py` 中找到 `ITEM_PIPELINES`（`dict` 类型的变量），在其中添加如下内容。

```python
ITEM_PIPELINES = {
    'crawUnit.pipelines.crawUnitMongoPipeline': 888,
}
```

然后，启动 Scrapy 爬虫，运行完成之后，就应该能看到抓取结果出现在 [任务详情-结果](../Task/View.md) 里。

##### 通用 Python 爬虫集成

将下列代码加入到您爬虫中的结果保存部分。

```python
# 引入保存结果方法
from crawUnit import save_item

# 这是一个结果，需要为 dict 类型
result = {'name': 'crawUnit'}

# 调用保存结果方法
save_item(result)
```

然后，启动爬虫，运行完成之后，就应该能看到抓取结果出现在 [任务详情-结果](../Task/View.md) 里。
