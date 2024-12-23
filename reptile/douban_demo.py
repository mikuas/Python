import requests
from lxml import etree


def getData(pageNumber=0):
    url = f"https://movie.douban.com/top250?start={str(25 * pageNumber)}&filter="

    result = requests.get(url, headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }, proxies={
        'http': 'https://127.0.0.1:10809',
        # 'https': 'https://127.0.0.1:10809'
    })

    print(f"status_code: {result.status_code}")

    html = etree.HTML(result.text)
    div = html.xpath('//div[@class="info"]')
    for item in div:
        print(f"名称: {item.xpath('./div/a/span/text()')[0]}")
        print(item.xpath('./div/p/text()')[0].strip())
        print(f"评分: {item.xpath('./div//div[@class="star"]/span/text()')[0]}", end='\n\n')
    print('------------------------------')

for i in range(15):
    print(f"第{i + 1}页的内容")
    getData(i)