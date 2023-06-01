from selenium.webdriver.common.by import By

class Buttons:
    def __init__(self, windows) -> None:
        self.windows = windows

    def get(self) -> list:
        html_buttons = self.windows.find_elements(By.ID, 'C2CofferBuy__btn')
        return html_buttons