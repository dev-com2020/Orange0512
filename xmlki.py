import csv
import requests
import xml.etree.ElementTree as ET


# def loadRSS():
#     # headers = {'User-Agent': 'Mozilla/5.0'}
#     # url = 'https://www.hindustantimes.com/feeds/rss/advertorial/rssfeed.xml'
#     # resp = requests.get(url, headers=headers)
#     # print(resp.status_code)
#     with open('advertorial.xml', 'rb') as f:



def parseXML(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    newsitems = []
    for item in root.findall('./channel/item'):
        news = {}
        for child in item:
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']

            else:
                news[child.tag] = child.text.encode('utf-8')
        newsitems.append(news)
    return newsitems


def savetoCsv(newsitems, filename):
    fields = ['pubDate', 'title', 'link', 'media', 'guid', 'description']
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(newsitems)


def main():
    # loadRSS()
    newsitem = parseXML('advertorial.xml')
    savetoCsv(newsitem, 'top.csv')

main()
