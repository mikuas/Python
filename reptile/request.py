import requests
from lxml import etree

url = 'https://movie.douban.com/top250'

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=headers)
html = etree.HTML(resp.text)
myList = html.xpath('//div[@class="info"]')

for item in myList:
    # 标题
    print(f"标题: {item.xpath('./div/a/span/text()')[0]}")
    # 导演
    print(f"导演: {item.xpath('./div/p/text()')[0].strip()}")
    # 评分
    print(f"评分: {item.xpath('//span[@class="rating_num"]/text()')[0]}")

