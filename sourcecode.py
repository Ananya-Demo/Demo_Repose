'''PROGRAM TO COLLECT DATA FROM USERS REGARDING THEIR EXPERIENCE WHEN THEY FACED COVID 19 AND CALCULATING THE SUCCESS RATE OF COVID-19 VACCINE'''
from tkinter import *
from tkinter import ttk

# Window
root = Tk()
root.attributes('-fullscreen', True)
root.title("Covid-19 Vaccine Form")

list = []

error = Label(root)

main_frm = Frame(root, bg="#374678")
main_frm.place(relx=0, rely=0, relheight=1, relwidth=1)

shadow_frm = Frame(main_frm, bg="#232729")
shadow_frm.place(relx=0.34, rely=0.14, relheight=0.80, relwidth=0.38)

# Page 1
cnvs_1 = Canvas(main_frm, bg="white", highlightthickness=0)
cnvs_1.place(relx=0.31, rely=0.1, relheight=0.80, relwidth=0.38)

# Exit Program Button
exit_btn_1 = Button(cnvs_1, text="x", font=("Arial", 15), bg="white", fg="#232729", bd=0, command=root.destroy)
exit_btn_1.place(relx=0.93, rely=0.03, relheight=0.03, relwidth=0.04)

def forward_1():  # Next Page Function
    global error
    error.place_forget()
    try:
        name = name_ent.get()
        age = age_ent.get()
        height = height_ent.get()
        weight = weight_ent.get()
        if name == "" or age == "" or height == "" or weight == "":  # Checking if any of the entry boxes aren't filled
            error = Label(cnvs_1, text="Error! All info is required to be filled in.", font=("Arial", 13), bg="#f51414",
                          fg="white")

            error.place(relx=0.075, rely=0.135, relheight=0.04, relwidth=0.85)
        else:
            age, height, weight = int(age), float(height), float(weight)
            cnvs_1.place_forget()
            cnvs_2.place(relx=0.31, rely=0.1, relheight=0.80, relwidth=0.38)
    except ValueError:
        error = Label(cnvs_1, text="Error! Age, Height and Weight are to be entered in numbers", font=("Arial", 13),
                      bg="#f51414", fg="white")
        error.place(relx=0.075, rely=0.135, relheight=0.04, relwidth=0.85)


title_lbl = Label(cnvs_1, text="COVID-19 VACCINE FORM", font=("Arial", 17), bg="white", fg="#232729", anchor="w")
title_lbl.place(relx=0.1, rely=0.05, relheight=0.1, relwidth=0.8)

name_lbl = Label(cnvs_1, text="Name*", font=("Arial", 13), bg="white", fg="#232729", anchor="w")
name_lbl.place(relx=0.1, rely=0.2, relheight=0.05, relwidth=0.8)

# Name Entry Box
name_ent = Entry(cnvs_1, font=("Arial", 13), relief=SOLID, bd=0.5)
name_ent.place(relx=0.1, rely=0.25, relheight=0.05, relwidth=0.8)

age_lbl = Label(cnvs_1, text="Age in numbers*", font=("Arial", 13), bg="white", fg="#232729", anchor="w")
age_lbl.place(relx=0.1, rely=0.325, relheight=0.05, relwidth=0.8)

# Age Entry Box
age_ent = Entry(cnvs_1, font=("Arial", 13), relief=SOLID, bd=0.5)
age_ent.place(relx=0.1, rely=0.375, relheight=0.05, relwidth=0.8)

gender_lbl = Label(cnvs_1, text="Gender*", font=("Arial", 13), bg="white", fg="#232729", anchor="w")
gender_lbl.place(relx=0.1, rely=0.45, relheight=0.05, relwidth=0.8)

gender = ["Male", "Female"]

# Gender Box with options
gender_cb = ttk.Combobox(cnvs_1, value=gender,state="readonly",font=20)
gender_cb.current(0)
gender_cb.place(relx=0.1, rely=0.5, relheight=0.05, relwidth=0.8)

