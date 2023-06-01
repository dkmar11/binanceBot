from selenium.webdriver.common.by import By
from typing import List
import re

class Quantities:
    def __init__(self, windows) -> None:
        self.windows = windows

    def get_max(self, prices) -> list[float]:
    
        max_quantity = []
        for index in range(1, len(prices)+1):
            xpath = f'//*[@id="__APP"]/div[2]/main/div[1]/div[4]/div/div[2]/div[{index}]/div[1]/div[3]/div/div[2]/div[2]/div[3]'
            html_max_quantity = self.windows.find_element(By.XPATH, xpath)
            max_quantity.append(html_max_quantity.text)
            
        return self.to_float(max_quantity)

    def get_min(self, prices) -> list[float]:

        min_quantity = []
        for index in range(1, len(prices)+1):
            xpath = f'//*[@id="__APP"]/div[2]/main/div[1]/div[4]/div/div[2]/div[{index}]/div[1]/div[3]/div/div[2]/div[2]/div[1]'
            html_min_quantity = self.windows.find_element(By.XPATH, xpath)
            min_quantity.append(html_min_quantity.text)

        return self.to_float(min_quantity)

    def to_float(self, array) -> list[float]:

        pattern = r'[-+]?\$?\n?(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d+)?|\.\d+)'
        result = []
        for elemento in array:
            match = re.search(pattern, elemento)
            if match:
                number = match.group()
                number_cleaned = re.sub(r'[^\d.]', '', number)
                result.append(float(number_cleaned))

        return result