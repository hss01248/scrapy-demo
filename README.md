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

## 图片下载的pipeline不起作用

> 要关掉ROBOTSTXT_OBEY,否则，一些防爬虫爬数据的页面下载不了图片
ROBOTSTXT_OBEY = False
默认为True，就是要遵守robots.txt 的规则,通俗来说， robots.txt 是遵循 Robot协议 的一个文件，
它保存在网站的服务器中，它的作用是，告诉搜索引擎爬虫，本网站哪些目录下的网页 不希望 你进行爬取收录。在Scrapy启动后，
会在第一时间访问网站的 robots.txt 文件，然后决定该网站的爬取范围.在某些情况下我们想要获取的内容恰恰是被 robots.txt 所禁止访问的。
所以，某些时候，我们就要将此配置项设置为 False ，拒绝遵守 Robot协议 ！