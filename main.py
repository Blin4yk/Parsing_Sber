# import json
# from urllib import parse
# import pandas as pd
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


# #https://megamarket.ru/catalog/iphone-15/#?related_search=iphone%2015&filters=%7B%224CB2C27EAAFC4EB39378C4B7487E6C9E%22%3A%5B%221%22%5D%2C%2288C83F68482F447C9F4E401955196697%22%3A%7B%22min%22%3A90000%7D%7Dmax"%3A350000%7D%7D
# #https://megamarket.ru/catalog/page-1/iphone%2015/#?filters=%7B%2288C83F68482F447C9F4E401955196697%22%3A%20%7B%22min%22%3A%2090000%2C%20%22max%22%3A%20350000%7D%2C%20%224CB2C27EAAFC4EB39378C4B7487E6C9E%22%3A%20%5B%221%22%5D%7D
# #https://megamarket.ru/catalog/page-1/iphone%2015/#?filters=%7B%2288C83F68482F447C9F4E401955196697%22%3A%20%7B%22min%22%3A%200%2C%20%22max%22%3A%209999999%7D%2C%20%224CB2C27EAAFC4EB39378C4B7487E6C9E%22%3A%20%5B%221%22%5D%7D

# BASEURL = 'https://megamarket.ru'


# def get_pages_html(url):
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     ITEMS = []
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
#     try:
#         for page in range(1, 100):
#             print(f"[+] Страница {page}")
#             driver.get(url=url.replace(f'page_num', f'page-{page}'))
#             WebDriverWait(driver, 60).until(
#                 ec.presence_of_element_located((By.TAG_NAME, "html")))
#             if not get_items(driver.page_source, ITEMS):
#                 break
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()
#     return ITEMS


# def get_items(html, items):
#     soup = BeautifulSoup(html, 'html.parser')
#     items_divs = soup.find_all('div', class_='catalog-item-list')
#     if len(items_divs) == 0:
#         return False
#     for item in items_divs:
#         link = BASEURL + item.find('a', class_='ddl_product_link').get('href')
#         item_price = item.find('div', class_='product-list-item-price')
#         if item_price:
#             item_price_result = item_price.find('span').get_text()
#             item_bonus = item.find('div', class_='money-bonus sm money-bonus_loyalty')
#             if item_bonus:
#                 item_bonus_percent = item.find('span', class_='bonus-percent').get_text()
#                 item_bonus_amount = item.find('span', class_='bonus-amount').get_text()
#                 item_title = item.find('div', class_='product-list-item-title').get_text()
#                 item_merchant_name = item.find('span', class_='merchant-info__name')
#                 if item_merchant_name:
#                     item_merchant_name = item_merchant_name.get_text()
#                 else:
#                     item_merchant_name = '-'

#                 bonus = int(item_bonus_amount.replace(' ', ''))
#                 price = int(item_price_result[0:-1].replace(' ', ''))
#                 bonus_percent = int(item_bonus_percent.replace('%', ''))
#                 items.append({
#                     'Наименование': item_title,
#                     'Продавец': item_merchant_name,
#                     'Цена': price,
#                     'Сумма бонуса': bonus,
#                     'Процент бонуса': bonus_percent,
#                     'Ссылка на товар': link
#                 })
#     return True


# def save_excel(data: list, filename: str):
#     """сохранение результата в excel файл"""
#     df = pd.DataFrame(data)
#     writer = pd.ExcelWriter(f'{filename}.xlsx')
#     df.to_excel(writer, sheet_name='data', index=False)
#     # указываем размеры каждого столбца в итоговом файле
#     writer.sheets['data'].set_column(0, 1, width=50)
#     writer.sheets['data'].set_column(1, 2, width=30)
#     writer.sheets['data'].set_column(2, 3, width=8)
#     writer.sheets['data'].set_column(3, 4, width=20)
#     writer.sheets['data'].set_column(4, 5, width=15)
#     writer.close()
#     print(f'Все сохранено в {filename}.xlsx')


