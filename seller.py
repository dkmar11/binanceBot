class Seller:
    def __init__(self, price, max, min, button) -> None:
        self.price = price
        self.quantity_max = max
        self.quantity_min = min
        self.button = button
        self.button_text = button.text