height_lbl = Label(cnvs_1, text="Height in numbers (cm)*", bg="white", fg="#232729", font=("Arial", 13), anchor="w")
height_lbl.place(relx=0.1, rely=0.575, relheight=0.05, relwidth=0.8)

# Height Entry Box
height_ent = Entry(cnvs_1, font=("Arial", 13), relief=SOLID, bd=0.5)
height_ent.place(relx=0.1, rely=0.625, relheight=0.05, relwidth=0.8)

weight_lbl = Label(cnvs_1, text="Weight in numbers (kg)*", bg="white", fg="#232729", font=("Arial", 13), anchor="w")
weight_lbl.place(relx=0.1, rely=0.7, relheight=0.05, relwidth=0.8)

# Weight Entry Box
weight_ent = Entry(cnvs_1, font=("Arial", 13), relief=SOLID, bd=0.5)
weight_ent.place(relx=0.1, rely=0.75, relheight=0.05, relwidth=0.8)

page_lbl_1 = Label(cnvs_1, text="1 of 3", font=("Arial", 10), bg="white", fg="#232729")
page_lbl_1.place(relx=0.44, rely=0.9, relheight=0.05, relwidth=0.12)

# Next Page Button
for_btn_1 = Button(cnvs_1, text="Next", font=("Arial", 10), bg="#232729", fg="#c9c9c9", bd=0, command=forward_1)
for_btn_1.place(relx=0.56, rely=0.9, relheight=0.05, relwidth=0.12)

cnvs_1.create_line(40, 95, 480, 95, fill="#232729")

# Page 2
cnvs_2 = Canvas(main_frm, bg="white", highlightthickness=0)

# Exit Program Button
exit_btn_2 = Button(cnvs_2, text="x", font=("Arial", 15), bg="white", fg="#232729", bd=0, command=root.destroy)
exit_btn_2.place(relx=0.93, rely=0.03, relheight=0.03, relwidth=0.04)


def forward_2():  # Next Page Function
    cnvs_2.place_forget()
    cnvs_3.place(relx=0.31, rely=0.1, relheight=0.80, relwidth=0.38)


def back_2():  # Previous Page Function
    cnvs_2.place_forget()
    cnvs_1.place(relx=0.31, rely=0.1, relheight=0.80, relwidth=0.38)


page_lbl_2 = Label(cnvs_2, text="2 of 3", font=("Arial", 10), bg="white", fg="#232729")
page_lbl_2.place(relx=0.44, rely=0.9, relheight=0.05, relwidth=0.12)

# Next Page Button
for_btn_2 = Button(cnvs_2, text="Next", font=("Arial", 10), bg="#232729", fg="#c9c9c9", bd=0, command=forward_2)
for_btn_2.place(relx=0.56, rely=0.9, relheight=0.05, relwidth=0.12)

# Previous Page Button
back_btn_2 = Button(cnvs_2, text="Previous", font=("Arial", 10), bg="#232729", fg="#c9c9c9", bd=0, command=back_2)
back_btn_2.place(relx=0.32, rely=0.9, relheight=0.05, relwidth=0.12)

lbl_1 = Label(cnvs_2, text="Are you suffering from any of these?", font=("Arial", 17), bg="white", fg="#232729",
              anchor="w")
lbl_1.place(relx=0.1, rely=0.075, relheight=0.1, relwidth=0.8)

# Checkboxes
v1 = IntVar()

_1 = Checkbutton(cnvs_2, text="  Covid\n  (or did you have)", font=("Arial", 13), bg="white", fg="#232729", variable=v1,
                 anchor="w", justify=LEFT)
_1.place(relx=0.1, rely=0.2, relheight=0.1, relwidth=0.4)

v2 = IntVar()

_2 = Checkbutton(cnvs_2, text="  Blood Disorders\n  (Sickle cell anemia\n  or thalassemia)", font=("Arial", 13),
                 bg="white", fg="#232729", variable=v2, anchor="w", justify=LEFT)
_2.place(relx=0.1, rely=0.325, relheight=0.1, relwidth=0.4)

