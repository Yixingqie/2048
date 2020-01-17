import turtle
import os
import random
import math

# Set up screen
totalpoints = 0;
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("2048")
wn.setup(width = 600, height = 700)

boreder_pen = turtle.Turtle()
boreder_pen.speed(0)
boreder_pen.color("white")
boreder_pen.penup()
boreder_pen.setposition(-250,-200)
boreder_pen.pendown()
boreder_pen.pensize(10)
for side in range(4):
    boreder_pen.fd(500)
    boreder_pen.lt(90)
boreder_pen.hideturtle()

grid  = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

numbers = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.shapesize(4.5,4.5,0)
top  = 200
left  =-150

colors = ["white", "gray", "lightblue", "green", "orange", "purple", "red", "magenta", "cyan", "navyblue", "olive"]

def draw_grid(pen,grid):
    top  = 200
    left  =-150
   
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x = left + (x *100)
            screen_y = top - (y*100)
            color_number = grid[y][x]
            color = colors[color_number]
            pen.color(color)
            pen.goto(screen_x, screen_y)
            pen.stamp()
draw_grid(pen, grid)

def valueGenerator():
    value = random.randint(1,2)
    return value * 2

text = turtle.Turtle()
text.speed(0)

def randomstart(pen,grid):

    rand1 = random.randint(0,3)
    rand2 = random.randint(0,3)
    screen_x = left + (rand1 *100)
    screen_y = top - (rand2*100)
    numbers[rand1][rand2] = valueGenerator()
    pen.color(colors[int(math.log(numbers[rand1][rand2],2))])
    grid[rand1][rand2] = int(math.log(numbers[rand1][rand2],2))
    pen.goto(screen_x, screen_y)
    pen.stamp()
    text.hideturtle()
    text.up()
    text.goto(screen_x, screen_y-15)
    text.down()
    text.write(numbers[rand1][rand2], move = False, align = "center", font = ("Arial", 20, "normal"))
    text.hideturtle()
    while True:
        rand3 = random.randint(0,3)
        rand4 = random.randint(0,3)
        if(rand3 != rand1 and rand4 !=rand2):
           break;
        

    screen_x = left + (rand3 *100)
    screen_y = top - (rand4*100)
    numbers[rand3][rand4] = valueGenerator()
    pen.color(colors[int(math.log(numbers[rand3][rand4],2))])
    grid[rand3][rand4] = int(math.log(numbers[rand3][rand4],2))
    pen.goto(screen_x, screen_y)
    pen.stamp()
    text.hideturtle()
    text.up()
    text.goto(screen_x, screen_y-15)
    text.down()
    text.write(numbers[rand3][rand4], move = False, align = "center", font = ("Arial", 20, "normal"))
    text.hideturtle()

randomstart(pen, grid)

def afterMove():
    top  = 200
    left  =-150
    found = False
    while not found:
        x = random.randint(0,3)
        y = random.randint(0,3)
        if(numbers[x][y] == 0):
            found = True
    
    numbers[x][y] = valueGenerator()

    grid[x][y] = int(math.log(numbers[x][y],2))
    screen_x = left + (x *100)
    screen_y = top - (y*100)
    pen.goto(screen_x, screen_y)
    pen.color(colors[grid[x][y]])
    pen.stamp()

    text.hideturtle()
    text.up()
    text.goto(screen_x, screen_y-15)
    text.down()
    text.write(numbers[x][y], move = False, align = "center", font = ("Arial", 20, "normal"))
    text.hideturtle()


def recolor():
    top  = 200
    left  =-150
    for x in range(3):
        for y in range(3):
            screen_x = left + (x *100)
            screen_y = top - (y*100)
            pen.goto(screen_x, screen_y)
            pen.color(colors[grid[x][y]])
            pen.stamp()
            text.hideturtle()
            text.up()
            text.goto(screen_x, screen_y-15)
            text.down()
            if (numbers[x][y] != 0):
                text.write(numbers[x][y], move = False, align = "center", font = ("Arial", 20, "normal"))
            text.hideturtle()

       
