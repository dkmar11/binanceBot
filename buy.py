from selenium.webdriver.common.by import By
import time
class Buy:
    def __init__(self, windows) -> None:
        self.windows = windows
    

    def buy(self, seller_goal, max_quantity) -> None:
        seller_goal.button.click()
        time.sleep(2.5)
        quantity_input = self.windows.find_element(By.ID,'C2CofferBuy_amount_input')
        sell_button = self.windows.find_element(By.ID, 'C2CofferBuy__btn_buyNow')
        if max_quantity >= seller_goal.quantity_max:
            quantity_input.send_keys(str(seller_goal.quantity_max))
            print(str(seller_goal.quantity_max))
        else:
            quantity_input.send_keys(str(max_quantity))
            print(max_quantity)

        sell_button.click()