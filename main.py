# response.css("a::attr(href)").extract()
# pages = response.css("a::attr(href)").extract()
# each = []
# for page in pages:
#     if 'detail' in page:
        # each.append(page)

import requests
from bs4 import BeautifulSoup

# url = 'https://versani.com/?page=search&subcat=&coll=&size=&brand=&stonetype=&stonecolor=&metl=&clsp=&plat=&colr=&avail=&prange=&sort=&display=&gender=ladies&cat=&m=108'

url = 'https://versani.com/?page=detail&par=B1138N&num=B1138N-14'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')

# table = soup.find_all('a')

# print(table)

# name  = response.css('font::text').extract()[1]
name = soup.find_all('font')[8].text

print(name)
all = response.css('font *::text').extract()
for style in all:
    if '#' in style:
        print(style)

for price in all:
    if '$' in price:
        print(price)
        break

images = response.css('img ::attr(src)').extract()
for img in images:
    if '$' in img:
        print(img)
        break
# price = response.css('font::text').extract()[8]

# style = response.css('font::text').extract()[7]

# collection = response.css('font a::text').extract()[0]

# finish = response.css('select#finish option::text').extract()

# metal = response.css('select#metalcolor option::text').extract()

# size = response.css('select#ringsize option::text').extract()