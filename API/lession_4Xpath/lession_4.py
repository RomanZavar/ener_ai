# from lxml import etree

# tree = etree.parse('API/lession_4Xpath/web_page.html')

# html = tree.getroot()

# title_element = tree.xpath('//p/text()')[0]

# print(title_element)

# list_items = tree.xpath('//ul/descendant::li')


# for li in list_items:
# text = "".join(map(str.strip, li.xpath('.//text()')))
# print(text)


# title_element = html.cssselect('p')
# print(title_element[0].text)


import requests
from lxml import html

resp = requests.get(url='https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm',
                    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'})

tree = html.fromstring(html=resp.coontent)
print(resp.status_code)
