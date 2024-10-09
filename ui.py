import tkinter
from tkinter import *
import order_data

root = Tk()
root.title("Turoni's Pizza POS")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 1200
window_height = 800
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry = (f'{window_width}x{window_height}+{x}+{y}')
root.resizable(False, False)

#-------------------------Functions--------------------------#

##Global Variables##
current_subtotal : float = 0.00
current_tax : float = 0.00
current_total : float = 0.00
order_number : int = 0

def add_to_list(item_name : str, price : float):
    #Add item to list box
    order_shown.insert(END, item_name + '\n')
    order_shown.insert(END, "                      $")
    #Format price to 2 decimal places
    price_insert = "{: .2f}".format(float(price))
    order_shown.insert(END, price_insert)
    order_shown.insert(END, '\n')
    
    order_data.OrderData().add_item(item_name, price)
    add_to_total(price)
    
def add_to_total(price):
    #Global vars
    global current_subtotal
    global current_tax
    global current_total
    
    #Calculate subtotal, tax, total (format float for display)
    current_subtotal += price
    subtotal_insert = "{: .2f}".format(float(current_subtotal))
    current_tax += price * .07
    tax_insert = "{: .2f}".format(float(current_tax))
    current_total = current_subtotal + current_tax
    total_insert = "{: .2f}".format(float(current_total))
    
    
    #Delete everything from total textbox and rewrite after each item added
    total.delete("1.0", "end")
    total.insert(END, "Subtotal:              $")
    total.insert(END, subtotal_insert)
    total.insert(END, '\n')
    total.insert(END, "Tax:                   $")
    total.insert(END, tax_insert)
    total.insert(END, '\n')
    total.insert(END, "Total:                 $")
    total.insert(END, total_insert)
    
def sandwich_size(item_name):
    def half(item_name):
        new_name = item_name + " (half)"
        add_to_list(new_name, 6.87)
        size_window.destroy()
                
    def full(item_name):
        new_name = item_name + " (full)"
        add_to_list(new_name, 12.68)
        size_window.destroy()
        
    def cncl():
        size_window.destroy()
    
    
    size_window = Toplevel(root)
    #Set window position
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()
    size_x = root_x + 400
    size_y = root_y + 200
    size_window.geometry(f'+{size_x}+{size_y}')
    
    size_window.title(item_name)
    #size_window.geometry("400x200")
    size_window.resizable(False, False)
    
    size_frame = Frame(size_window, width=380, height=180, background="seashell3", highlightbackground="Black", highlightthickness=2,)
    size_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", rowspan=3, columnspan=2)
    
    sizelbl = Label(size_frame, text="Size?", background="seashell3", fg="Black", font=("Courier", 12))
    sizelbl.grid(row=0, column=0, sticky="nsew", ipadx=167, columnspan=2)
    half_option = Button(size_frame, text="Half", width=10, font=("Courier", 15),borderwidth=0, bg="White", fg="Black", command=lambda: half(item_name))
    half_option.grid(row=1, column=0, ipady=20, pady=10)
    full_option = Button(size_frame, text="Full", width=10, font=("Courier", 15),borderwidth=0, bg="White", fg="Black", command=lambda: full(item_name))
    full_option.grid(row=1, column=1, ipady=20, pady=10)
    cancel = Button(size_frame, text="Cancel", width=5, font=("Courier", 15),borderwidth=0, bg="White", fg="Black", command=lambda: cncl())
    cancel.grid(row=2, column=0, ipady=10, pady=10, columnspan=2)

