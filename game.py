import random
from pynput import keyboard
import tkinter
r=tkinter.Tk()
SCREEN_WIDTH=640
SCREEN_HEIGHT=480
canvas=tkinter.Canvas(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
r.geometry(str(SCREEN_WIDTH)+ "x"+str(SCREEN_HEIGHT+50))
l=[(10,11),(11,12),(12,13),(13,14),(14,15)]                 #list containing some parts of snake as tuple

direction="right"
next_direction=direction
ball_x=15                                #coodinates of ball x & y
ball_y=20
game_over=False
speed=100                                #speed of snake 
snake_size=20                            #size of snake
score=0
back = tkinter.Frame(master=r)
back.pack()
text = tkinter.Label(back,text="CLICK ON START BUTTON")
text.pack(side="left")
go = tkinter.Button(master=back, text='Start Game',command=lambda:start_game())      #for creating a button on screen
go.pack(side="left")                                                                 
go = tkinter.Button(master=back, text='End Game',command=lambda:exit_game())
go.pack(side="left")
game_over_text =tkinter.Label(r)  
game_over_text.pack(side="bottom") 
def create_square(a,b):
                                        #creating body of snake
    canvas.create_rectangle(a*snake_size+1,b*snake_size+1,a*snake_size+snake_size-1,b*snake_size+snake_size-1,fill='yellow',outline="")

def draw_ball(a,b,colour):
                                        #creating structure of ball 
    canvas.create_oval(a*snake_size+3,b*snake_size+3,a*snake_size+snake_size-3,b*snake_size+snake_size-3,fill=colour,outline="")
    


def start_game():                       #to start the game 
    global score
    score=0
    text.config(text="score:"+str(score))
    game_over_text.config(text="")
    global game_over
    game_over=False
    global l
    l=[(10,11),(11,12),(12,13),(13,14),(14,15)]
    global direction
    direction="right"
    random_ball()

def move_snake():                                           #for motion of snake
    global score
    if game_over:
        return
    global direction
    direction = next_direction
    horc=SCREEN_WIDTH//snake_size
    verc=SCREEN_HEIGHT//snake_size
    head=l[-1]
    head_x,head_y=head
    if direction=="right":
        new_head_x=(head_x+1)% horc                             #to move towards right (in x-axis)
        new_head_y=head_y                                       #keeping y-axis as fixed
    if direction=="up":
        new_head_x=head_x                                       #keeping x-axis as fixed                   
        new_head_y=(head_y-1+verc)% verc                        #to move towards up (in y-axis)
    if direction=="down":
        new_head_x=head_x
        new_head_y=(head_y+1)% verc
    if direction=="left":
        new_head_x=(head_x-1+horc)% horc
        new_head_y=head_y
    if new_head_x==ball_x and new_head_y==ball_y:
        score+=10
        text.config(text="Score:"+str(score))
        random_ball()
   
    else:
        l.pop(0)
    l.append((new_head_x,new_head_y))

def change_direction(key):                                      #keyboard control by using up, down,right & left arrow key
    global next_direction
    if keyboard.Key.up==key and direction!="down":
        next_direction="up"
    if keyboard.Key.left==key and direction!="right":
        next_direction="left"
    if keyboard.Key.down==key and direction!="up" :
        next_direction="down"
    if keyboard.Key.right==key and direction!="left":
        next_direction="right"
listener = keyboard.Listener(on_press=change_direction)
listener.start()           

def check_dead():
    global game_over
    if not game_over:
        if len(set(l))!=len(l):
            game_over=True
            exit_game()
def draw_screen():
    canvas.delete("all")
    move_snake()
    #DRAWING SNAKE          
    for i in l:
        create_square(i[0],i[1])
    head=l[-1]
    draw_ball(head[0],head[1],"black")
    draw_ball(ball_x,ball_y,"red")
    check_dead()
    r.after(speed,draw_screen)

def random_ball():                          #for generating the random position of ball by using random() 
    global ball_x
    global ball_y
    horc=SCREEN_WIDTH//snake_size
    verc=SCREEN_HEIGHT//snake_size
    ball_x=int(random.random()*horc)
    ball_y=int(random.random()*verc)

def exit_game():                        #to exit the game 
    global game_over
    game_over_text.config(text="GAME OVER -_-")
    game_over=True


    
start_game()
game_over=True
canvas['bg']='green'
canvas.pack()
r.after(speed,draw_screen)
r.mainloop()

