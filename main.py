from tkinter  import *;
import math;

check_mark_text = "✔";
total_checks = "";
timer = 25 * 60;
break_timer = 5 * 60;
long_break_timer = 20 * 60;
reps = 0;
timer_exec = None;


def count_down(count):
    global timer_exec;
    print(count);
    min = math.floor(count / 60);
    secs = count % 60;
    if secs < 10:
        secs = f"0{secs}";
    txt = f"{min}:{secs}";
    canvas.itemconfig(timer_text, text = txt);
    if count > 0:
        timer_exec = window.after(1000,count_down,count - 1);
    else:
         start_timer();

def reset_timer():
    global reps;
    global timer_exec;
    global total_checks;
    label_title.config(text="Pomodoro Timer",fg = "#9bdeac");
    canvas.itemconfig(timer_text, text = "60:00");
    total_checks = "";
    reps = 0;
    window.after_cancel(timer_exec);
    check_list.config(text = total_checks);

def start_timer():
    global reps;
    global total_checks;
    chosen_timer = timer;
    txt = "";
    color= "";
    reps +=1;
    print(reps);

    if reps % 8 == 0:
         chosen_timer = long_break_timer;
         txt = "Long Break";
         color = "#e7305b";  
         total_checks += check_mark_text;
    elif reps % 2 ==0:
         chosen_timer = break_timer;
         txt = "Short Break";
         color = "#e2979c";
         total_checks += check_mark_text;
    else :
         chosen_timer = timer;
         txt = "Work!";
         color = "#9bdeac";
             
    label_title.config(text=txt,fg = color);
    check_list.config(text = total_checks);
    print(chosen_timer);
    count_down(chosen_timer);

window = Tk();

window.config(padx=100,pady=40,bg = "#f7f5dd");


label_title = Label(text=f"Pomodoro Timer",font=("Courier",30,"bold"), fg = "#9bdeac" ,  bg = "#f7f5dd");
label_title.grid(row=0,column=2);

canvas = Canvas(width=200,height=224,bg="#f7f5dd",highlightthickness=0);

src = PhotoImage(file = "./imgs/tomato.png");

tomato = canvas.create_image(100,112,image = src);
timer_text = canvas.create_text(100,130,text="60:00",fill="white",font=("Courier",35,"bold"));

canvas.grid(row=1,column=2);

check_list = Label(text = "", font=("Courier","15","normal"), fg = "#9bdeac", bg="#f7f5dd");
check_list.grid(row=4,column=2);


start_btn = Button(text = "Start Timer",highlightthickness=0,command = start_timer);
reset_btn = Button(text = "Reset",highlightthickness=0, command = reset_timer);

start_btn.grid(row=5,column=1);
reset_btn.grid(row=5,column=4);


window.mainloop();



