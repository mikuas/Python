from lxml import etree

htmlData = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>影片介绍</title>
    <style>
        .movie-title {
            font-size: 24px;
            font-weight: bold;
            color: #333;
        }
        .movie-info {
            font-size: 16px;
            color: #666;
        }
        .movie-detail {
            margin-top: 10px;
            font-size: 14px;
            color: #999;
        }
        .highlight {
            color: #ff4500;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="movie-intro">
        <span><p>Hello</p></span>
        <span class="movie-title">《流浪地球》<span>Inter</span></span><br/>
        <span class="movie-info">（2019年上映）</span>
        <div class="movie-detail">
            <span class="highlight">导演：</span><span>郭帆</span><br>
            <span class="highlight">主演：</span><span>吴京, 屈楚萧, 李光洁, 赵今麦,吕受益</span><br>
            <span class="type">类型：</span><span>科幻, 冒险, 灾难</span><br>
            <span class="highlight">国家/地区：</span><span>中国</span><br>
            <span class="highlight">语言：</span><span>汉语普通话</span><br>
            <span class="highlight">上映日期：</span><span>2019-02-05(中国大陆)</span><br>
            <span class="highlight">片长：</span><span>125分钟</span><br>
            <span>片长</span><span>125分钟</span><br>
        </div>
        <div class="movie-detail">
            <span class="highlight">剧情简介：</span><br>
            <span>在未来的太阳急速衰老膨胀，地球面临被吞噬的灭顶之灾。为了拯救地球，人类联合起来在地球表面建造了巨大的推进器，希望将地球推出太阳系，这便是“流浪地球”计划。地球上的所有人都是这个庞大计划的一部分，他们在这颗星球上建起了巨大的推进器，试图将它推出太阳系。然而，在这一过程中，他们面临着一系列的挑战和危险。</span>
        </div>
    </div>
</body>
</html>
"""

page = etree.HTML(htmlData)
data = page.xpath('//div/span')
print(data)
for _ in data:
    print(_.xpath('text()'))
