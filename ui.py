import tkinter as tk
from tkinter import *

def main():
    app = MainWindow()
    menu = MenuFrame(app)
    menu.grid(row=0, column=0, sticky="nsew")
    menu.grid_propagate(False)
    app.mainloop()

class MainWindow(tk.Tk):
    #Initialize main window
    def __init__(self):
        super().__init__()
        self.title("Turoni's Pizzery & Brewery")
        self.minsize(width=1000, height=700)
        
        #Configure rows and columns
        for i in range(6):
            self.rowconfigure(i, weight=1,)
            self.columnconfigure(i, weight=1)
            
class MenuFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, height=700, width=1000, bd=5)
        
        #Item Options
        self.split_btn = tk.Button(self, text="Split", width=15, height=2)
        self.split_btn.grid(row=0, column=2)
        self.combine_btn = tk.Button(self, text="Combine", width=15, height=2)
        self.combine_btn.grid(row=0, column=3)
        self.table_btn = tk.Button(self, text="Table", width=15, height=2)
        self.table_btn.grid(row=5, column=2)
        self.discount_btn = tk.Button(self, text="Discount", width=15, height=2)
        self.discount_btn.grid(row=5, column=3)
        
        #Create Option Frame
        self.option = OptionFrame(self)
        self.option.grid(row=1, column=2, columnspan=2, rowspan=4, padx=20, sticky="n")
        
        #Create menu frame btns
        self.menu_label = tk.Label(self, text="Menu Items")
        self.menu_label.grid(row=0, column=0, columnspan=2) 
        self.drink_btn = tk.Button(self, text="Drinks", height=5, width=5, command=lambda: self.change_menu(0))
        self.drink_btn.grid(padx=10, row=1, column=0)
        self.appetizer_btn = tk.Button(self, text="Appetizers", height=5, width=5, command=lambda: self.change_menu(1))
        self.appetizer_btn.grid(padx=10, row=1, column=1)
        self.sandwich_btn = tk.Button(self, text="Sandwiches", height=5, width=5, command=lambda: self.change_menu(2))
        self.sandwich_btn.grid(padx=10, row=2, column=0)
        self.salad_btn = tk.Button(self, text="Salads", height=5, width=5, command=lambda: self.change_menu(3))
        self.salad_btn.grid(padx=10, row=2, column=1)
        self.pizza_btn = tk.Button(self, text="Gourmet\nPizzas", height=5, width=5, command=lambda: self.change_menu(4))
        self.pizza_btn.grid(padx=10, row=3, column=0)
        self.dessert_btn = tk.Button(self, text="Desserts", height=5, width=5, command=lambda: self.change_menu(5))
        self.dessert_btn.grid(padx=10, row=3, column=1)
        self.side_btn = tk.Button(self, text="Side\nMenu", height=5, width=5, command=lambda: self.change_menu(6))
        self.side_btn.grid(padx=10, row=4, column=0)
        
        #Order Options
        self.void_btn = tk.Button(self, text="Void", width=5, height=2)
        self.void_btn.grid(padx=10, pady=10, row=0, column=4)
        self.check_btn = tk.Button(self, text="Checks", width=10, height=2)
        self.check_btn.grid(pady=10, row=0, column=5)
        self.print_btn = tk.Button(self, text="Print", width=5, height=2)
        self.print_btn.grid(padx=10, pady=10, row=0, column=6)
        self.order_label = tk.Label(self, text="Order")
        self.order_label.grid(row=1, column=4, columnspan=3)
        
    def change_menu(self, option):
        self.option.destroy()
        self.option = OptionFrame(self)
        self.option.grid(row=1, column=2, columnspan=2, rowspan=4, padx=20, sticky="new")
        self.option.grid_propagate(False)
        
        match option:
            case 0:
                self.option.drink_menu()
            case 1:
                self.option.appetizer_menu()
            case 2:
                self.option.sandwich_menu()
            case 3:
                self.option.salad_menu()  
            case 4:
                self.option.pizza_menu()
            case 5:
                self.option.dessert_menu()
            case 6:
                self.option.side_menu()


class OptionFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, background="gray", height=500, width=370)
        
    def drink_menu(self):
        self.soft_drink_btn = tk.Button(self, text="Soft Drinks", width=5, height=5)
        self.soft_drink_btn.grid(padx=20, pady=20, row=0, column=0, sticky="new")
        self.bottled_beer_btn = tk.Button(self, text="Bottled\nBeer", width=5, height=5)
        self.bottled_beer_btn.grid(padx=20, pady=20, row=0, column=1, sticky="new")
        self.draft_beer_btn = tk.Button(self, text="Draft\nBeer", width=5, height=5)
        self.draft_beer_btn.grid(padx=20, pady=20, row=0, column=2, sticky="new")
        self.special_btn = tk.Button(self, text="Brewery\nSpecials", width=5, height=5)
        self.special_btn.grid(padx=20, pady=20, row=1, column=0, sticky="new")
        self.mixed_drinks_btn = tk.Button(self, text="Mixed\nDrinks", width=5, height=5)
        self.mixed_drinks_btn.grid(padx=20, pady=20, row=1, column=1, sticky="new")
        
    def appetizer_menu(self):
        self.garlic_toast_btn = tk.Button(self, text="Garlic\nToast", width=5, height=5)
        self.garlic_toast_btn.grid(padx=20, pady=20, row=0, column=0, sticky="new")
        self.breadstick_btn = tk.Button(self, text="Breadsticks", width=5, height=5)
        self.breadstick_btn.grid(padx=20, pady=20, row=0, column=1, sticky="new")
        self.mozzarella_stick_btn = tk.Button(self, text="Mozzarella\nSticks", width=5, height=5)
        self.mozzarella_stick_btn.grid(padx=20, pady=20, row=0, column=2, sticky="new")
        self.grilled_cheese_btn = tk.Button(self, text="Grilled\nCheese", width=5, height=5)
        self.grilled_cheese_btn.grid(padx=20, pady=20, row=1, column=0, sticky="new")
        self.bruschetta_btn = tk.Button(self, text="Bruschetta", width=5, height=5)
        self.bruschetta_btn.grid(padx=20, pady=20, row=1, column=1, sticky="new")
        self.wings_btn = tk.Button(self, text="Boneless\nWings", width=5, height=5)
        self.wings_btn.grid(padx=20, pady=20, row=1, column=2, sticky="new")
        self.popper_toast_btn = tk.Button(self, text="Popper\nToast", width=5, height=5)
        self.popper_toast_btn.grid(padx=20, pady=20, row=2, column=0, sticky="new")
        self.jalapeno_popper_btn = tk.Button(self, text="Jalapeno\nPopper", width=5, height=5)
        self.jalapeno_popper_btn.grid(padx=20, pady=20, row=2, column=1, sticky="new")
    
    def sandwich_menu(self):
        self.stromboli_btn = tk.Button(self, text="Stromboli", width=5, height=5)
        self.stromboli_btn.grid(padx=20, pady=20, row=0, column=0, sticky="new")
        self.veggie_strom_btn = tk.Button(self, text="Veggie\nStromboli", width=5, height=5)
        self.veggie_strom_btn.grid(padx=20, pady=20, row=0, column=1, sticky="new")
        self.ham_n_ch_btn = tk.Button(self, text="Ham and\nCheese", width=5, height=5)
        self.ham_n_ch_btn.grid(padx=20, pady=20, row=0, column=2, sticky="new")
        self.spcy_chkn_btn = tk.Button(self, text="Spicy\nStrom", width=5, height=5)
        self.spcy_chkn_btn.grid(padx=20, pady=20, row=1, column=0, sticky="new")
        self.vinny_btn = tk.Button(self, text="Vinny\nBurger", width=5, height=5)
        self.vinny_btn.grid(padx=20, pady=20, row=1, column=1, sticky="new")
        self.steak_btn = tk.Button(self, text="Chargrilled\nSteak", width=5, height=5)
        self.steak_btn.grid(padx=20, pady=20, row=1, column=2, sticky="new")
        
    def salad_menu(self):
        self.italian_btn = tk.Button(self, text="Italian\nSalad", width=5, height=5)
        self.italian_btn.grid(padx=20, pady=20, row=0, column=0, sticky="new")
        self.spinach_btn = tk.Button(self, text="Spinach\nSalad", width=5, height=5)
        self.spinach_btn.grid(padx=20, pady=20, row=0, column=1, sticky="new")
        self.house_btn = tk.Button(self, text="House\nSalad", width=5, height=5)
        self.house_btn.grid(padx=20, pady=20, row=0, column=2, sticky="new")
        self.greek_btn = tk.Button(self, text="Greek\nSalad", width=5, height=5)
        self.greek_btn.grid(padx=20, pady=20, row=1, column=0, sticky="new")
    
#Start main
if __name__ == "__main__":
    main()