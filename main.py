import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 1


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    canvas.itemconfig(timer, text='00:00')
    window.after_cancel(window.after_id)
    timer_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    window.state(newstate='normal')
    window.attributes('-topmost', True)
    global reps
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps in [1, 3, 5, 7]:
        timer_label.config(text="Work!")
        count_down(work_sec)
        reps += 1
    elif reps == 8:
        timer_label.config(text="Long break :)")
        count_down(long_sec)
        check_mark.config(text=4 * "✔")
    elif reps % 2 == 0:
        timer_label.config(text="Break :)")
        count_down(short_sec)
        reps += 1
        check_mark.config(text=(reps // 2) * "✔")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer, text=f'{count_min:02d}:{count_sec:02d}')
    if count > 0:
        window.after_id = window.after(1000, count_down, count - 1)
    elif reps == 8:
        timer_label.config(text="FINISHED!")
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.minsize(width=450, height=400)
window.config(background=YELLOW, padx=100, pady=50)
window.title("Pomodoro")

canvas = Canvas(width=205, height=224, background=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(102, 130, text="00:00", font=(FONT_NAME, 18, "bold"), fill="white")
canvas.grid(column=1, row=1)

timer_label = Label()
timer_label.config(text="Timer", font=(FONT_NAME, 34, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_mark = Label(text="", font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg='green')
check_mark.grid(column=1, row=3)

start_button = Button(text="Start", fg="black", bg="white", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", fg="black", bg="white", command=reset)
reset_button.grid(column=2, row=2)

window.mainloop()
