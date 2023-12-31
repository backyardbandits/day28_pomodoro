from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

lb_title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
lb_title.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo_tomato)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=1, column=1)



bt_start = Button(text="Start", bg=YELLOW, bd=0, highlightthickness=0)
bt_start.grid(row=2, column=0)

bt_reset = Button(text="Reset", bg=YELLOW, bd=0, highlightthickness=0)
bt_reset.grid(row=2, column=2)

lb_check = Label(text="✓", fg=GREEN, bg=YELLOW)
lb_check.grid(row=3, column=1)



# ----------------------------------------------------------- #
window.mainloop()