def down():
    top  = 200
    left  =-150
    for i in range(len(grid)): # columns
        for j in range(len(grid)-1): # rows
            if (numbers[i][j] == numbers[i][j+1] and numbers[i][j] != 0):
                grid[i][j+1] = int(math.log(numbers[i][j] * 2,2))

                numbers[i][j+1] = numbers[i][j] * 2
                grid[i][j] = 0
                numbers[i][j] = 0
                screen_x = left + (i *100)
                screen_y = top - (j*100)
                pen.goto(screen_x, screen_y)
                pen.color(colors[grid[i][j]])
                pen.stamp()
                text.hideturtle()
                text.up()
                text.goto(screen_x, screen_y-15)
                text.down()
                if (numbers[i][j] != 0):
                    text.write(numbers[i][j], move = False, align = "center", font = ("Arial", 20, "normal"))
                text.hideturtle()

                screen_x = left + (i *100)
                screen_y = top - ((j+1)*100)
                pen.goto(screen_x, screen_y)
                pen.color(colors[grid[i][j+1]])
                pen.stamp()
                text.hideturtle()
                text.up()
                text.goto(screen_x, screen_y-15)
                text.down()
                if (numbers[i][j+1] != 0):
                    text.write(numbers[i][j+1], move = False, align = "center", font = ("Arial", 20, "normal"))
                text.hideturtle()
                
            elif(numbers[i][j] != 0 and numbers[i][j+1] == 0):
                print("here")
                grid[i][j+1] = int(math.log(numbers[i][j],2))
                grid[i][j] = 0
                numbers[i][j+1] = numbers[i][j]
                numbers[i][j] = 0
                screen_x = left + (i *100)
                screen_y = top - (j*100)
                pen.goto(screen_x, screen_y)
                pen.color(colors[grid[i][j]])
                pen.stamp()
                text.hideturtle()
                text.up()
                text.goto(screen_x, screen_y-15)
                text.down()
                if (numbers[i][j] != 0):
                    text.write(numbers[i][j], move = False, align = "center", font = ("Arial", 20, "normal"))
                text.hideturtle()

                screen_x = left + (i *100)
                screen_y = top - ((j+1)*100)
                pen.goto(screen_x, screen_y)
                pen.color(colors[grid[i][j+1]])
                pen.stamp()
                text.hideturtle()
                text.up()
                text.goto(screen_x, screen_y-15)
                text.down()
                if (numbers[i][j+1] != 0):
                    text.write(numbers[i][j+1], move = False, align = "center", font = ("Arial", 20, "normal"))
                text.hideturtle()
            

            j += 1  
        i += 1
    afterMove()

def up():
    top  = 200
    left  =-150
    for i in range(len(grid)): # columns
        j= 3
        for x in range(3): # rows
            
            if (numbers[i][j] == numbers[i][j-1] and numbers[i][j] != 0):
                grid[i][j-1] = int(math.log(numbers[i][j] * 2,2))
                numbers[i][j-1] = numbers[i][j] * 2
                grid[i][j] = 0
                numbers[i][j] = 0
                screen_x = left + (i *100)
                screen_y = top - (j*100)
                pen.goto(screen_x, screen_y)
                pen.color(colors[grid[i][j]])
                pen.stamp()
                text.hideturtle()
                text.up()
                text.goto(screen_x, screen_y-15)
                text.down()
                if (numbers[i][j] != 0):
                    text.write(numbers[i][j], move = False, align = "center", font = ("Arial", 20, "normal"))
                text.hideturtle()

                screen_x = left + (i *100)
                screen_y = top - ((j-1)*100)
                pen.goto(screen_x, screen_y)
                pen.color(colors[grid[i][j-1]])
                pen.stamp()
                text.hideturtle()
                text.up()
                text.goto(screen_x, screen_y-15)
                text.down()
                if (numbers[i][j-1] != 0):
                    text.write(numbers[i][j-1], move = False, align = "center", font = ("Arial", 20, "normal"))
                text.hideturtle()
                
            elif(numbers[i][j] != 0 and numbers[i][j-1] == 0):
                print("here")
                grid[i][j-1] = int(math.log(numbers[i][j],2))
                grid[i][j] = 0
                numbers[i][j-1] = numbers[i][j]
                numbers[i][j] = 0
                screen_x = left + (i *100)
                screen_y = top - (j*100)
                pen.goto(screen_x, screen_y)
                pen.color(colors[grid[i][j]])
                pen.stamp()
                text.hideturtle()
                text.up()
                text.goto(screen_x, screen_y-15)
                text.down()
                if (numbers[i][j] != 0):
                    text.write(numbers[i][j], move = False, align = "center", font = ("Arial", 20, "normal"))
                text.hideturtle()

                screen_x = left + (i *100)
                screen_y = top - ((j-1)*100)
                pen.goto(screen_x, screen_y)
                pen.color(colors[grid[i][j-1]])
                pen.stamp()
                text.hideturtle()
                text.up()
                text.goto(screen_x, screen_y-15)
                text.down()
                if (numbers[i][j-1] != 0):
                    text.write(numbers[i][j-1], move = False, align = "center", font = ("Arial", 20, "normal"))
                text.hideturtle()
            

            j -= 1
        i += 1
    afterMove()

