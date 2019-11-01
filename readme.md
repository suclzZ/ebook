* Scrapy使用：
`
    + 安装scrapy ：
        pip install scrapy
    + 创建项目：
        scrapy startproject 【proj】【dir】
    + 生成spider:
        cd 【proj】
        scrapy genspider 【name】 【domain】
    + 执行：
        scrapy crawl 【name】

        
* 项目参考： 
   
    参考 ：[github scrapy](https://github.com/GuanLdong/QidianScrapy)

* es索引

    /POST /ebook
  {
      "settings": {
        "number_of_shards": 2,
        "number_of_replicas": 1
      },
      "mappings": {
        "novel": {
          "properties": {
            "bid": {
              "type": "keyword"
            },
            "title": {
              "type": "keyword"
            },
            "author": {
              "type": "keyword"
            },
            "types": {
              "type": "text"
            },
            "crtDate": {
              "type": "date",
              "format":"yyyy-MM-dd"
            },
            "pubDate": {
              "type": "date",
              "format":"yyyy-MM-dd"
            },
            "comeFrom":{
              "type":"keyword"	
            },
            "url":{
                "type":"text"	
            },
            "introduction": {
              "type": "text"
            },
            "image": {
              "type": "text",
              "index":false
            },
            "content": {
              "type": "text"
            }
          }
        }
      }
  }