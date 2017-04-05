# scrapy-demo



# 注意点

## json序列化时汉字编码问题

> 必须加ensure_ascii=False,否则会将汉字变成\u90d的Unicode字符串形式

```
    def __init__(self):
        self.file = open('items2.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
```