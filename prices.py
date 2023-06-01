from selenium.webdriver.common.by import By
from typing import List
class Prices:
    def __init__(self, windows) -> None:
        self.windows = windows

    def get(self) -> list[float]:
        prices = []
        html_prices = self.windows.find_elements(By.CLASS_NAME, 'css-1m1f8hn')
        for element in html_prices:
            prices.append(float(element.text))
        return prices