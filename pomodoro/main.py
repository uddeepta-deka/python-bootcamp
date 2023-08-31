from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps: int = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="TIMER")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_secs)
        timer_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_secs)
        timer_label.config(text="BREAK", fg=PINK)
    else:
        countdown(work_secs)
        timer_label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    count_mins = math.floor(count / 60)
    count_secs = count % 60
    if count_secs < 10:
        count_secs = "0" + str(count_secs)
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        global reps
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="TIMER", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 25), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 25), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()
