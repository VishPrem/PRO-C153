from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.geometry("500x400")
window.configure(bg="sky blue")

heading_label = Label(window, text="Interest Calculator", fg="black", bg="purple", font=("Calibri", 20), bd=5)
heading_label.place(x=50, y=20)

p_label = Label(window, text="Enter Principal:", fg="black", bg="sky blue", font = ("Calibri", 12))
p_label.place(x=20, y=100)
p_entry = Entry(window, text="", bd=2, width=15)
p_entry.place(x=150, y=102)

r_label = Label(window, text="Enter ROI:", fg="black", bg="sky blue", font = ("Calibri", 12))
r_label.place(x=20, y=150)
r_entry = Entry(window, text="", bd=2, width=15)
r_entry.place(x=150, y=152)

t_label = Label(window, text="Enter Time:", fg="black", bg="sky blue", font = ("Calibri", 12))
t_label.place(x=20, y=200)
t_entry = Entry(window, text="", bd=2, width=15)
t_entry.place(x=150, y=202)

result_frame = LabelFrame(window, text="Result", bg="grey", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20, y=300)
show_label = Label(result_frame, text="Your result will be displayed here", bg="grey", font=("Calibri", 12), width=55)
show_label.place(x=20, y=20)
show_label.pack()

def calculate():
    p = float(p_entry.get())
    r = float(r_entry.get())
    t = float(t_entry.get())
    i = (p * r * t) / 100
    i = round(i, 2)
    show_label.destroy()
    message = Label(result_frame, text="Interest on $" + str(p) + " at rate of interest " + str(r) + " for " + str(t) + " years is " + str(i), bg="grey", font=("Calibri", 12), width=55)
    message.place(x=20, y=40)
    message.pack()

calculate_button = Button(window, text="Calculate", fg="black", bg="yellow", bd=4, command=calculate)
calculate_button.place(x=20, y=250)

window.mainloop()