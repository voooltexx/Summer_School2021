from tkinter import *
import random
import time

game_width = 500
game_height = 500

snake_item = 10

snake_color1 = "green"
snake_color2 = "black"

snake_x = 24
snake_y = 24

snake_x_nav = 0
snake_y_nav = 0

snake_list = []
snake_size = 3

apples_list = []
apples_size = 15

root = Tk()
root.title("Snake v1.0")

root.resizable(0,0)

canvas = Canvas(root, width=game_width, height=game_height)
canvas.pack()

def can_we_delete():
    if len(snake_list) > snake_size:
        tmp_item = snake_list.pop(0)
        canvas.delete(tmp_item[2])
        canvas.delete(tmp_item[3])

for i in range(apples_size):
    x = tmp_x = random.randint(0, 49)
    y = tmp_y = random.randint(0, 49)
    id1 = canvas.create_oval(         x*snake_item, 
                            y*snake_item,
                            x*snake_item + snake_item, 
                            y*snake_item+snake_item,
                            fill = 'green')
    
    id2 = canvas.create_oval(x*snake_item + 2, 
                            y*snake_item + 2,
                            x*snake_item + snake_item - 2, 
                            y*snake_item+snake_item - 2,
                            fill = 'red')
    apples_list.append([tmp_x, tmp_y, id1, id2])

print(apples_list)

root.update()

def snake_moving():
    global snake

def snake_print_item(canvas, x, y):
    global snake_list
    if len(snake_list) > snake_size:
        tmp_item = snake_list.pop(0)
        canvas.delete(tmp_item[2])
        canvas.delete(tmp_item[3])
    id1 = canvas.create_rectangle(x*snake_item, 
                            y*snake_item,
                            x*snake_item + snake_item, 
                            y*snake_item+snake_item,
                            fill = snake_color2)
    
    id2 = canvas.create_rectangle(x*snake_item + 2, 
                            y*snake_item + 2,
                            x*snake_item + snake_item - 2, 
                            y*snake_item+snake_item - 2,
                            fill = snake_color1)
    snake_list.append([x,y,id1,id2])


snake_print_item(canvas, snake_x, snake_y)

def check_if_apples(x, y):
    global snake_size
    global apples_list
    for i in range(len(apples_list)):
        if apples_list[i][0] == x and apples_list[i][1] == y:
            canvas.delete(apples_list[i][2])
            canvas.delete(apples_list[i][3])
            snake_size += 1
            apples_list.pop(i)
            return

def game_over(x, y):
    global snake_size
    for i in range(len(snake_list)):
        pass


def snake_move(event):
    global snake_x
    global snake_y
    global snake_x_nav
    global snake_y_nav
    if event.keysym == "Up":
        snake_x_nav = 0
        snake_y_nav = -1
    elif event.keysym == "Down":
        snake_x_nav = 0
        snake_y_nav = 1
    elif event.keysym == "Left":
        snake_x_nav = -1
        snake_y_nav = 0
    elif event.keysym == "Right":
        snake_x_nav = 1
        snake_y_nav = 0
    snake_x  += snake_x_nav
    snake_y  += snake_y_nav
    snake_print_item(canvas, snake_x, snake_y)
    check_if_apples(snake_x, snake_y)

canvas.bind_all("<KeyPress-Left>", snake_move)
canvas.bind_all("<KeyPress-Right>", snake_move)
canvas.bind_all("<KeyPress-Up>", snake_move)
canvas.bind_all("<KeyPress-Down>", snake_move)

while 1:
    can_we_delete()
    snake_x += snake_x_nav
    snake_y += snake_y_nav
    snake_print_item(canvas, snake_x, snake_y)
    check_if_apples(snake_x, snake_y)
    root.update_idletasks()
    root.update()
    time.sleep(0.09)

root.mainloop()
