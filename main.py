import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(200, 300)

weight_label = tkinter.Label(text="Enter Your Weight (kg)")
weight_label.place(relx=0.5, y=40, anchor="center")

height_label = tkinter.Label(text="Enter Your Height (cm)")
height_label.place(relx=0.5, y=100, anchor="center")

weight_entry = tkinter.Entry()
weight_entry.place(width=100, height=20, relx=0.5, y=70, anchor="center")

height_entry = tkinter.Entry()
height_entry.place(width=100, height=20, relx=0.5, y=130, anchor="center")

final_label = tkinter.Label()
final_label.place(relx=0.5, y=220, anchor="center")
def button_click():
    if len(weight_entry.get()) == 0 or len(height_entry.get()) == 0:
        final_label.config(text="Please enter both weight and height!")
    else:
        try:
            x = (float(weight_entry.get()) / ((float(height_entry.get())/100)**2))
            if x < 18.5:
                final_label.config(text=f"Your BMI is {round(x,2)}.\nYou are under weight!")
            elif 18.5 <= x <= 24.9:
                final_label.config(text=f"Your BMI is {round(x,2)}.\nYou are normal")
            elif 24.9 < x <= 29.9:
                final_label.config(text=f"Your BMI is {round(x,2)}.\nYou are over weight!")
            elif 29.9 < x <= 34.9:
                final_label.config(text=f"Your BMI is {round(x,2)}.\nYou are obese (class I)!")
            elif 34.9 < x <= 39.9:
                final_label.config(text=f"Your BMI is {round(x,2)}.\nYou are obese (class II)!")
            elif 39.9 < x:
                final_label.config(text=f"Your BMI is {round(x,2)}.\nYou are extremely obese!!")
        except ValueError:
            final_label.config(text="Please enter valid number!")

my_button = tkinter.Button(width=10, text="Calculate", command=button_click)
my_button.place(relx=0.5, y=170, anchor="center")

window.mainloop()