def builder_pizza(item_name, handtoss, thincrust, stuffedcrust):
    def hand(item_name, price):
        new_name = item_name + " (handtoss)"
        add_to_list(new_name, price)
        size_window.destroy()
                
    def thin(item_name, price):
        new_name = item_name + " (thincrust)"
        add_to_list(new_name, price)
        size_window.destroy()
        
    def stuffed(item_name, price):
        new_name = item_name + " (stuffedcrust)"
        add_to_list(new_name, price)
        size_window.destroy()
    
    def cncl():
        size_window.destroy()
    
    size_window = Toplevel(root)
    #Set window position
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()
    size_x = root_x + 400
    size_y = root_y + 200
    size_window.geometry(f'+{size_x}+{size_y}')
    
    size_window.title(item_name)
    #size_window.geometry("400x200")
    size_window.resizable(False, False)
    
    size_frame = Frame(size_window, width=380, height=180, background="seashell3", highlightbackground="Black", highlightthickness=2,)
    size_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", rowspan=3, columnspan=2)
    
    sizelbl = Label(size_frame, text="Crust?", background="seashell3", fg="Black", font=("Courier", 12))
    sizelbl.grid(row=0, column=0, sticky="nsew", ipadx=167, columnspan=3)
    small_option = Button(size_frame, text="HandToss", width=10, font=("Courier", 15),borderwidth=0, bg="White", fg="Black", command=lambda: hand(item_name, handtoss))
    small_option.grid(row=1, column=0, ipady=20, pady=10)
    medium_option = Button(size_frame, text="ThinCrust", width=10, font=("Courier", 15),borderwidth=0, bg="White", fg="Black", command=lambda: thin(item_name, thincrust))
    medium_option.grid(row=1, column=1, ipady=20, pady=10)
    large_option = Button(size_frame, text="StuffedCrust", width=10, font=("Courier", 15),borderwidth=0, bg="White", fg="Black", command=lambda: stuffed(item_name, stuffedcrust))
    large_option.grid(row=1, column=2, ipady=20, pady=10)
    cancel = Button(size_frame, text="Cancel", width=5, font=("Courier", 15),borderwidth=0, bg="White", fg="Black", command=lambda: cncl())
    cancel.grid(row=2, column=0, ipady=10, pady=10, columnspan=3)
    
        
def pizza_size(item_name, s_price, m_price, l_price):
    def small(item_name, price):
        new_name = item_name + " (sm)"
        add_to_list(new_name, price)
        size_window.destroy()
                
    def medium(item_name, price):
        new_name = item_name + " (med)"
        add_to_list(new_name, price)
        size_window.destroy()
        
    def large(item_name, price):
        new_name = item_name + " (lrg)"
        add_to_list(new_name, price)
        size_window.destroy()
    
    def cncl():
        size_window.destroy()
    
    size_window = Toplevel(root)
    #Set window position
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()
    size_x = root_x + 400
    size_y = root_y + 200
    size_window.geometry(f'+{size_x}+{size_y}')
    
    size_window.title(item_name)
    #size_window.geometry("400x200")
    size_window.resizable(False, False)
    
    size_frame = Frame(size_window, width=380, height=180, background="seashell3", highlightbackground="Black", highlightthickness=2,)
    size_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", rowspan=3, columnspan=2)
    
    sizelbl = Label(size_frame, text="Size?", background="seashell3", fg="Black", font=("Courier", 12))
    sizelbl.grid(row=0, column=0, sticky="nsew", ipadx=167, columnspan=3)
    small_option = Button(size_frame, text="Small", width=10, font=("Courier", 15),borderwidth=0, bg="White", fg="Black", command=lambda: small(item_name, s_price))
    small_option.grid(row=1, column=0, ipady=20, pady=10)
    medium_option = Button(size_frame, text="Medium", width=10, font=("Courier", 15),borderwidth=0, bg="White", fg="Black", command=lambda: medium(item_name, m_price))
    medium_option.grid(row=1, column=1, ipady=20, pady=10)
    large_option = Button(size_frame, text="Large", width=10, font=("Courier", 15),borderwidth=0, bg="White", fg="Black", command=lambda: large(item_name, l_price))
    large_option.grid(row=1, column=2, ipady=20, pady=10)
    cancel = Button(size_frame, text="Cancel", width=5, font=("Courier", 15),borderwidth=0, bg="White", fg="Black", command=lambda: cncl())
    cancel.grid(row=2, column=0, ipady=10, pady=10, columnspan=3)
    
def finish_order():
    global order_number
    
    order_data.OrderData().close_order()
    order_number += 1
    clear_lists()
    