v3 = IntVar()

_3 = Checkbutton(cnvs_2, text="  Heart Disease", font=("Arial", 13), bg="white", fg="#232729", variable=v3, anchor="w")
_3.place(relx=0.1, rely=0.45, relheight=0.1, relwidth=0.4)

v4 = IntVar()

_4 = Checkbutton(cnvs_2, text="  Diabetes", font=("Arial", 13), bg="white", fg="#232729", variable=v4, anchor="w")
_4.place(relx=0.1, rely=0.575, relheight=0.1, relwidth=0.4)

v5 = IntVar()

_5 = Checkbutton(cnvs_2, text="  Severe Obesity", font=("Arial", 13), bg="white", fg="#232729", variable=v5, anchor="w")
_5.place(relx=0.1, rely=0.7, relheight=0.1, relwidth=0.4)

v6 = IntVar()

_6 = Checkbutton(cnvs_2, text="  Cancer", font=("Arial", 13), bg="white", fg="#232729", variable=v6, anchor="w")
_6.place(relx=0.6, rely=0.2, relheight=0.1, relwidth=0.4)

v7 = IntVar()

_7 = Checkbutton(cnvs_2, text="  Lung Problems", font=("Arial", 13), bg="white", fg="#232729", variable=v7, anchor="w")
_7.place(relx=0.6, rely=0.325, relheight=0.1, relwidth=0.4)

v8 = IntVar()

_8 = Checkbutton(cnvs_2, text="  Weakened Immune\n  System", font=("Arial", 13), bg="white", fg="#232729", variable=v8,
                 anchor="w", justify=LEFT)
_8.place(relx=0.6, rely=0.45, relheight=0.1, relwidth=0.4)

v9 = IntVar()

_9 = Checkbutton(cnvs_2, text="  Chronic Kidney\n  Disease", font=("Arial", 13), bg="white", fg="#232729", variable=v9,
                 anchor="w", justify=LEFT)
_9.place(relx=0.6, rely=0.575, relheight=0.1, relwidth=0.4)

v10 = IntVar()

_10 = Checkbutton(cnvs_2, text="  Chronic Liver\n  Disease", font=("Arial", 13), bg="white", fg="#232729", variable=v10,
                  anchor="w", justify=LEFT)
_10.place(relx=0.6, rely=0.7, relheight=0.1, relwidth=0.4)

cnvs_2.create_line(260, 100, 260, 500, fill="#232729")

# Page 3
cnvs_3 = Canvas(main_frm, bg="white", highlightthickness=0)

# Exit Program Button
exit_btn_3 = Button(cnvs_3, text="x", font=("Arial", 15), bg="white", fg="#232729", bd=0, command=root.destroy)
exit_btn_3.place(relx=0.93, rely=0.03, relheight=0.03, relwidth=0.04)


def back_3():  # Previous Page Function
    cnvs_3.place_forget()
    cnvs_2.place(relx=0.31, rely=0.1, relheight=0.80, relwidth=0.38)


page_lbl_3 = Label(cnvs_3, text="3 of 3", font=("Arial", 10), bg="white", fg="#232729")
page_lbl_3.place(relx=0.44, rely=0.9, relheight=0.05, relwidth=0.12)

# Previous Page Button
back_btn_3 = Button(cnvs_3, text="Previous", font=("Arial", 10), bg="#232729", fg="#c9c9c9", bd=0, command=back_3)
back_btn_3.place(relx=0.32, rely=0.9, relheight=0.05, relwidth=0.12)

vac_lbl = Label(cnvs_3, text="Have you taken the COVID vaccine?", font=("Arial", 17), bg="white", fg="#232729")
vac_lbl.place(relx=0.02, rely=0.12, relheight=0.1, relwidth=0.96)

vac = StringVar()
vac.set("No")

