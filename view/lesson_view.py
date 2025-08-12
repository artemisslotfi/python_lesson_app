from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from warnings import showwarning
from repository.lesson_repository import *
from tools.validation import *


# 5
def reset_form():
    code.set("")
    title.set("")
    teacher.set("")
    class_number.set("")
    unit.set(0)
    show_data_on_table(find_all())

def show_data_on_table(lesson_list):
    # خالی کردن جدول
    for item in table.get_children():
        table.delete(item)
    #درج داده ها از دیتابیس روی جدول
    for lesson in lesson_list:
        table.insert("", END, values=lesson)
# 6
def save_click():
    if title_validator(title.get()) and title_validator(teacher.get()) and class_number_validator(class_number.get()) and 0<unit.get()<=24:
        save(title.get(),teacher.get(),class_number.get(),unit.get())
        messagebox.showinfo("Save", f"Successfully saved!")
        reset_form()
        show_data_on_table(find_all())
    else:
        messagebox.showerror("Error", "Please enter a valid title/teacher/class number/unit")

# HomeWork
def edit_click():
    if title_validator(title.get()) and title_validator(teacher.get()) and class_number_validator(class_number.get()) and 0<unit.get()<=24:
        edit(code.get(),title.get(), teacher.get(), class_number.get(), unit.get())
        messagebox.showinfo("Edit", f"Successfully edited!")
        reset_form()
        show_data_on_table(find_all())
    else:
        messagebox.showerror("Error", "Please enter a valid code/title/teacher/class number/unit")

def remove_click():
    remove(code.get())
    messagebox.showinfo("Remove", f"Successfully removed!")
    reset_form()
    show_data_on_table(find_all())


# 7
def table_select(event):
    table_row=table.focus()
    selected=table.item(table_row)["values"]
    if selected:
        code.set(selected[0])
        title.set(selected[1])
        teacher.set(selected[2])
        class_number.set(selected[3])
        unit.set(selected[4])


def close_window():
    if messagebox.askyesno("Exit", "Are you sure ?"):
        win.destroy()


def search_lesson(event):
    lesson_list = find_by_title_and_teacher(title_search.get(), teacher_search.get())
    show_data_on_table(lesson_list)

# 0
win = Tk()
# geometry-title
win.title("Lesson")
win.resizable(width=False, height=False)
win.geometry("710x360")

# 1
# Code
code=StringVar()
Label(win,text="Code").place(x=20,y=20)
Entry(win, textvariable=code).place(x=100,y=20)

# Title
title=StringVar()
Label(win,text="Title").place(x=20,y=60)
Entry(win, textvariable=title).place(x=100,y=60)

# Teacher
teacher=StringVar()
Label(win,text="Teacher").place(x=20,y=100)
Entry(win, textvariable=teacher).place(x=100,y=100)
# Class Number
class_number=StringVar()
Label(win,text="Class Number").place(x=20,y=140)
Entry(win, textvariable=class_number).place(x=100,y=140)

# Unit
unit=IntVar()
Label(win,text="Unit").place(x=20,y=180)
Entry(win, textvariable=unit).place(x=100,y=180)

# 2
# Buttons (Save-Edit-Remove)
Button(win, text="Clear", command=reset_form, width=29).place(x=20,y=250)
Button(win, text="Save", command=save_click, width=7).place(x=20,y=300)
Button(win, text="Edit", command=edit_click, width=7).place(x=95,y=300)
Button(win, text="Remove", command=remove_click, width=7).place(x=170,y=300)
# 3
# Search Title
title_search = StringVar()
Label(win,text="Search Title").place(x=250,y=20)
title_search_txt = Entry(win, textvariable=title_search)
title_search_txt.bind("<KeyRelease>", search_lesson)
title_search_txt.place(x=325,y=20)

# Search Teacher
teacher_search = StringVar()
Label(win,text="Search Teacher").place(x=470,y=20)
teacher_search_txt = Entry(win, textvariable=teacher_search)
teacher_search_txt.bind("<KeyRelease>", search_lesson)
teacher_search_txt.place(x=560,y=20)


# 4
# Table
table = ttk.Treeview(win, height=12,columns=(1,2,3,4,5),show="headings")
table.column(1, width=70)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=80)
table.column(5, width=80)

table.heading(1, text="Code")
table.heading(2, text="Title")
table.heading(3, text="Teacher")
table.heading(4, text="Class Number")
table.heading(5, text="Unit")

# TreeviewSelect
# bind--> table_select
table.bind("<<TreeviewSelect>>", table_select)

table.place(x=250, y = 60)


win.protocol("WM_DELETE_WINDOW", close_window)

reset_form()

win.mainloop()