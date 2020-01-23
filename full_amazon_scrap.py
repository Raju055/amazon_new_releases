import pandas as pd
import requests
from bs4 import BeautifulSoup as soup
import csv
import json


def html_parser(url):
    url_request = requests.get(url)
    page_soup = soup(url_request.content, 'html5lib')
    # print(soup.prettify(page_soup))
    container = page_soup.findAll('ul', {'id': 'zg_browseRoot'})
    print(len(container))

    table = container[0].findAll('ul')

    all_item_list = table[len(table) - 1].findAll('li')
    print(len(all_item_list))
    return all_item_list


def write_to_csv(file_name, item_url, cat_1, cat_2, cat_3, cat_4, cat_5, cat_6, cat_7, cat_8):

    select = True
    with open(file_name, 'a') as f:
        df = pd.DataFrame.to_csv(f, header=False)
    df = df.append(
        {'select': select, 'amazon_url': item_url, 'cat1': cat_1, 'cat2': cat_2, 'cat3': cat_3,
         'cat4': cat_4, 'cat5': cat_5, 'cat6': cat_6, 'cat7': cat_7, 'cat8': cat_8}, ignore_index=True)
    df.to_csv(file_name)


def main():
    file_name = 'amazon_hot_releases.csv'
    dfObj = pd.DataFrame(
        columns=['select', 'amazon_url', 'cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat6', 'cat7', 'cat8'])
    dfObj.to_csv(file_name)

    main_url = 'https://www.amazon.com/gp/new-releases/ref=zg_bs_tab'
    item_list = html_parser(main_url)

    for item1 in range(0, len(item_list) - 1):
        item_cat1_url = item1.find('a').attrs['href']
        cat1 = item1.text.strip()
        cat2 = ''
        cat3 = ''
        cat4 = ''
        cat5 = ''
        cat6 = ''
        cat7 = ''
        cat8 = ''
        write_to_csv(file_name, item_cat1_url, cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8)

        item_cat2 = html_parser(item_cat1_url)
        for item2 in range(0, len(item_cat2) - 1):
            item_cat2_url = item2.find('a').attrs['href']
            cat2 = item2.text.strip()
            write_to_csv(file_name, item_cat1_url, cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8)

            item_cat3 = html_parser(item_cat2_url)
            for item3 in range(0, len(item_cat3) - 1):
                item_cat3_url = item3.find('a').attrs['href']
                cat3 = item3.text.strip()
                write_to_csv(file_name, item_cat1_url, cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8)

                item_cat4 = html_parser(item_cat3_url)
                for item4 in range(0, len(item_cat4) - 1):
                    item_cat4_url = item4.find('a').attrs['href']
                    cat4 = item4.text.strip()
                    write_to_csv(file_name, item_cat1_url, cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8)

                    item_cat5 = html_parser(item_cat4_url)
                    for item5 in range(0, len(item_cat5) - 1):
                        item_cat5_url = item5.find('a').attrs['href']
                        cat5 = item5.text.strip()
                        write_to_csv(file_name, item_cat1_url, cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8)

                        item_cat6 = html_parser(item_cat5_url)
                        for item6 in range(0, len(item_cat5) - 1):
                            item_cat6_url = item6.find('a').attrs['href']
                            cat6 = item6.text.strip()
                            write_to_csv(file_name, item_cat1_url, cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8)

                            item_cat7 = html_parser(item_cat6_url)
                            for item7 in range(0, len(item_cat5) - 1):
                                item_cat7_url = item7.find('a').attrs['href']
                                cat7 = item7.text.strip()
                                write_to_csv(file_name, item_cat1_url, cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8)

                                item_cat7 = html_parser(item_cat6_url)
                                for item8 in range(0, len(item_cat7) - 1):
                                    item_cat4_url = item8.find('a').attrs['href']
                                    cat8 = item8.text.strip()
                                    write_to_csv(file_name, item_cat1_url, cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8)

if __name__ == '__main__':
    main()
