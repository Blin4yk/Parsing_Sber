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
# from selenium.webdriver.chrome.options import Options

# def get_driver():
#     # Создание опций для Chrome
#     options = Options()
#     # Установка пользовательского агента
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

#     # Создание драйвера Chrome с опциями
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     return driver


# BASEURL = 'https://megamarket.ru'


# def get_pages_html(url):
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     ITEMS = []
#     try:
#         for page in range(1, 10):
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
#     items_divs = soup.find_all('div', class_='catalog-items-list')
#     if len(items_divs) == 0:
#         return False
#     for item_div in items_divs:
#         link_element = item_div.find_element_by_xpath('.//a[contains(@class, "ddl_product_link")]')
#         link = BASEURL + link_element.get_attribute('href')

#         price_element = item_div.find_element_by_xpath('.//div[contains(@class, "catalog-item-regular-desktop__price")]')
#         item_price_result = price_element.text

#         item_bonus_element = item_div.find_element_by_xpath('.//div[contains(@class, "money-bonus_loyalty")]')
#         item_bonus_percent = item_bonus_element.find_element_by_xpath('.//span[contains(@class, "bonus-percent")]').text
#         item_bonus_amount = item_bonus_element.find_element_by_xpath('.//span[contains(@class, "bonus-amount")]').text

#         item_title_element = item_div.find_element_by_xpath('.//div[contains(@class, "catalog-item-regular-desktop__main-info")]')
#         item_title = item_title_element.text

#         item_merchant_name_element = item_div.find_element_by_xpath('.//span[contains(@class, "merchant-info__name")]')
#         item_merchant_name = item_merchant_name_element.text if item_merchant_name_element else '-'

#         bonus = int(item_bonus_amount.replace(' ', ''))
#         price = int(item_price_result[0:-1].replace(' ', ''))
#         bonus_percent = int(item_bonus_percent.replace('%', ''))
#         items.append({
#             'Наименование': item_title,
#             'Продавец': item_merchant_name,
#             'Цена': price,
#             'Сумма бонуса': bonus,
#             'Процент бонуса': bonus_percent,
#             'Ссылка на товар': link
#         })
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


# if __name__ == '__main__':
#     main()




#------------------------------------------------------------------------------------------------------------------------------------------------


# import bs4
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


# baseURL = 'https://megamarket.ru'
# target = input('target? ')
# targetURL = baseURL + '/catalog/?q=' + target.replace(' ', '%20')


# def get_source_html(url):
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()

#     try:
#         driver.get(url=url)
#         WebDriverWait(driver, 60).until(
#             ec.presence_of_element_located((By.TAG_NAME, "html")))
#         with open('source-page.html', 'w', encoding='utf-8') as file:
#             file.write(driver.page_source)
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()


# def get_items(file_path):
#     with open(file_path, encoding='utf-8') as file:
#         src = file.read()

#     soup = BeautifulSoup(src, 'lxml')
#     items_divs = soup.find_all('div', class_='catalog-item')

#     items = {}
#     for item in items_divs:
#         item_block = item.find('div', class_='item-block')
#         item_link = item.find('div', class_='item-image')
#         if isinstance(item_link, bs4.element.Tag):
#             link_block = item_link.find('a')
#             start = str(link_block).find('href="')
#             end = str(link_block).find('">', start)
#             link = baseURL + str(link_block)[start+6:end]
#             item_info = item_block.find('div', class_='item-info')
#             item_price_block = item_info.find(
#                 'div', class_='inner catalog-item__prices-container')
#             item_money = item_price_block.find('div', class_='item-money')
#             item_price = item_money.find('div', class_='item-price')
#             item_price_result = item_price.find('span').get_text()
#             item_bonus = item_money.find('div', class_='item-bonus')
#             if isinstance(item_bonus, bs4.element.Tag):
#                 item_bonus_loyalty = item_bonus.find(
#                     'div', class_='money-bonus sm money-bonus_loyalty')
#                 item_bonus_percent = item_bonus_loyalty.find(
#                     'span', class_='bonus-percent').get_text()
#                 item_bonus_amount = item_bonus_loyalty.find(
#                     'span', class_='bonus-amount').get_text()

#                 bonus = int(item_bonus_amount.replace(' ', ''))
#                 price = int(item_price_result[0:-1].replace(' ', ''))
#                 k = round(price / bonus, 3)
#                 items[k] = {'price': item_price_result[0:-2], 'bonus amount':
#                             item_bonus_amount, 'bonus percent': item_bonus_percent,
#                             'link': link}

#     items = dict(sorted(items.items(), key=lambda x: x[0]))
#     return items


# def output(items):
#     for item in items:
#         print(f'{item} - {items[item]}')