# # def main():
# #     target = input('Введите название товара: ')
# #     min_price = input('Минимальная цена (enter, чтобы пропустить): ')
# #     min_price = min_price if min_price != '' else '0'
# #     max_price = input('Максимальная цена (enter, чтобы пропустить): ')
# #     max_price = max_price if max_price != '' else '9999999'
# #     target_url = f"{BASEURL}/catalog/page_num/{target}"
# #     if max_price and min_price and (max_price.isdigit() and min_price.isdigit()):
# #         filter = {
# #             "88C83F68482F447C9F4E401955196697": {"min": int(min_price), "max": int(max_price)},# фильтр по цене
# #             "4CB2C27EAAFC4EB39378C4B7487E6C9E": ["1"]}# фильтр по наличию товара
# #         json_data = json.dumps(filter)
# #         # Кодирование JSON строки для передачи через URL
# #         url_encoded_data = parse.quote(json_data)
# #         target_url += '#?filters=' + url_encoded_data

# #     items = get_pages_html(url=target_url)
# #     save_excel(items, target)

# def main():
#     target = input('Введите название товара: ')
#     min_price = input('Минимальная цена (enter, чтобы пропустить): ')
#     min_price = min_price if min_price != '' else '0'
#     max_price = input('Максимальная цена (enter, чтобы пропустить): ')
#     max_price = max_price if max_price != '' else '9999999'

#     # Собираем URL для поиска с указанными фильтрами
#     # target_url = f"{BASEURL}/catalog/page-1/{parse.quote(target)}/#"
#     target_url = "https://megamarket.ru/catalog/iphone-15/#?related_search=iphone%2015&filters=%7B%224CB2C27EAAFC4EB39378C4B7487E6C9E%22%3A%5B%221%22%5D%2C%2288C83F68482F447C9F4E401955196697%22%3A%7B%22min%22%3A90000%2C%22max%22%3A350000%7D%7D"

#     if max_price.isdigit() and min_price.isdigit():
#         # Формируем фильтр
#         filter_data = {
#             "88C83F68482F447C9F4E401955196697": {"min": int(min_price), "max": int(max_price)},  # фильтр по цене
#             "4CB2C27EAAFC4EB39378C4B7487E6C9E": ["1"]  # фильтр по наличию товара
#         }
#         # Кодируем фильтр в формат JSON и затем в URL
#         url_encoded_data = parse.quote(json.dumps(filter_data))
#         # Добавляем закодированные данные фильтра к target_url
#         target_url += f'?filters={url_encoded_data}'

#     items = get_pages_html(url=target_url)
#     save_excel(items, target)




# if __name__ == '__main__':
#     main()







import json
from urllib import parse
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#https://megamarket.ru/catalog/iphone-15/#?related_search=iphone%2015&filters=%7B%224CB2C27EAAFC4EB39378C4B7487E6C9E%22%3A%5B%221%22%5D%2C%2288C83F68482F447C9F4E401955196697%22%3A%7B%22min%22%3A90000%7D%7Dmax"%3A350000%7D%7D
#https://megamarket.ru/catalog/page-1/iphone%2015/#?filters=%7B%2288C83F68482F447C9F4E401955196697%22%3A%20%7B%22min%22%3A%2090000%2C%20%22max%22%3A%20350000%7D%2C%20%224CB2C27EAAFC4EB39378C4B7487E6C9E%22%3A%20%5B%221%22%5D%7D
#https://megamarket.ru/catalog/page-1/iphone%2015/#?filters=%7B%2288C83F68482F447C9F4E401955196697%22%3A%20%7B%22min%22%3A%200%2C%20%22max%22%3A%209999999%7D%2C%20%224CB2C27EAAFC4EB39378C4B7487E6C9E%22%3A%20%5B%221%22%5D%7D

BASEURL = 'https://megamarket.ru'


