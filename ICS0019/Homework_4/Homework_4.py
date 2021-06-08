import requests
import json
import re
from bs4 import BeautifulSoup

def main():
    start_url = 'https://www.osta.ee/en/category/computers/desktop-computers'


    def parse(start_urls, carryover):
        page = requests.get(start_urls)
        soup = BeautifulSoup(page.text, 'html.parser')
        # print (soup)

        items_list = soup.find('article', class_='category-offers-list__section').find_all("figure", class_='offer-thumb')
        # print(items_list)

        page_items = []

        for item in items_list:
            data = {'title': '', 'price': '', 'picture_href': ''}

            data['title'] = item.find('div', class_='offer-thumb__content').find('h3').text.strip()

            #strip all the annoying whispace from the price string, leave the discounts
            pricestring = re.sub('[ \r\n]+', '', item.find('div', class_='offer-thumb__price--content').text)

            data['price'] = pricestring

            try:
                data['picture_href'] = item.find('a', class_='offer-thumb__link').img['data-original']
            except:
                data['picture_href'] = "no image"


            page_items.append(data)

        if carryover != [] :
            carryover.extend(page_items)
        else:
            carryover = page_items


        try:
            next_page = 'https://www.osta.ee/en/' + soup.find("a", class_='next')['href']
            if next_page:
                print('parsing next page')
                parse(next_page, carryover)
        except:
            print("No more pages")
            print(json.dumps(carryover))
            with open ('osta_pcs.json', 'w') as f:
                json.dump(carryover, f)


    parse(start_url, [])

if __name__ == '__main__':
    main()