# Yes or No Buttons
Radiobutton(cnvs_3, text="Yes", font=("Arial", 13), bg="white", fg="#232729", variable=vac, value="Yes").place(
relx=0.39, rely=0.244, relheight=0.06, relwidth=0.1)
Radiobutton(cnvs_3, text="No", font=("Arial", 13), bg="white", fg="#232729", variable=vac, value="No").place(relx=0.515,
                                                                                                             rely=0.244,
                                                                                                             relheight=0.06,
                                                                                                             relwidth=0.1)

cov_lbl = Label(cnvs_3, text="If yes, have gotten COVID after that?", font=("Arial", 17), bg="white", fg="#232729")
cov_lbl.place(relx=0.02, rely=0.55, relheight=0.1, relwidth=0.96)

cov = StringVar()
cov.set("No")

# Yes or No Buttons
Radiobutton(cnvs_3, text="Yes", font=("Arial", 13), bg="white", fg="#232729", variable=cov, value="Yes").place(
    relx=0.39, rely=0.682, relheight=0.06, relwidth=0.1)
Radiobutton(cnvs_3, text="No", font=("Arial", 13), bg="white", fg="#232729", variable=cov, value="No").place(relx=0.515,
                                                                                                             rely=0.682,
                                                                                                             relheight=0.06,
                                                                                                             relwidth=0.1)


def submit():  # Submit Form Function
    global list
    name = name_ent.get()
    name_ent.delete(0, "end")
    age = int(age_ent.get())
    age_ent.delete(0, "end")
    gender = gender_cb.get()
    gender_cb.current(0)

    height = float(height_ent.get())
    height_ent.delete(0, "end")
    weight = float(weight_ent.get())
    weight_ent.delete(0, "end")
    person = []  # Storing person's info
    cnvs_3.place_forget()
    cnvs_4.place(relx=0.31, rely=0.1, relheight=0.80, relwidth=0.38)
    if v1.get() == 0 and v2.get() == 0 and v3.get() == 0 and v4.get() == 0 and v5.get() == 0 and v6.get() == 0 and v7.get() == 0 and v8.get() == 0 and v9.get() == 0 and v10.get() == 0:
        pass
    elif vac.get() == "No":
        pass
    else:
        person.extend([name, age, gender, height, weight])
        if v1.get() == 1:
            person.append("COVID")
        if v2.get() == 1:
            person.append("Blood Disorders")
        if v3.get() == 1:
            person.append("Heart Disease")
        if v4.get() == 1:
            person.append("Diabetes")
        if v5.get() == 1:
            person.append("Severe Obesity")
        if v6.get() == 1:
            person.append("Cancer")
        if v7.get() == 1:
            person.append("Lung Problems")
        if v8.get() == 1:
            person.append("Weakened Immune System")
        if v9.get() == 1:
            person.append("Chronic Kidney Disease")
        if v10.get() == 1:
            person.append("Chronic Liver Disease")
        person.append(cov.get())
        list.append(
            person)  # Storing list of person's info in the main list, only if they are from a High Risk Category and they have taken the vaccine


# Submit Form Button
submit_btn = Button(cnvs_3, text="Submit", font=("Arial", 10), bg="#f51414", fg="white", bd=0, command=submit)
submit_btn.place(relx=0.56, rely=0.9, relheight=0.05, relwidth=0.12)

cnvs_3.create_line(50, 280, 475, 280, fill="#232729")

# Page 4
cnvs_4 = Canvas(main_frm, bg="white", highlightthickness=0)

# Exit Program Button
exit_btn_4 = Button(cnvs_4, text="x", font=("Arial", 15), bg="white", fg="#232729", bd=0, command=root.destroy)
exit_btn_4.place(relx=0.93, rely=0.03, relheight=0.03, relwidth=0.04)


def add():  # Redoing form for another person
    cnvs_4.place_forget()
    error.place_forget()
    vac.set("No")
    cov.set("No")
    _1.deselect()
    _2.deselect()
    _3.deselect()
    _4.deselect()
    _5.deselect()
    _6.deselect()
    _7.deselect()
    _8.deselect()
    _9.deselect()
    _10.deselect()
    cnvs_1.place(relx=0.31, rely=0.1, relheight=0.80, relwidth=0.38)


