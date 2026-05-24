import tkinter as tk

root = tk.Tk()
root.title("SFIT Form Validation")
root.geometry("1000x1000")

image=tk.PhotoImage(file="jay1.png")

label=tk.Label(root,image=image)
label.place(x=0,y=0)

is_dark_mode = tk.BooleanVar(value=False)

# Widgets
name_label = tk.Label(root, text="Enter your name" ,font=("Arial",15))
name_label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

age_label = tk.Label(root, text="Enter your age", font=("Arial",15))
age_label.pack(pady=10)

scale = tk.Scale(root, from_=0, to=100, orient="horizontal")
scale.pack(pady=10)

branch_label = tk.Label(root, text="Select your Branch",font=("Arial",15))
branch_label.pack(pady=10)

check_var = tk.BooleanVar()
checkbutton1 = tk.Checkbutton(root, text="CMPN", variable=check_var)
checkbutton1.pack(pady=10)

check_var1=tk.BooleanVar()
checkbutton2 = tk.Checkbutton(root, text="IT", variable=check_var1)
checkbutton2.pack(pady=10)


division_label = tk.Label(root, text="Select your Division",font=("Arial",15))
division_label.pack(pady=10)

division_var = tk.IntVar()
radiobutton1 = tk.Radiobutton(root, text="A", variable=division_var, value=1, font=("Arial",10))
radiobutton2 = tk.Radiobutton(root, text="B", variable=division_var, value=2, font=("Arial",10))
radiobutton3 = tk.Radiobutton(root, text="C", variable=division_var, value=3 , font=("Arial",10))
radiobutton1.pack(pady=5)
radiobutton2.pack(pady=5)
radiobutton3.pack(pady=5)

pref_label = tk.Label(root, text="Select any one preference",font=("Arial",15))
pref_label.pack(pady=10)

preference_var = tk.IntVar()
radiobutton4 = tk.Radiobutton(root, text="Coding", variable=preference_var, value=4, font=("Arial",10))
radiobutton5 = tk.Radiobutton(root, text="Editing", variable=preference_var, value=5, font=("Arial",10))
radiobutton6 = tk.Radiobutton(root, text="Graphic Designing", variable=preference_var, value=6, font=("Arial",10))
radiobutton4.pack(pady=5)
radiobutton5.pack(pady=5)
radiobutton6.pack(pady=5)

def on_button_click():
    print(f"Name: {entry.get()}")
    print(f"Age: {scale.get()}")
    print(f"Branch CMPN selected: {check_var.get()}")
    print(f"Division selected: {division_var.get()}")
    print(f"Preference selected: {preference_var.get()}")

button = tk.Button(root, text="Submit", command=on_button_click)
button.pack(pady=30)

def toggle_theme():
    if is_dark_mode.get():
        bg_color = "#2e2e2e"
        fg_color = "#ffffff"
    else:
        bg_color = "#d0e7f9"
        fg_color = "#000000"

    root.configure(bg=bg_color)
    for widget in all_widgets:
        try:
            widget.configure(bg=bg_color, fg=fg_color)
        except:
            pass
    entry.configure(insertbackground=fg_color)

toggle_button = tk.Checkbutton(root, text="Dark Mode", variable=is_dark_mode, command=toggle_theme)
toggle_button.pack()

# Store all widgets for theme toggle
all_widgets = [
    name_label, entry, age_label, scale, branch_label, checkbutton1,checkbutton2,
    division_label, radiobutton1, radiobutton2, radiobutton3,
    pref_label, radiobutton4, radiobutton5, radiobutton6,
    button, toggle_button
]

toggle_theme()
root.mainloop()
