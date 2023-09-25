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
timer_window = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_window)
    canvas.itemconfig(timer, text="00:00")
    header_label.config(text="Timer")
    count_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 2 != 0:
        count_down(work_sec)
        header_label.config(text="Work", fg=GREEN)
    elif reps == 8:
        count_down(long_break_sec)
        header_label.config(text="Break", fg=RED)
    else:
        count_down(short_break_sec)
        header_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_window
        timer_window = window.after(1000, count_down, count - 1)
    else:
        global reps
        start_timer()
        rep_count = ""
        for n in range(math.floor(reps/2)):
            rep_count += "🍅"
        count_label.config(text=rep_count)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Widget")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer type label
header_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
header_label.grid(column=2, row=1)

# Tomato Canvas
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=tomato_img)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Start Button
start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

# Rest Button
reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

# Count Label
count_label = Label(fg=GREEN, bg=YELLOW)
count_label.grid(column=2, row=4)

window.mainloop()
