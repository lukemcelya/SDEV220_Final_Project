import tkinter as tk
from tkinter import *

def main():
    app = MainWindow()
    menu = MenuFrame(app)
    menu.grid(row=0, column=0, sticky="nsew")
    item = ItemFrame(app)
    item.grid(row=0, column=1, columnspan=3, sticky="nsew")
    order = OrderFrame(app)
    order.grid(row=0, column=4, columnspan=3, sticky="nsew")
    app.mainloop()

class MainWindow(tk.Tk):
    #Initialize main window
    def __init__(self):
        super().__init__()
        self.title("Turoni's Pizzery & Brewery")
        self.minsize(width=1000, height=700)
        
        #Configure rows and columns
        for i in range(5):
            self.rowconfigure(i, weight=1,)
            self.columnconfigure(i, weight=1)
            
class MenuFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #Create menu frame buttons
        self.menu_label = tk.Label(self)
        self.menu_label.grid(pady=5, row=0, column=0, columnspan=2) 
        self.drink_btn = tk.Button(self, text="Drinks", height=5, width=5)
        self.drink_btn.grid(pady=10, padx=10, row=1, column=0)
        self.appetizer_btn = tk.Button(self, text="Appetizers", height=5, width=5)
        self.appetizer_btn.grid(pady=10, padx=10, row=1, column=1)
        self.lunch_spc_btn = tk.Button(self, text="Lunch\nSpecials", height=5, width=5)
        self.lunch_spc_btn.grid(pady=10, padx=10, row=2, column=0)
        self.salad_btn = tk.Button(self, text="Salads", height=5, width=5)
        self.salad_btn.grid(pady=10, padx=10, row=2, column=1)
        self.pizza_btn = tk.Button(self, text="Gourmet\nPizzas", height=5, width=5)
        self.pizza_btn.grid(pady=10, padx=10, row=3, column=0)
        self.byo_btn = tk.Button(self, text="Build Your\nOwn", height=5, width=5)
        self.byo_btn.grid(pady=10, padx=10, row=3, column=1)
        self.kids_btn = tk.Button(self, text="Kid's\nMenu", height=5, width=5)
        self.kids_btn.grid(pady=10, padx=10, row=4, column=0)
        self.sandwich_btn = tk.Button(self, text="Sandwiches", height=5, width=5)
        self.sandwich_btn.grid(pady=10, padx=10, row=4, column=1)
        self.dessert_btn = tk.Button(self, text="Desserts", height=5, width=5)
        self.dessert_btn.grid(pady=10, padx=10, row=5, column=0)
        self.side_btn = tk.Button(self, text="Side\nMenu", height=5, width=5)
        self.side_btn.grid(pady=10, padx=10, row=5, column=1)
        
           
class ItemFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #Create item frame buttons
        self.split_btn = tk.Button(self, text="Split", width=15, height=2)
        self.split_btn.grid(pady=20, padx=10, row=0, column=0)
        self.combine_btn = tk.Button(self, text="Combine", width=15, height=2)
        self.combine_btn.grid(pady=20, padx=10, row=0, column=1)
        self.table_btn = tk.Button(self, text="Table", width=15, height=2)
        self.table_btn.grid(pady=20, padx=10, row=2, column=0)
        self.discount_btn = tk.Button(self, text="Discount", width=15, height=2)
        self.discount_btn.grid(pady=20, padx=10, row=2, column=1)
        
        #Seperate frames for buttons based on selection
        self.item_selection_frame = tk.Frame(self, background="white", height=500, width=400)
        self.item_selection_frame.grid(row=1, column=0, columnspan=3)
        
class OrderFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.void_btn = tk.Button(self, text="Void", width=5, height=2)
        self.void_btn.grid(pady=10, row=0, column=0)
        self.check_btn = tk.Button(self, text="Checks", width=10, height=2)
        self.check_btn.grid(pady=10, row=0, column=1)
        self.print_btn = tk.Button(self, text="Print", width=5, height=2)
        self.print_btn.grid(pady=10, row=0, column=2)
        self.order_label = tk.Label(self, text="Order")
        self.order_label.grid(row=2, column=0, columnspan=3)
    
#Start main
if __name__ == "__main__":
    main()