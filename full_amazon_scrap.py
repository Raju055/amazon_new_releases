import pandas as pd
import requests
from bs4 import BeautifulSoup as soup

def html_parser(url):
    url_request = requests.get(url)
    page_soup = soup(url_request.content, 'html5lib')   
    container = page_soup.findAll('ul', {'id': 'zg_browseRoot'})  
    try:
        table = container[len(container)-1].findAll('ul')
    except Exception:
        pass
    try:
        all_item_list = table[len(table) - 1].findAll('li') 
    except Exception:
        all_item_list = []
        pass
    return all_item_list

def write_to_csv( x, item_url, cat_1, cat_2, cat_3, cat_4, cat_5, cat_6, cat_7, cat_8):
    select = True
    if x == 1:
        global file_name
        global dfObj
        file_name = 'amazon_hot_releases.csv'
        dfObj = pd.DataFrame(
            columns=['select', 'amazon_url', 'cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat6', 'cat7', 'cat8'])
        dfObj.to_csv(file_name)

#    with open(file_name, 'a') as f:
#        dfObj = dfObj.to_csv(f, header=True)
    dfObj = dfObj.append(
        {'select': select, 'amazon_url': item_url, 'cat1': cat_1, 'cat2': cat_2, 'cat3': cat_3,
         'cat4': cat_4, 'cat5': cat_5, 'cat6': cat_6, 'cat7': cat_7, 'cat8': cat_8}, ignore_index=True)
    dfObj.to_csv(file_name)

def main():
    i = 1
    main_url = 'https://www.amazon.com/gp/new-releases/ref=zg_bs_tab'
    item_cat1 = html_parser(main_url)
    for index1, item1 in enumerate(item_cat1):  # for index1, item1 in enumerate(item_list): #  for item1 in range(0, len(item_list) - 1):
        try:
            item_cat1_url = item1.find('a').attrs['href']
            cat1 = item1.text.strip()
            cat2 = ''
            cat3 = ''
            cat4 = ''
            cat5 = ''
            cat6 = ''
            cat7 = ''
            cat8 = ''
            write_to_csv( i, item_cat1_url, cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8 )
            i += 1

            item_cat2 = html_parser(item_cat1_url)
            for index2, item2 in enumerate(item_cat2):
                try:
                    item_cat2_url = item2.find('a').attrs['href']
                    cat2 = item2.text.strip()
                    write_to_csv(i, item_cat2_url, cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8)

                    item_cat3 = html_parser(item_cat2_url)
                    for index3, item3 in enumerate(item_cat3):
                        try:
                            item_cat3_url = item3.find('a').attrs['href']
                            cat3 = item3.text.strip()
                            write_to_csv(i, item_cat3_url, cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8)

                            item_cat4 = html_parser(item_cat3_url)
                            for index4, item4 in enumerate(item_cat4):
                                try:
                                    item_cat4_url = item4.find('a').attrs['href']
                                    cat4 = item4.text.strip()
                                    write_to_csv(i, item_cat4_url, cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8)

                                    item_cat5 = html_parser(item_cat4_url)
                                    for index5, item5 in enumerate(item_cat5):
                                        try:
                                            item_cat5_url = item5.find('a').attrs['href']
                                            cat5 = item5.text.strip()
                                            write_to_csv(i, item_cat5_url, cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8)

                                            item_cat6 = html_parser(item_cat5_url)
                                            for index6, item6 in enumerate(item_cat6):
                                                try:
                                                    item_cat6_url = item6.find('a').attrs['href']
                                                    cat6 = item6.text.strip()
                                                    write_to_csv(i, item_cat6_url, cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8)

                                                    item_cat7 = html_parser(item_cat6_url)
                                                    for index7, item7 in enumerate(item_cat7):
                                                        try:
                                                            item_cat7_url = item7.find('a').attrs['href']
                                                            cat7 = item7.text.strip()
                                                            write_to_csv(i, item_cat7_url, cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8)

                                                            item_cat8 = html_parser(item_cat7_url)
                                                            for index8, item8 in enumerate(item_cat8):
                                                                try:
                                                                    item_cat8_url = item8.find('a').attrs['href']
                                                                    cat8 = item8.text.strip()
                                                                    write_to_csv(i, item_cat8_url, cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8)
                                                                except Exception:
                                                                    break
                                                        except Exception:
                                                            break
                                                except Exception:
                                                    break
                                        except Exception:
                                            break
                                except Exception:
                                    break
                        except Exception:
                            break
                except Exception:
                    break
        except Exception :
            break
if __name__ == '__main__':
    main()
