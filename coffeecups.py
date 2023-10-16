import tkinter as tk
from tkinter import PhotoImage


coffee_prices = {
    "Espresso": {"Small": 2.00, "Medium": 2.50, "Large": 3.00},
    "Cappuccino": {"Small": 3.00, "Medium": 3.50, "Large": 4.00},
    "Latte": {"Small": 3.50, "Medium": 4.00, "Large": 4.50},
    "Mocha": {"Small": 3.50, "Medium": 4.00, "Large": 4.50},
    "Americano": {"Small": 2.50, "Medium": 3.00, "Large": 3.50},
}

class CoffeePriceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Price Calculator")

        
        background_image = PhotoImage(file="coffee.gif")  # Use the converted GIF image
        background_label = tk.Label(root, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        self.coffee_choice = tk.StringVar()
        self.size_choice = tk.StringVar()
        self.total_price = tk.DoubleVar()
        self.total_cups = tk.IntVar()

        coffee_label = tk.Label(root, text="Select Coffee:", bg="brown")
        coffee_label.pack()
        coffee_dropdown = tk.OptionMenu(root, self.coffee_choice, *coffee_prices.keys())
        coffee_dropdown.pack()

        size_label = tk.Label(root, text="Select Size:", bg="brown")
        size_label.pack()
        size_dropdown = tk.OptionMenu(root, self.size_choice, "Small", "Medium", "Large")
        size_dropdown.pack()

        add_to_cart_button = tk.Button(root, text="Add to Cart", command=self.add_to_cart)
        add_to_cart_button.pack(pady=10)

        clear_button = tk.Button(root, text="Clear", command=self.clear_cart)
        clear_button.pack()

        result_label = tk.Label(root, text="Total Price:", bg="brown")
        result_label.pack()
        result_display = tk.Label(root, textvariable=self.total_price, bg="brown")
        result_display.pack()

        cups_label = tk.Label(root, text="Total Cups of Coffee:", bg="brown")
        cups_label.pack()
        cups_display = tk.Label(root, textvariable=self.total_cups, bg="brown")
        cups_display.pack()

        self.cart = []

        background_image.image = background_image  

    def add_to_cart(self):
        coffee = self.coffee_choice.get()
        size = self.size_choice.get()

        if coffee in coffee_prices and size in coffee_prices[coffee]:
            price = coffee_prices[coffee][size]
            self.cart.append({"coffee": coffee, "size": size, "price": price})
            self.total_price.set(sum(item["price"] for item in self.cart))
            self.total_cups.set(len(self.cart))

    def clear_cart(self):
        self.cart = []
        self.total_price.set(0.0)
        self.total_cups.set(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeePriceApp(root)
    root.mainloop()