# def main():
#     get_source_html(url=targetURL)
#     items = get_items(file_path='source-page.html')
#     output(items)


# if __name__ == '__main__':
#     main()


#------------------------------------------------------------------------------------------------------------------------------------------------------------

# import json
# from urllib import parse
# import pandas as pd
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from selenium.webdriver.edge.service import Service as EdgeService

# BASEURL = 'https://megamarket.ru'

# def get_driver():
#     # Создание сервиса для Microsoft Edge
#     edge_service = EdgeService(EdgeChromiumDriverManager().install())
    
#     # Создание драйвера Microsoft Edge
#     driver = webdriver.Edge(service=edge_service)
#     return driver


# def get_pages_html(url):
#     driver = get_driver()
#     driver.maximize_window()
#     ITEMS = []
#     try:
#         for page in range(2, 10):
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
#     items_divs = soup.find_all('div', class_='catalog-items-list')
#     if len(items_divs) == 0:
#         return False
#     for item in items_divs:
#         link = BASEURL + item.find('a', class_='ddl_product_link').get('href')
#         item_price = item.find('div', class_='catalog-item-regular-desktop__price')
#         if item_price:
#             item_price_result = item_price.get_text()
#             item_bonus = item.find('div', class_='money-bonus_loyalty')
#             if item_bonus:
#                 item_bonus_percent = item.find('span', class_='bonus-percent').get_text()
#                 item_bonus_amount = item.find('span', class_='bonus-amount').get_text()
#                 item_title = item.find('div', class_='catalog-item-regular-desktop__main-info').get_text()
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
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


BASEURL = 'https://megamarket.ru'


def get_driver():
    # Создание опций для Firefox
    options = Options()
    # Установка пользовательского агента
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/97.0")

    # Путь к исполняемому файлу Firefox
    firefox_binary_path = 'geckodriver.exe'

    # Создание драйвера Firefox с опциями
    driver = webdriver.Firefox(executable_path=firefox_binary_path, options=options)
    return driver



def get_pages_html(url):
    driver = get_driver()
    driver.maximize_window()
    ITEMS = []
    try:
        for page in range(1, 10):
            print(f"[+] Страница {page}")
            driver.get(url=url.replace(f'page_num', f'page-{page}'))
            WebDriverWait(driver, 60).until(
                ec.presence_of_element_located((By.TAG_NAME, "html")))
            if not get_items(driver.page_source, ITEMS):
                break
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    return ITEMS


def get_items(html, items):
    soup = BeautifulSoup(html, 'html.parser')
    items_divs = soup.find_all('div', class_='catalog-items-list')
    if len(items_divs) == 0:
        return False
    for item_div in items_divs:
        link_element = item_div.find_element_by_xpath('.//a[contains(@class, "ddl_product_link")]')
        link = BASEURL + link_element.get_attribute('href')

        price_element = item_div.find_element_by_xpath('.//div[contains(@class, "catalog-item-regular-desktop__price")]')
        item_price_result = price_element.text

        item_bonus_element = item_div.find_element_by_xpath('.//div[contains(@class, "money-bonus_loyalty")]')
        item_bonus_percent = item_bonus_element.find_element_by_xpath('.//span[contains(@class, "bonus-percent")]').text
        item_bonus_amount = item_bonus_element.find_element_by_xpath('.//span[contains(@class, "bonus-amount")]').text

        item_title_element = item_div.find_element_by_xpath('.//div[contains(@class, "catalog-item-regular-desktop__main-info")]')
        item_title = item_title_element.text

        item_merchant_name_element = item_div.find_element_by_xpath('.//span[contains(@class, "merchant-info__name")]')
        item_merchant_name = item_merchant_name_element.text if item_merchant_name_element else '-'

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


def main():
    target = input('Введите название товара: ')
    min_price = input('Минимальная цена (enter, чтобы пропустить): ')
    min_price = min_price if min_price != '' else '0'
    max_price = input('Максимальная цена (enter, чтобы пропустить): ')
    max_price = max_price if max_price != '' else '9999999'
    target_url = f"{BASEURL}/catalog/page_num/{target}"
    if max_price and min_price and (max_price.isdigit() and min_price.isdigit()):
        filter = {
            "88C83F68482F447C9F4E401955196697": {"min": int(min_price), "max": int(max_price)},# фильтр по цене
            "4CB2C27EAAFC4EB39378C4B7487E6C9E": ["1"]}# фильтр по наличию товара
        json_data = json.dumps(filter)
        # Кодирование JSON строки для передачи через URL
        url_encoded_data = parse.quote(json_data)
        target_url += '#?filters=' + url_encoded_data

    items = get_pages_html(url=target_url)
    save_excel(items, target)


if __name__ == '__main__':
    main()
