from graphics import Canvas

import sys
import os
sys.path.append(os.path.dirname(__file__))

import graphics 


import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1 

def main():

    #1: Set up the World
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    player = canvas.create_rectangle(0, 0, 0+SIZE, 0+SIZE,fill = 'blue')
    goal = canvas.create_rectangle(350, 350, 350+SIZE, 350+SIZE,fill = 'salmon')
    
    # 2: Animation loop
    dx = 20
    dy = 0
    while True:
        # TODO: update the world
        canvas.move(player, dx, dy)

        # sleep
        time.sleep(DELAY)
        #3: Handle Key Press
        keys = canvas.get_new_key_presses()
        if keys:
            key = keys[0].keysym
            print("你按下了：", key)
            if key == 'ArrowLeft':
                direction = 'left'
            elif key == 'ArrowRight':
                direction = 'right'
            elif key == 'ArrowUp':
                direction = 'up'
            elif key == 'ArrowDown':
                direction = 'down'
        #4: Detecting collisions
        if is_out_of_bounds(canvas, player, 400, 400):
            print("Game Over!")
            break  # 或 return，讓主程式結束


        #5: Moving the goal 
        moving_the_goal(canvas, player, goal)

def is_out_of_bounds(canvas,player,canvas_width, canvas_height):

        x = canvas.get_left_x(player)
        y = canvas.get_top_y(player)

        if x<0 or x+20>CANVAS_WIDTH:
            print("Game Over!")
        elif y<0 or y+20>CANVAS_HEIGHT:
            print("Game Over!")  

        return False   
        
def moving_the_goal(canvas,player,goal):
    # 每一輪都檢查碰撞
    px = canvas.get_left_x(player)
    py = canvas.get_top_y(player)

    gx = canvas.get_left_x(goal)
    gy = canvas.get_top_y(goal)

    if px == gx and py == gy:
        # 碰到了！隨機換一個位置
        new_x = random.randint(0, 19) * 20
        new_y = random.randint(0, 19) * 20
        canvas.moveto(goal, new_x, new_y)

if __name__ == '__main__':
    main()


