import tkinter


def miles_to_km():
    value_miles = input_miles.get()
    value_km = round(float(value_miles) * 1.60934, 3)
    result_label.config(text=value_km)


window = tkinter.Tk()  # equivalent to Screen class in the turtle module
window.title("Miles to Km converter")
window.minsize(width=500, height=300)
window.config(padx=25, pady=25)

# Label
miles_label = tkinter.Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)

km_label = tkinter.Label(text="Km", font=("Arial", 24, "bold"))
km_label.grid(column=2, row=1)

is_equal_label = tkinter.Label(text="Is equal to", font=("Arial", 24))
is_equal_label.grid(column=0, row=1)

result_label = tkinter.Label(text="0", font=("Arial", 20))
result_label.grid(column=1, row=1)

# Button
button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

# Entry
input_miles = tkinter.Entry(width=7)
input_miles.grid(column=1, row=0)


window.mainloop()  # This always has to be at the very end of the code
