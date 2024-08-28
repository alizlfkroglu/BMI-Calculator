from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=300)
window.config(padx=20,pady=20)

def click_calculate():
    weight = my_entry.get()
    height = my_entry2.get()

    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight)/(float(height)/100) **2
            result_string =write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number")

my_label = Label(text="Enter Your Weight (kg)")
my_label.config(padx=10, pady=10)
my_label.pack()

my_entry = Entry(width=20,border=5)
my_entry.pack()

my_label2 = Label(text="Enter Your Height (cm)")
my_label2.config(padx=10, pady=10)
my_label2.pack()

my_entry2 = Entry(width=20, border=5)
my_entry2.pack()

my_button = Button(text="Calculate", command=click_calculate)
my_button.config(padx=5, pady=5)
my_button.pack()

result_label = Label()
result_label.pack()

def write_result(bmi):
    result_string = f"Your Bmi is: {round(bmi,2)}. You are "
    if bmi <=16:
        result_string += "severely thin!"
    elif 16 < bmi <= 17:
        result_string += "moderately thin"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin"
    elif 18.5 < bmi <= 25:
        result_string += "normal"
    elif 25 < bmi <= 30:
        result_string += "over weight"
    elif 30 < bmi <= 35:
        result_string += "obese class 1"
    elif 35 < bmi <= 40:
        result_string += "obese class 2"
    else:
        result_string += "obese class 3"

    return result_string

window.mainloop()

