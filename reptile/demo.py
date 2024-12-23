import requests
from lxml import etree

url = 'https://www.bilibili.com/'

result = requests.get(url, headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
})
html = etree.HTML(result.text)
statusCode = result.status_code
print(f"status code: {statusCode}")
div = html.xpath('//div[@class="channel-items__left"]')
for item in div:
    print(item.xpath('./a/text()'))

div = html.xpath("//div[@class='bili-feed4']//li")
for item in div:
    print(item.xpath('./a/span/text()'))

