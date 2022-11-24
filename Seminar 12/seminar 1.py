import xml.etree.ElementTree as ET
import requests

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
# https://cbr.ru/scripts/XML_daily.asp?date_req=14/12/2014
params = {'date_req': '14/12/2014'}
# response = requests.get(url)
new_session = requests.Session()
# hh.ru/1
# hh.ru/1
response = new_session.get(url, params=params)
# print(response.status_code)
# if response.status_code == 200:

if response.ok:
    # print(response.headers)
    # print(response.cookies)
    # print(response.text)
    # print(response.content)
    # print(response.ok)
    crb_xml = response.text
    cur_root = ET.fromstring(crb_xml)
    print(cur_root.tag)
    # print(cur_root.text)
    print(cur_root.attrib)
    print(cur_root.attrib['Date'])
    # for i in cur_root:
    #     print(i.tag)
    #     print(i.text)
    #     print(i.attrib)

    # print(cur_root[0].tag)
    # print(cur_root[0].attrib)

    # for i in cur_root.findall('Valute'):
    #     cur_name = i.find('Name').text
    #     cur_nom = i.find('Nominal').text
    #     cur_char = i.find('CharCode').text
    #     cur_val = i.find('Value').text
    #     print(cur_name, cur_nom, cur_char, cur_val)

    cny_find = cur_root.find("Valute[CharCode='CNY']")
    print(cny_find.attrib)
    yen_name = cny_find.findtext('Name')
    yen_nom = cny_find.findtext('Nominal')
    yen_char = cny_find.findtext('CharCode')
    yen_val = cny_find.findtext('Value')
    print(yen_name, yen_nom, yen_char, yen_val)
    yen_nom = int(yen_nom)
    yen_val = float(yen_val.replace(',', '.'))

    cny = 100
    rub = cny * yen_val / yen_nom
    print(round(rub, 2))
    print(f'CN\u00A5{cny} = {round(rub, 2)}\u20BD')
    print('\u5143')

#     U+5143



