import tkinter as tk

def button_click():
    print("دکمه فشرده شد!")

# ایجاد یک پنجره
window = tk.Tk()
window.title("نمونه برنامه با دکمه")

# ایجاد یک دکمه
button = tk.Button(window, text="کلیک کنید", command=button_click)
button.pack()

# نمایش پنجره
window.mainloop()