def left():
    top  = 200
    left  =-150
    i = 3
    for y in range(3): # columns
        for j in range(len(grid)): # rows
            if (numbers[i][j] == numbers[i-1][j] and numbers[i][j] != 0):
                grid[i-1][j] = int(math.log(numbers[i][j] * 2,2))
                numbers[i-1][j] = numbers[i][j] * 2
                grid[i][j] = 0
                numbers[i][j] = 0
                screen_x = left + (i *100)
                screen_y = top - (j*100)
                pen.goto(screen_x, screen_y)
                pen.color(colors[grid[i][j]])
                pen.stamp()
                text.hideturtle()
                text.up()
                text.goto(screen_x, screen_y-15)
                text.down()
                if (numbers[i][j] != 0):
                    text.write(numbers[i][j], move = False, align = "center", font = ("Arial", 20, "normal"))
                text.hideturtle()

                screen_x = left + ((i-1) *100)
                screen_y = top - ((j)*100)
                pen.goto(screen_x, screen_y)
                pen.color(colors[grid[i-1][j]])
                pen.stamp()
                text.hideturtle()
                text.up()
                text.goto(screen_x, screen_y-15)
                text.down()
                if (numbers[i-1][j] != 0):
                    text.write(numbers[i-1][j], move = False, align = "center", font = ("Arial", 20, "normal"))
                text.hideturtle()
                
            elif(numbers[i][j] != 0 and numbers[i-1][j] == 0):
                print("here")
                grid[i-1][j] = int(math.log(numbers[i][j],2))
                grid[i][j] = 0
                numbers[i-1][j] = numbers[i][j]
                numbers[i][j] = 0
                screen_x = left + (i *100)
                screen_y = top - (j*100)
                pen.goto(screen_x, screen_y)
                pen.color(colors[grid[i][j]])
                pen.stamp()
                text.hideturtle()
                text.up()
                text.goto(screen_x, screen_y-15)
                text.down()
                if (numbers[i][j] != 0):
                    text.write(numbers[i][j], move = False, align = "center", font = ("Arial", 20, "normal"))
                text.hideturtle()

                screen_x = left + ((i-1) *100)
                screen_y = top - ((j)*100)
                pen.goto(screen_x, screen_y)
                pen.color(colors[grid[i-1][j]])
                pen.stamp()
                text.hideturtle()
                text.up()
                text.goto(screen_x, screen_y-15)
                text.down()
                if (numbers[i-1][j] != 0):
                    text.write(numbers[i-1][j], move = False, align = "center", font = ("Arial", 20, "normal"))
                text.hideturtle()
            
            j += 1  
        i -= 1
    afterMove()

def right():
    top  = 200
    left  =-150
    for i in range(len(grid)-1): # columns
        for j in range(len(grid)): # rows
            if (numbers[i][j] == numbers[i+1][j] and numbers[i][j] != 0):
                grid[i+1][j] = int(math.log(numbers[i][j] * 2,2))
                numbers[i+1][j] = numbers[i][j] * 2
                grid[i][j] = 0
                numbers[i][j] = 0
                screen_x = left + (i *100)
                screen_y = top - (j*100)
                pen.goto(screen_x, screen_y)
                pen.color(colors[grid[i][j]])
                pen.stamp()
                text.hideturtle()
                text.up()
                text.goto(screen_x, screen_y-15)
                text.down()
                if (numbers[i][j] != 0):
                    text.write(numbers[i][j], move = False, align = "center", font = ("Arial", 20, "normal"))
                text.hideturtle()

                screen_x = left + ((i+1) *100)
                screen_y = top - ((j)*100)
                pen.goto(screen_x, screen_y)
                pen.color(colors[grid[i+1][j]])
                pen.stamp()
                text.hideturtle()
                text.up()
                text.goto(screen_x, screen_y-15)
                text.down()
                if (numbers[i+1][j] != 0):
                    text.write(numbers[i+1][j], move = False, align = "center", font = ("Arial", 20, "normal"))
                text.hideturtle()
                
            elif(numbers[i][j] != 0 and numbers[i+1][j] == 0):
                print("here")
                grid[i+1][j] = int(math.log(numbers[i][j],2))
                grid[i][j] = 0
                numbers[i+1][j] = numbers[i][j]
                numbers[i][j] = 0
                screen_x = left + (i *100)
                screen_y = top - (j*100)
                pen.goto(screen_x, screen_y)
                pen.color(colors[grid[i][j]])
                pen.stamp()
                text.hideturtle()
                text.up()
                text.goto(screen_x, screen_y-15)
                text.down()
                if (numbers[i][j] != 0):
                    text.write(numbers[i][j], move = False, align = "center", font = ("Arial", 20, "normal"))
                text.hideturtle()

                screen_x = left + ((i+1) *100)
                screen_y = top - ((j)*100)
                pen.goto(screen_x, screen_y)
                pen.color(colors[grid[i+1][j]])
                pen.stamp()
                text.hideturtle()
                text.up()
                text.goto(screen_x, screen_y-15)
                text.down()
                if (numbers[i+1][j] != 0):
                    text.write(numbers[i+1][j], move = False, align = "center", font = ("Arial", 20, "normal"))
                text.hideturtle()
            

            j += 1  
        i += 1
    
    afterMove()
turtle.listen()
turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(right, "Right")
turtle.onkey(left, "Left")


    

wn.mainloop()

