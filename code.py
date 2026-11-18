import tkinter as tk # this code is very confusing 
arr = [["◼" for i in range(11)] for i in range(11)] 
root = tk.Tk() 
root.title("grid project") 
x = 5 
y = 5 
x2 = 6 
y2 = 6 
t = tk.Text(root, font=("Arial", 20), width=25, height=11) 
t.pack() 
dr = 0 
dr2 = 0 
def update(): # without this there is no display so its vital 
    t.config(state="normal") 
    t.delete("1.0", "end") 
    for j, row in enumerate(arr): 
        for i, square in enumerate(row): 
            if i == x and j == y: 
                t.insert("end", square, "blue") 
            elif i == x2 and j == y2: 
                t.insert("end", square, "red") 
            else: 
                t.insert("end", square) 
        t.insert("end", "\n") 
    t.config(state="disabled") 
def kp(event):  
    global x,y,x2,y2,dr,dr2 
    if event.keysym == "w": # movement p1 
        y -= 1 
        dr = "north" 
    elif event.keysym == "s": 
        y += 1 
        dr = "south" 
    elif event.keysym == "a": 
        x -= 1 
        dr = "west" 
    elif event.keysym == "d": 
        x += 1 
        dr = "east" 
    elif event.keysym == "Up": # movement p2 
        y2 -= 1 
        dr2 = "north" 
    elif event.keysym == "Down": 
        y2 += 1 
        dr2 = "south" 
    elif event.keysym == "Left": 
        x2 -= 1 
        dr2 = "west" 
    elif event.keysym == "Right": 
        x2 += 1 
        dr2 = "east" 
    elif event.keysym == "q": # dash p1 
        if dr == "north": 
            y -= 3 
        elif dr == "south": 
            y += 3 
        elif dr == "west": 
            x -= 3 
        elif dr == "east": 
            x += 3 
    elif event.keysym == "Control_R": # dash p2 
        if dr2 == "north": 
            y2 -= 3 
        elif dr2 == "south": 
            y2 += 3 
        elif dr2 == "west": 
            x2 -= 3 
        elif dr2 == "east": 
            x2 += 3 
    if x >= 10: 
        x = 10 
    if x <= 0: 
        x = 0 
    if y >= 10: 
        y = 10 
    if y <= 0: 
        y = 0 
    if x2 >= 10: 
        x2 = 10 
    if x2 <= 0: 
        x2 = 0 
    if y2 >= 10: 
        y2 = 10 
    if y2 <= 0: 
        y2 = 0 
    update() 
t.tag_config("blue", foreground="blue") 
t.tag_config("red", foreground="red") 
update() 
root.bind("<Key>", kp) 
root.mainloop() 
# todo list 
#  
# furnish it a little more 
# notes to self: 