def clear_lists():
    global current_subtotal, current_tax, current_total
    order_data.OrderData().add_order_to_df(current_subtotal, current_tax, current_total)
    
    current_subtotal = 0
    current_tax = 0
    current_total = 0
    order_shown.delete("1.0", "end")
    total.delete("1.0", "end")

def drink_options():
    for widget in choices.winfo_children():
        widget.destroy()
    
    soft_drinks = tkinter.Button(choices, text="Soft Drinks", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Soft Drink", 2.50))
    soft_drinks.grid(row=1, column=0, padx = 10, pady= 10, ipady = 30)

    bottled_beer = tkinter.Button(choices, text="Bottled Beer", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Bottled Beer", 5.00))
    bottled_beer.grid(row=1, column=1, padx = 10, pady=10, ipady=30)

    draft = tkinter.Button(choices, text="Draft", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Draft Pint", 8.00))
    draft.grid(row=1, column=2, padx = 10, pady= 10, ipady = 30)

    brew_spcl = tkinter.Button(choices, wraplength= 80, text="Brewery Specials", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Brew Special", 9.00))
    brew_spcl.grid(row=2, column=0, padx = 10, pady= 10, ipady = 21)

    mixed_drinks = tkinter.Button(choices, text="Mixed Drinks", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Mixed Drink", 10.00))
    mixed_drinks.grid(row=2, column=1, padx = 10, pady= 10, ipady = 30)
    

def appetizer_options():
    for widget in choices.winfo_children():
        widget.destroy()
    
    garlic_toast = tkinter.Button(choices, text="Garlic Toast", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Garlic Toast", 5.94))
    garlic_toast.grid(row=1, column=0, padx = 10, pady= 10, ipady = 30)
    
    breadsticks = tkinter.Button(choices, text="Breadsticks", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Breadsticks", 5.94))
    breadsticks.grid(row=1, column=1, padx = 10, pady=10, ipady=30)

    mozzarella = tkinter.Button(choices, wraplength= 82, text="Mozarella Sticks", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Mozzarella Sticks", 9.31))
    mozzarella.grid(row=1, column=2, padx = 10, pady= 10, ipady = 21)

    grilled_cheese = tkinter.Button(choices, wraplength= 80, text="Grilled Cheese", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Grilled Cheez-Eze", 5.94))
    grilled_cheese.grid(row=2, column=0, padx = 10, pady= 10, ipady = 21)

    bruschetta = tkinter.Button(choices, text="Bruschetta", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Bruschetta", 7.93))
    bruschetta.grid(row=2, column=1, padx = 10, pady= 10, ipady = 30)
    
    wings = tkinter.Button(choices, wraplength= 80, text="Boneless Wings", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Boneless Wings", 9.31))
    wings.grid(row=2, column=2, padx = 10, pady= 10, ipady = 21)
    
    popper_toast = tkinter.Button(choices, wraplength= 80, text="Popper Toast", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Popper Toast", 8.27))
    popper_toast.grid(row=3, column=0, padx = 10, pady=10, ipady=21)

    jalapeno = tkinter.Button(choices, wraplength= 80, text="Jalapeno Poppers", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Jalapeno Poppers", 10.49))
    jalapeno.grid(row=3, column=1, padx = 10, pady= 10, ipady = 21)

def daily_options():
    for widget in choices.winfo_children():
        widget.destroy()
    
    monday = tkinter.Button(choices, wraplength=80, text = "Greek Salad (M)", width=10, font=("Courier", 15),borderwidth=0, command = lambda: add_to_list("Monday Spcl", 8.87))
    monday.grid(row=1, column=0, padx = 10, pady= 10, ipady = 21)
    
    tuesday = tkinter.Button(choices, wraplength=80, text = "Ham + Cheese (T)", width=10, font=("Courier", 15),borderwidth=0, command = lambda: add_to_list("Tuesday Spcl", 10.14))
    tuesday.grid(row=1, column=1, padx = 10, pady= 10, ipady = 21)
    
    wednesday = tkinter.Button(choices, wraplength=80, text = "Stromboli (W)", width=10, font=("Courier", 15),borderwidth=0, command = lambda: add_to_list("Wednesday Spcl", 10.14))
    wednesday.grid(row=1, column=2, padx = 10, pady= 10, ipady = 30)
    
    thursday = tkinter.Button(choices, wraplength=80, text = "Steak Sandwich (Th)", width=10, font=("Courier", 15),borderwidth=0, command = lambda: add_to_list("Thursday Spcl", 11.41))
    thursday.grid(row=2, column=0, padx = 10, pady= 10, ipady = 21)
    
    friday = tkinter.Button(choices, wraplength=80, text = "Italian Salad (F)", width=10, font=("Courier", 15),borderwidth=0, command = lambda: add_to_list("Friday Spcl", 9.58))
    friday.grid(row=2, column=1, padx = 10, pady= 10, ipady = 21)
    
        
def salad_options():
    for widget in choices.winfo_children():
        widget.destroy()
        
    italian = tkinter.Button(choices, wraplength= 80, text="Italian Salad", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Italian Salad", 11.41))
    italian.grid(row=1, column=0, padx = 10, pady= 10, ipady = 21)
    
    spinach = tkinter.Button(choices, wraplength= 80, text="Spinach Salad", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Spinach Salad", 10.14))
    spinach.grid(row=1, column=1, padx = 10, pady=10, ipady=21)

    house = tkinter.Button(choices, wraplength= 80, text="House Salad", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("House Salad", 6.29))
    house.grid(row=1, column=2, padx = 10, pady= 10, ipady = 21)

    greek = tkinter.Button(choices, wraplength= 80, text="Greek Salad", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Greek Salad", 10.14))
    greek.grid(row=2, column=0, padx = 10, pady= 10, ipady = 21)
    
def sandwich_options():
    for widget in choices.winfo_children():
        widget.destroy()
    
    stromboli = tkinter.Button(choices, text="Stromboli", width=10, font=("Courier", 15),borderwidth=0, command=lambda: sandwich_size("Stromboli"))
    stromboli.grid(row=1, column=0, padx = 10, pady= 10, ipady = 30)
    
    veggie_strom = tkinter.Button(choices, wraplength= 82, text="Veggie Stromboli", width=10, font=("Courier", 15),borderwidth=0, command=lambda: sandwich_size("Veggie Stromboli"))
    veggie_strom.grid(row=1, column=1, padx = 10, pady=10, ipady=21)

    ham_cheese = tkinter.Button(choices, wraplength= 82, text="Ham and Cheese", width=10, font=("Courier", 15),borderwidth=0, command=lambda: sandwich_size("Ham and Cheese"))
    ham_cheese.grid(row=1, column=2, padx = 10, pady= 10, ipady = 21)

    spicy_chk = tkinter.Button(choices, wraplength= 82, text="Spicy Stromboli", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Spicy Stromboli", 12.84))
    spicy_chk.grid(row=2, column=0, padx = 10, pady= 10, ipady = 21)

    vinny = tkinter.Button(choices, wraplength= 82, text="Vinny Burger", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Vinny Burger", 11.77))
    vinny.grid(row=2, column=1, padx = 10, pady= 10, ipady = 21)
    
    steak = tkinter.Button(choices, wraplength= 100, text="Chargrilled Steak", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Chargrilled Steak", 13.99))
    steak.grid(row=2, column=2, padx = 10, pady= 10, ipady = 21)
    
def pizza_options():
    for widget in choices.winfo_children():
        widget.destroy()
    
    house_spcl = tkinter.Button(choices, text="House\nSpecial", width=10, font=("Courier", 15),borderwidth=0, command=lambda: pizza_size("House Special", 14.11, 24.06, 32.78))
    house_spcl.grid(row=1, column=0, padx = 10, pady= 10, ipady = 21)
    
    strom_pie = tkinter.Button(choices, text="Stromboli\nPie", width=10, font=("Courier", 15),borderwidth=0, command=lambda: pizza_size("Stromboli Pie", 14.54, 24.08, 32.40))
    strom_pie.grid(row=1, column=1, padx = 10, pady=10, ipady=21)

    marg = tkinter.Button(choices, text="Margarita", width=10, font=("Courier", 15),borderwidth=0, command=lambda: pizza_size("Queen Margarita", 13.02, 19.98, 28.06))
    marg.grid(row=1, column=2, padx = 10, pady= 10, ipady = 30)

    hawaiian = tkinter.Button(choices, text="Hawaiian", width=10, font=("Courier", 15),borderwidth=0, command=lambda: pizza_size("Hawaiian Delight", 14.44, 20.51, 28.61))
    hawaiian.grid(row=2, column=0, padx = 10, pady= 10, ipady = 30)

    vincen = tkinter.Button(choices, text="Vincenzio", width=10, font=("Courier", 15),borderwidth=0, command=lambda: pizza_size("Vencenzio", 16.15, 26.10, 34.82))
    vincen.grid(row=2, column=1, padx = 10, pady= 10, ipady = 30)
    
    iron = tkinter.Button(choices, text="Iron\nMan", width=10, font=("Courier", 15),borderwidth=0, command=lambda: pizza_size("Iron Man", 14.11, 24.06, 32.78))
    iron.grid(row=2, column=2, padx = 10, pady= 10, ipady = 21)
    
    greek_p = tkinter.Button(choices, text="Greek", width=10, font=("Courier", 15),borderwidth=0, command=lambda: pizza_size("Greek", 14.11, 24.06, 32.78))
    greek_p.grid(row=3, column=0, padx = 10, pady=10, ipady=30)

    veggie = tkinter.Button(choices, text="Veggie\nSpecial", width=10, font=("Courier", 15),borderwidth=0, command=lambda: pizza_size("Veggie Special", 14.11, 24.06, 32.78))
    veggie.grid(row=3, column=1, padx = 10, pady= 10, ipady = 21)
    
    meat = tkinter.Button(choices, text="Lots a\nMeat", width=10, font=("Courier", 15),borderwidth=0, command=lambda: pizza_size("Lots-a-Meat", 17.75, 24.81, 33.76))
    meat.grid(row=3, column=2, padx = 10, pady= 10, ipady = 21)
    
    pepper = tkinter.Button(choices, text="Pepper\nPlanet", width=10, font=("Courier", 15),borderwidth=0, command=lambda: pizza_size("Pepper Planet", 14.11, 24.06, 32.78))
    pepper.grid(row=4, column=0, padx = 10, pady=10, ipady=21)

    buffalo = tkinter.Button(choices, text="Buffalo", width=10, font=("Courier", 15),borderwidth=0, command=lambda: pizza_size("Buffalo Chicken", 16.15, 26.10, 34.82))
    buffalo.grid(row=4, column=1, padx = 10, pady= 10, ipady = 30)

    bbq = tkinter.Button(choices, text="BBQ", width=10, font=("Courier", 15),borderwidth=0, command=lambda: pizza_size("BBQ", 16.15, 26.10, 34.82))
    bbq.grid(row=4, column=2, padx = 10, pady= 10, ipady = 30)
    
def builder_options():
    for widget in choices.winfo_children():
        widget.destroy()
    
    build_small= tkinter.Button(choices,  text="Make a\nPizza\n(Small)", width=10, font=("Courier", 15),borderwidth=0, command=lambda: builder_pizza("Custom -small-", 12.11, 10.10, 15.20))
    build_small.grid(row=1, column=0, padx = 10, pady= 10, ipady = 21)
    
    build_med = tkinter.Button(choices, text="Make a\nPizza\n(Med)", width=10, font=("Courier", 15),borderwidth=0, command=lambda: builder_pizza("Custom -med-", 18.11, 15.06, 22.78))
    build_med.grid(row=1, column=1, padx = 10, pady= 10, ipady = 21)
    
    build_large = tkinter.Button(choices, text="Make a\nPizza\n(Large)", width=10, font=("Courier", 15),borderwidth=0, command=lambda: builder_pizza("Custom -lrg-", 23.11, 21.06, 30.78))
    build_large.grid(row=1, column=2, padx = 10, pady= 10, ipady = 21)
    
def kiddie_options():
    for widget in choices.winfo_children():
        widget.destroy()
    
    boneless = tkinter.Button(choices, wraplength= 80, text="Boneless Wing Meal", width = 10, font = ("Courier", 15), borderwidth = 0, command = lambda: add_to_list("Boneless Wing (Kiddie)", 8.34))
    boneless.grid(row=0, column=0, padx=10, pady=10, ipady=21)
    
    pizza_meal = tkinter.Button(choices, wraplength= 80, text="7in Pizza Meal", width = 10, font = ("Courier", 15), borderwidth = 0, command = lambda: add_to_list("7in. Cheese Pizza (Kiddie)", 8.14))
    pizza_meal.grid(row=0, column=1, padx=10, pady=10, ipady=21)
    
    grilled_cheese = tkinter.Button(choices, wraplength= 80, text="Grilled Cheese", width = 10, font = ("Courier", 15), borderwidth = 0, command = lambda: add_to_list("Grilled Cheese(Kiddie)", 7.85))
    grilled_cheese.grid(row=0, column=2, padx=10, pady=10, ipady=30)
    
    cheese_fries = tkinter.Button(choices, wraplength= 80, text="Cheese Fries", width = 10, font = ("Courier", 15), borderwidth = 0, command = lambda: add_to_list("Cheese Fries (Kiddie)", 4.99))
    cheese_fries.grid(row=1, column=0, padx=10, pady=10, ipady=30)
    
def dessert_options():
    for widget in choices.winfo_children():
        widget.destroy()
    
    cookies = tkinter.Button(choices, text="Cookies", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Cookie", 3.48))
    cookies.grid(row=1, column=0, padx = 10, pady= 10, ipady = 30)
    cheesecake = tkinter.Button(choices, text="Cheesecake", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Cheesecake", 8.21))
    cheesecake.grid(row=1, column=1, padx = 10, pady= 10, ipady = 30)
    ice_cream = tkinter.Button(choices, text="Ice Cream", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Ice Cream", 5.44))
    ice_cream.grid(row=1, column=2, padx = 10, pady= 10, ipady = 30)
    

def side_options():
    for widget in choices.winfo_children():
        widget.destroy()
    
    cheese_cup = tkinter.Button(choices, text="Cheese\nCup", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Cheese Cup", 1.00))
    cheese_cup.grid(row=1, column=0, padx = 10, pady= 10, ipady = 21)
    
    ranch = tkinter.Button(choices, text="Ranch\nCup", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Ranch Cup", .75))
    ranch.grid(row=1, column=1, padx = 10, pady=10, ipady=21)

    marinara = tkinter.Button(choices, text="Marinara\nSauce", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Marinara Sauce", .50))
    marinara.grid(row=1, column=2, padx = 10, pady= 10, ipady = 21)

    veggie_order = tkinter.Button(choices, text="Order of\nVeggie", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Order of Veggies", 2.00))
    veggie_order.grid(row=2, column=0, padx = 10, pady= 10, ipady = 21)

    italian = tkinter.Button(choices, text="Italian\nSauce", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Italian Sauce", .75))
    italian.grid(row=2, column=1, padx = 10, pady= 10, ipady = 21)
    
    buffalo = tkinter.Button(choices, text="Buffalo\nSauce", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Buffalo Sauce", .75))
    buffalo.grid(row=2, column=2, padx = 10, pady= 10, ipady = 21)
    
    bbq = tkinter.Button(choices, text="BBQ\nSauce", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("BBQ Sauce", .75))
    bbq.grid(row=3, column=0, padx = 10, pady=10, ipady=21)

    garlic = tkinter.Button(choices, text="Garlic\nSauce", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Garlic Sauce", .75))
    garlic.grid(row=3, column=1, padx = 10, pady= 10, ipady = 21)
    
    blue_cheese = tkinter.Button(choices, text="Blue\nCheese", width=10, font=("Courier", 15),borderwidth=0, command=lambda: add_to_list("Blue Cheese", 1.00))
    blue_cheese.grid(row=3, column=2, padx = 10, pady= 10, ipady = 21)    

def catering_options():
    for widget in choices.winfo_children():
        widget.destroy()
    
    pizza_party = tkinter.Button(choices, wraplength= 80, text="50 Person Meal", width = 10, font = ("Courier", 15), borderwidth = 0, command = lambda: add_to_list("Pizza Party (50 People)", 150.00))
    pizza_party.grid(row=0, column=0, padx=10, pady=10, ipady=21)
    
    pizza_buffet = tkinter.Button(choices, wraplength= 80, text="Pizza Buffet", width = 10, font = ("Courier", 15), borderwidth = 0, command = lambda: add_to_list("Pizza Buffet(100 People)", 300.00))
    pizza_buffet.grid(row=0, column=1, padx=10, pady=10, ipady=30)
    
    mini_party = tkinter.Button(choices, wraplength= 80, text="Mini Party", width = 10, font = ("Courier", 15), borderwidth = 0, command = lambda: add_to_list("Mini Party (12 People))", 75.00))
    mini_party.grid(row=0, column=2, padx=10, pady=10, ipady=30)
    
def cancel_menu():
    for widget in choices.winfo_children():
        widget.destroy()

#-------------------------Widgets--------------------------#
Background_Frame = Frame(root, highlightbackground="Black", highlightthickness=2, background="seashell3")
Background_Frame.grid(row=0, column=0, columnspan=3, rowspan=3, padx=10)

top_menu = Frame(Background_Frame, background="seashell3")
top_menu.grid(row=0, column = 0)

top_choices = Frame(Background_Frame, background="seashell3")
top_choices.grid(row=0, column=1, pady=5)

top_ticket = Frame(Background_Frame, background="seashell3")
top_ticket.grid(row=0, column=2, pady=5)

menu = Frame(Background_Frame, background="seashell3")
menu.grid(row=1, column = 0, padx=10, rowspan=2)

choices = Frame(Background_Frame, highlightbackground="Black", highlightthickness=1, width=428, height=500, background="White")
choices.grid(row=1, column = 1, padx=10, sticky="NS", rowspan=2)

ticket = Frame(Background_Frame, highlightbackground="Black", highlightthickness=1, width=250, background="White")
ticket.grid(row=1, column = 2, padx=10, sticky="NS", rowspan=2)

bottom_menu = Frame(Background_Frame, background="seashell3")
bottom_menu.grid(row=3, column=0)

bottom_choices = Frame(Background_Frame, background="seashell3")
bottom_choices.grid(row=3, column=1, pady=5)

bottom_ticket = Frame(Background_Frame, background="seashell3")
bottom_ticket.grid(row=3, column=2)

#Buttons
#top widgets
menu_items = tkinter.Label(top_menu, text="Menu Items", font=("Courier", 30), borderwidth=0, background="seashell3", foreground="Black")
menu_items.grid(row=0, column=0, ipady=5, columnspan=2)

turoni_label= tkinter.Label(top_choices, text="Turoni's | Pizza & Brewery", width=30, font=("Courier", 15), borderwidth=0, background= "tomato2")
turoni_label.grid(row=0, column=0, columnspan = 2, ipady=5, padx=5, pady=5)

void = tkinter.Button(top_ticket, text="void", font=("Courier", 15), width = 10, borderwidth=0)
void.grid(row=0, column=0,ipady=5, pady=5, padx=5)

printer = tkinter.Button(top_ticket, text = "print", font=("Courier", 15), width = 10, borderwidth=0)
printer.grid(row=0, column=1, ipady=5, pady=5, padx=5)


#Menu Buttons
drinks = tkinter.Button(menu, text="Drinks", width=10, font=("Courier", 15), borderwidth=0, command=lambda: drink_options())
drinks.grid(row=1, column=0, padx = 2, pady= 10, ipady = 30)

appetizers = tkinter.Button(menu, text="Appetizers", width=10, font=("Courier", 15),borderwidth=0, command=lambda: appetizer_options())
appetizers.grid(row=1, column=1, padx = 5, pady=10, ipady=30)

daily = tkinter.Button(menu, wraplength= 80, text="Daily Specials", width=10, font=("Courier", 15),borderwidth=0, command = lambda: daily_options())
daily.grid(row=2, column=0, padx = 5, pady= 10, ipady = 21)

salads = tkinter.Button(menu, text="Salads", width=10, font=("Courier", 15),borderwidth=0, command=lambda: salad_options())
salads.grid(row=2, column=1, padx = 5, pady= 10, ipady = 30)

gourmet = tkinter.Button(menu, wraplength= 80, text="Gourmet Pizzas", width=10, font=("Courier", 15),borderwidth=0, command=lambda: pizza_options())
gourmet.grid(row=3, column=0, padx = 5, pady= 10, ipady = 21)

build = tkinter.Button(menu, wraplength= 80, text="Build Your Own", width=10, font=("Courier", 15),borderwidth=0, command=lambda:builder_options())
build.grid(row=3, column= 1, padx = 5, pady= 10, ipady = 21)

kiddie = tkinter.Button(menu, text="Kiddie Menu", width=10, font=("Courier", 15),borderwidth=0, command=lambda: kiddie_options())
kiddie.grid(row=4, column= 0, padx = 5, pady= 10, ipady = 30)

sandwiches = tkinter.Button(menu, text="Sandwiches", width=10, font=("Courier", 15),borderwidth=0, command=lambda: sandwich_options())
sandwiches.grid(row=4, column= 1, padx = 5, pady= 10, ipady = 30)

desserts = tkinter.Button(menu, text="Desserts", width=10, font=("Courier", 15),borderwidth=0, command=lambda: dessert_options())
desserts.grid(row=5, column= 0, padx = 5, pady= 10, ipady = 30)

sides = tkinter.Button(menu, text="Side Items", width=10, font=("Courier", 15),borderwidth=0, command=lambda: side_options())
sides.grid(row=5, column= 1, padx = 5, pady= 10, ipady = 30)

catering = tkinter.Button(menu, text="Catering", width = 25, font=("Courier", 15),borderwidth=0, command=lambda: catering_options())
catering.grid(row=6, column=0, pady = 5, ipady=20, columnspan=2)


#Choices Buttons


#Ticket Buttons
order= tkinter.Label(ticket, text="Order", bg="White", fg="Black", font=("Courier", 15),borderwidth=0)
order.grid(row = 0, column=1, columnspan=3, ipadx=121, ipady=5)

order_shown = Text(ticket, width=30, height= 30, highlightcolor="Black", highlightbackground="Black", highlightthickness=1, fg='Black', bg='White', font=("Courier", 15),borderwidth=0)
order_shown.grid(row=1, column= 1, ipadx=10)

total = Text(ticket, width=30, height= 5, fg='Black', bg='White', font=("Courier", 15), highlightcolor="Black", highlightbackground="Black", highlightthickness=1)
total.grid(row=2, column= 1, ipadx=10, padx=5, pady=5)


#bottom Widgets

discounts= tkinter.Button(bottom_choices, text="discounts", width=30, font=("Courier", 15),borderwidth=0, background="seashell3")
discounts.grid(row=0, column=0, columnspan=2, ipady=5, padx=5, pady=5)

chain = tkinter.Button(bottom_ticket, text="Chain", font=("Courier", 15),borderwidth=0)
chain.grid(row=0, column=0,ipady=5, pady=5, padx=5)

pay = tkinter.Button(bottom_ticket, text="Staff Bank",width = 10, font=("Courier", 15),borderwidth=0)
pay.grid(row=0, column=1, ipady=5, pady=5, padx=5)

finish = tkinter.Button(bottom_ticket, text = "Done", font=("Courier", 15),borderwidth=0, command=lambda: finish_order())
finish.grid(row=0, column=2, ipady=5, pady=5, padx=5)

cancel = tkinter.Button(bottom_menu, text = "Cancel", bg='red', fg='black', font=("Courier", 15),borderwidth=0, command=lambda: cancel_menu())
cancel.grid(row=0, column=0, ipady=5, padx=5)
#-------------------------Images--------------------------#

root.mainloop()