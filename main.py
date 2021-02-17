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
reps = 0
CHECKS = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", foreground=GREEN)
    canvas.itemconfig(time_text, text="00:00")
    global CHECKS, reps
    CHECKS = ""
    check_mark.config(text=CHECKS)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global CHECKS
    reps += 1
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 20

    if reps % 8 == 0:
        timer_label.config(text="Break", foreground=PINK)
        count_down(long_break)
    elif reps % 2 != 0:
        timer_label.config(text="Work", foreground=GREEN)
        count_down(work)
    elif reps % 2 == 0:
        timer_label.config(text="Break", foreground=RED)
        count_down(short_break)
    if reps % 2 == 0:
        CHECKS += "✔"
        check_mark.config(text=CHECKS)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo_image)
time_text = canvas.create_text(112, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

timer_label = Label(text="Timer", font=(FONT_NAME, 60, "normal"), foreground=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=1, row=3)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=3, row=3)

check_mark = Label(foreground=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 30, "bold"))
check_mark.grid(column=2, row=4)

window.mainloop()
