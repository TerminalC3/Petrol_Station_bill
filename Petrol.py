from datetime import datetime
from tkinter import *
from time import localtime, strftime


date = datetime.today().strftime("%d-%m-%y")
time = strftime("%H:%M", localtime())


def print_bill():

    global bill_window
    bill_window = Tk()

    customer_name = name_entry.get()
    regno = regno_entry.get()
    quantity = quantity_entry.get()
    serviceman = serviceman_entry.get()
    central_tax_percent = central_tax_entry.get()
    petrol_price = price_entry.get()
    state_tax_percent = state_tax_entry.get()
    added_charge = add_charges_entry.get()
    total_petrol_price = float(petrol_price) * float(quantity)
    central_tax = (float(central_tax_entry.get()) / 100 ) * total_petrol_price
    state_tax = (float(state_tax_entry.get()) / 100) * total_petrol_price
    total_cost = float(total_petrol_price) + float(added_charge) + float(state_tax) + float(central_tax)
    total_cost = float("{:.2f}".format(total_cost))

    bill_window.title("Bill for " + customer_name)
    bill_window.geometry("1366x768")
    bill_window.config(bg="#ffff66")

    bunk_title_label = Label(bill_window, text = "BHARAT PETROLEUM", font = ("Impact", 30, "bold"), bg="#ffff66")
    bunk_title_label.pack()

    fill_label5 = Label(bill_window, bg="#ffff66")
    fill_label6 = Label(bill_window, bg="#ffff66")
    fill_label7 = Label(bill_window, bg="#ffff66")
    fill_label8 = Label(bill_window, bg="#ffff66")
    fill_label5.pack()
    fill_label6.pack()
    fill_label7.pack()
    fill_label8.pack()

    date_labell = Label(bill_window, text = "Date :                                " + date, font = ("Century Gothic", 15, "bold"), bg = "#ffff66")
    date_labell.pack(anchor = "w")

    time_labell = Label(bill_window, text = "Time :                                " + str(time), font = ("Century Gothic", 15, "bold"), bg = "#ffff66")
    time_labell.pack(anchor = "w")

    bill_name = Label(bill_window, text = "Customer name :             " + customer_name, font = ("Century Gothic", 15, "bold"), bg = "#ffff66")
    bill_name.pack(anchor = "w")

    bill_regno = Label(bill_window, text="Registration number :       " + regno, font=("Century Gothic", 15, "bold"), bg="#ffff66")
    bill_regno.pack(anchor = "w")

    bill_quantity = Label(bill_window, text="Litres :                             " + quantity + " ltrs", font=("Century Gothic", 15, "bold"), bg="#ffff66")
    bill_quantity.pack(anchor = "w")

    bill_serviceman = Label(bill_window, text="Serviceman name :         " + serviceman, font=("Century Gothic", 15, "bold"), bg="#ffff66")
    bill_serviceman.pack(anchor = "w")

    bill_apparent_total = Label(bill_window, text="Total price :                    " + str(total_petrol_price), font=("Century Gothic", 15, "bold"), bg="#ffff66")
    bill_apparent_total.pack(anchor = 'w')

    bill_central_tax_label = Label(bill_window, text="Central tax :                   " + str(central_tax) , font=("Century Gothic", 15, "bold"), bg="#ffff66")
    bill_central_tax_label.pack(anchor = 'w')

    bill_state_label = Label(bill_window, text="State tax :                       " + str(state_tax) , font=("Century Gothic", 15, "bold"), bg="#ffff66")
    bill_state_label.pack(anchor = 'w')

    bill_added_charges_label = Label(bill_window, text="Added charges:                 " + str(added_charge), font=("Century Gothic", 15, "bold"), bg="#ffff66")
    bill_added_charges_label.pack(anchor='w')

    bill_total_price_label = Label(bill_window, text="Total Cost:                      " + str(total_cost), font=("Century Gothic", 15, "bold"), bg="#ffff66")
    bill_total_price_label.pack(anchor='w')

    bill_central_percent_label = Label(bill_window, text="Central tax percent:      " + str(central_tax_percent), font=("Century Gothic", 15, "bold"), bg="#ffff66")
    bill_central_percent_label.pack(anchor='w')

    bill_state_percent_label = Label(bill_window, text="State tax percent:          " + str(state_tax_percent), font=("Century Gothic", 15, "bold"), bg="#ffff66")
    bill_state_percent_label.pack(anchor='w')

    bill_close_button = Button(bill_window, text = "Close", command = close, font=("Century Gothic", 15, "bold"), bg="#ffff66")
    bill_close_button.pack()

    bill_window.mainloop()


def close():
    bill_window.destroy()


window = Tk()

window_image = PhotoImage(file = "Petrol.png")
window.iconphoto(False, window_image)
window.geometry("1366x768")
window.config(bg = "red")

fill_label = Label(bg = 'red')
fill_label1 = Label(bg = 'red')
fill_label2 = Label(bg = 'red')
fill_label3 = Label(bg = 'red')
fill_label4 = Label(bg = 'red')

date_label = Label(text = date, bg = 'red', font = ("consolas", 15))
date_label.pack()

petrol_image = Label(image = window_image, bg = 'red')
petrol_image.pack()

price_label = Label(text = "Price per litre", font = ("consolas", 10, "bold"), bg = "red")
price_entry = Entry(font = ("Arial", 15), width = 9, bg = "#ff6666")
price_entry.insert(END, 100.21)
price_label.pack()
price_entry.pack()

central_tax_label = Label(text = "Central tax", font = ("consolas", 10, "bold"), bg = "red")
central_tax_entry = Entry(font = ("Arial", 15), width = 9, bg = "#ff6666")
central_tax_entry.insert(END, 20)
central_tax_label.pack()
central_tax_entry.pack()


state_tax_label = Label(text = "State tax", font = ("consolas", 10, "bold"), bg = "red")
state_tax_entry = Entry(font = ("Arial", 15), width = 9, bg = "#ff6666")
state_tax_entry.insert(END, 10)
state_tax_label.pack()
state_tax_entry.pack()


add_charges_label = Label(text = "Add charges", font = ("consolas", 10, "bold"), bg = "red")
add_charges_entry = Entry(font = ("Arial", 15), width = 9, bg = "#ff6666")
add_charges_entry.insert(END, 0)
add_charges_label.pack()
add_charges_entry.pack()

fill_label3.pack()

name_label = Label(text = "Customer name", font = ("consolas", 15), bg = "red")
name_entry = Entry(font = ("Arial", 15), width = 25, bg = "#ff6666")
name_label.pack()
name_entry.pack()

fill_label.pack()

regno_label = Label(text = "Vehicle registration number", font = ("consolas", 15), bg = "red")
regno_entry = Entry(font = ("Arial", 15), width = 25, bg = "#ff6666")
regno_label.pack()
regno_entry.pack()

fill_label1.pack()

quantity_label = Label(text = "Quantity", font = ("consolas", 15), bg = "red")
quantity_entry = Entry(font = ("Arial", 15), width = 25, bg = "#ff6666")
quantity_label.pack()
quantity_entry.pack()

fill_label2.pack()

serviceman_label = Label(text = "Serviceman name", font = ("consolas", 15), bg = "red")
serviceman_entry = Entry(font = ("Arial", 15), width = 25, bg = "#ff6666")
serviceman_label.pack()
serviceman_entry.pack()

fill_label4.pack()

print_button = Button(text = "Print bill", font = ("Arial", 15), bg = '#ff6666', command = print_bill)
print_button.pack()

window.mainloop()
