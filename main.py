from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from prices import Prices
from quantities import Quantities
from buttons import Buttons
from seller import Seller
from search_seller import Search_seller
from buy import Buy
import time

windows = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
windows.get('https://www.binance.com/en')
while True:
    max_quantity = float(input('Maxima cantidad de compra: '))
    min_quantity = float(input('Minima cantidad de compra: '))
    max_price = float(input('Precio maximo de compra: '))

    sellers = []
    buy_class = Buy(windows)
    prices_class = Prices(windows)
    quantities_class = Quantities(windows)
    buttons_class = Buttons(windows)
    search_seller_class = Search_seller(max_price, max_quantity, min_quantity)
    while True:
        try:
            prices = prices_class.get()
            quantities_min = quantities_class.get_min(prices)
            quantities_max = quantities_class.get_max(prices)
            buttons = buttons_class.get()
            for index in range(len(prices)):
                seller = Seller(prices[index], quantities_max[index], quantities_min[index], buttons[index])
                sellers.append(seller)
        except:
            print('Error al obtener datos')
            time.sleep(0.5)
            continue
        seller_goal = search_seller_class.get(sellers)
        print(prices)
        print(quantities_max)
        print(quantities_min)
        print(seller_goal)
        if seller_goal != None:
            buy_class.buy(seller_goal, max_quantity)
            break
        time.sleep(0.5)