def get_pages_html(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    ITEMS = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    try:
        print(f"[+] Страница ")
        driver.get(url=url)
        WebDriverWait(driver, 60).until(
            ec.presence_of_element_located((By.TAG_NAME, "html")))
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    return ITEMS


def get_items(html, items):
    soup = BeautifulSoup(html, 'html.parser')
    items_divs = soup.find_all('div', class_='catalog-item-list')
    if len(items_divs) == 0:
        return False
    for item in items_divs:
        link = BASEURL + item.find('a', class_='ddl_product_link').get('href')
        item_price = item.find('div', class_='product-list-item-price')
        if item_price:
            item_price_result = item_price.find('span').get_text()
            item_bonus = item.find('div', class_='money-bonus sm money-bonus_loyalty')
            if item_bonus:
                item_bonus_percent = item.find('span', class_='bonus-percent').get_text()
                item_bonus_amount = item.find('span', class_='bonus-amount').get_text()
                item_title = item.find('div', class_='product-list-item-title').get_text()
                item_merchant_name = item.find('span', class_='merchant-info__name')
                if item_merchant_name:
                    item_merchant_name = item_merchant_name.get_text()
                else:
                    item_merchant_name = '-'

                bonus = int(item_bonus_amount.replace(' ', ''))
                price = int(item_price_result[0:-1].replace(' ', ''))
                bonus_percent = int(item_bonus_percent.replace('%', ''))
                items.append({
                    'Наименование': item_title,
                    'Продавец': item_merchant_name,
                    'Цена': price,
                    'Сумма бонуса': bonus,
                    'Процент бонуса': bonus_percent,
                    'Ссылка на товар': link
                })
    return True


def save_excel(data: list, filename: str):
    """сохранение результата в excel файл"""
    df = pd.DataFrame(data)
    writer = pd.ExcelWriter(f'{filename}.xlsx')
    df.to_excel(writer, sheet_name='data', index=False)
    # указываем размеры каждого столбца в итоговом файле
    writer.sheets['data'].set_column(0, 1, width=50)
    writer.sheets['data'].set_column(1, 2, width=30)
    writer.sheets['data'].set_column(2, 3, width=8)
    writer.sheets['data'].set_column(3, 4, width=20)
    writer.sheets['data'].set_column(4, 5, width=15)
    writer.close()
    print(f'Все сохранено в {filename}.xlsx')


# def main():
#     target = input('Введите название товара: ')
#     min_price = input('Минимальная цена (enter, чтобы пропустить): ')
#     min_price = min_price if min_price != '' else '0'
#     max_price = input('Максимальная цена (enter, чтобы пропустить): ')
#     max_price = max_price if max_price != '' else '9999999'
#     target_url = f"{BASEURL}/catalog/page_num/{target}"
#     if max_price and min_price and (max_price.isdigit() and min_price.isdigit()):
#         filter = {
#             "88C83F68482F447C9F4E401955196697": {"min": int(min_price), "max": int(max_price)},# фильтр по цене
#             "4CB2C27EAAFC4EB39378C4B7487E6C9E": ["1"]}# фильтр по наличию товара
#         json_data = json.dumps(filter)
#         # Кодирование JSON строки для передачи через URL
#         url_encoded_data = parse.quote(json_data)
#         target_url += '#?filters=' + url_encoded_data

#     items = get_pages_html(url=target_url)
#     save_excel(items, target)

def main():
    target = input('Введите название товара: ')
    min_price = input('Минимальная цена (enter, чтобы пропустить): ')
    min_price = min_price if min_price != '' else '0'
    max_price = input('Максимальная цена (enter, чтобы пропустить): ')
    max_price = max_price if max_price != '' else '9999999'

    # Собираем URL для поиска с указанными фильтрами
    # target_url = f"{BASEURL}/catalog/page-1/{parse.quote(target)}/#"
    target_url = "https://megamarket.ru/catalog/iphone-15/#?related_search=iphone%2015&filters=%7B%224CB2C27EAAFC4EB39378C4B7487E6C9E%22%3A%5B%221%22%5D%2C%2288C83F68482F447C9F4E401955196697%22%3A%7B%22min%22%3A90000%2C%22max%22%3A350000%7D%7D"

    if max_price.isdigit() and min_price.isdigit():
        # Формируем фильтр
        filter_data = {
            "88C83F68482F447C9F4E401955196697": {"min": int(min_price), "max": int(max_price)},  # фильтр по цене
            "4CB2C27EAAFC4EB39378C4B7487E6C9E": ["1"]  # фильтр по наличию товара
        }
        # Кодируем фильтр в формат JSON и затем в URL
        url_encoded_data = parse.quote(json.dumps(filter_data))
        # Добавляем закодированные данные фильтра к target_url
        target_url += f'?filters={url_encoded_data}'

    items = get_pages_html(url=target_url)
    save_excel(items, target)




if __name__ == '__main__':
    main()

