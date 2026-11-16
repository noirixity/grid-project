import tkinter as tk
arr = [["◼" for i in range(11)] for i in range(11)]
root = tk.Tk()
root.title("grid project")
x = 5
y = 5
t = tk.Text(root, font=("Arial", 20), width=18, height=11)
t.pack()
def update():
    t.config(state="normal")
    t.delete("1.0", "end")
    for j, row in enumerate(arr):
        for i, square in enumerate(row):
            if i == x and j == y:
                t.insert("end", square, "grey")
            else:
                t.insert("end", square)
        t.insert("end", "\n")
    t.config(state="disabled")
def kp(event):
    global x
    global y
    if event.keysym == "w":
        y -= 1
    elif event.keysym == "s":
        y += 1
    elif event.keysym == "a":
        x -= 1
    elif event.keysym == "d":
        x += 1
    if x >= 10:
        x = 10
    if x <= 0:
        x = 0
    if y >= 10:
        y = 10
    if y <= 0:
        y = 0
    update()
t.tag_config("grey", foreground="grey")
update()
root.bind("<Key>", kp)
root.mainloop()
