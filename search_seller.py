from typing import Optional
from seller import Seller

class Search_seller:
    def __init__(self, max_price, max_quantity, min_quantity) -> None:
        self.max_price = max_price
        self.max_quantity = max_quantity
        self.min_quantity = min_quantity

    def get(self, sellers) -> Optional[Seller]:
        if len(sellers) != 0:
            for seller in sellers:
                if self.min_quantity <= seller.quantity_max and seller.price <= self.max_price and seller.button_text != 'Limited' and self.max_quantity >= seller.quantity_min:
                    return seller
            return None