lbl_2 = Label(cnvs_4, text="Thank you\nand stay safe!", font=("Arial", 20), bg="white", fg="#232729")
lbl_2.place(relx=0.1, rely=0.3, relheight=0.2, relwidth=0.8)

# Add Another Person Button
add_btn = Button(cnvs_4, text="+ Another person", font=("Arial", 17), bg="#f51414", fg="red", bd=0, command=add)
add_btn.place(relx=0.25, rely=0.5, relheight=0.1, relwidth=0.5)

root.mainloop()
#part 2
# Printing Main List
print(list)

a1 = b1 = a2 = b2 = a3 = b3 = a4 = b4 = a5 = b5 = a6 = b6 = a7 = b7 = a8 = b8 = a9 = b9 = a10 = b10 = 0

import matplotlib.pyplot as plt

# Gathering Data to plot graph
for i in range(len(list)):
    if 'COVID' in list[i]:
        if 'Yes' in list[i]:
            a1 += 1
        else:
            b1 += 1
    if 'Lung Problems' in list[i]:
        if 'Yes' in list[i]:
            a2 += 1
        else:
            b2 += 1
    if 'Heart Disease' in list[i]:
        if 'Yes' in list[i]:
            a3 += 1
        else:
            b3 += 1
    if 'Diabetes' in list[i]:
        if 'Yes' in list[i]:
            a4 += 1
        else:
            b4 += 1
    if 'Severe Obesity' in list[i]:
        if 'Yes' in list[i]:
            a5 += 1
        else:
            b5 += 1
    if 'Cancer' in list[i]:
        if 'Yes' in list[i]:
            a6 += 1
        else:
            b6 += 1
    if 'Blood Disorders' in list[i]:
        if 'Yes' in list[i]:
            a7 += 1
        else:
            b7 += 1
    if 'Weakened Immune System' in list[i]:
        if 'Yes' in list[i]:
            a8 += 1
        else:
            b8 += 1
    if 'Chronic Kidney Disease' in list[i]:
        if 'Yes' in list[i]:
            a9 += 1
        else:
            b9 += 1
    if 'Chronic Liver Disease' in list[i]:
        if 'Yes' in list[i]:
            a10 += 1
        else:

            b10 += 1

# Calculating Percentage
if a1 + b1 == 0:
    p1 = 0
else:
    p1 = (b1 / (a1 + b1)) * 100
if a2 + b2 == 0:
    p2 = 0
else:
    p2 = (b2 / (a2 + b2)) * 100
if a3 + b3 == 0:
    p3 = 0
else:
    p3 = (b3 / (a3 + b3)) * 100
if a4 + b4 == 0:
    p4 = 0
else:
    p4 = (b4 / (a4 + b4)) * 100
if a5 + b5 == 0:
    p5 = 0
else:
    p5 = (b5 / (a5 + b5)) * 100
if a6 + b6 == 0:
    p6 = 0
else:
    p6 = (b6 / (a6 + b6)) * 100
if a7 + b7 == 0:
    p7 = 0
else:
    p7 = (b7 / (a7 + b7)) * 100
if a8 + b8 == 0:
    p8 = 0
else:
    p8 = (b8 / (a8 + b8)) * 100
if a9 + b9 == 0:
    p9 = 0
else:
    p9 = (b9 / (a9 + b9)) * 100
if a10 + b10 == 0:
    p10 = 0
else:
    p10 = (b10 / (a10 + b10)) * 100

# Plotting Graph


names = ['COVID', 'Lung\nProblems', 'Heart\nDisease', 'Diabetes', 'Severe\nObesity', 'Cancer', 'Blood\nDisorders',
         'Weakened\nImmune\nSystem', 'Chronic\nKidney\nDisease', 'Chronic\nLiver\nDisease']
values = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
plt.figure(figsize=(12, 6))
plt.bar(names, values)
plt.ylabel('Success Rate (%)')
plt.ylim(0, 100)
plt.title("Graph of the Success Rate of the Covid-19 Vaccine\non those that are from High Risk Categories")
plt.show()