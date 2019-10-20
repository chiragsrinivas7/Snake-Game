import pygame
import sys
import random
from pygame.locals import *
from time import sleep
from tkinter import messagebox
from tkinter import Tk

last_key=None

board_width = 580
board_height = 380
block_size=20
RED=(255,0,0)
BLACK=(0,0,0)
WHITE=(255,255,255)
score=0
root=Tk()


def game_over(snake_list):
    for i in snake_list:
        for j in snake_list:
            if i!=j and i.x==j.x and i.y==j.y and (snake_list.index(i)-snake_list.index(j))>1:
                
                root.withdraw()
                messagebox.showinfo("Game Over","Score:{}".format(score))
                pygame.quit()
                sys.exit()
                

def generate_food():
    x = random.randrange(0, board_width + block_size, block_size)
    y = random.randrange(0, board_height + block_size, block_size)
    block = pygame.Rect(x,y,block_size,block_size)
    pygame.draw.rect(surface,WHITE,block)
    return x,y

class snake:
    def __init__(self, x = 0 , y = 0):
        self.x=x
        self.y=y
        
    def draw_block(self):
        block = pygame.Rect(self.x, self.y, block_size, block_size)
        pygame.draw.rect(surface, BLACK, block)

    def erase_block(self):
        block = pygame.Rect(self.x, self.y, block_size, block_size)
        pygame.draw.rect(surface, RED, block)

    def move_head(self, key):        
        global a,b,score        
        if self.x==a and self.y==b:
            a,b=generate_food()                
            snake_list.append(snake(snake_list[-1].x, snake_list[-1].y))
            score+=1
                                    
        if key==K_RIGHT:                                    
            if self.x==board_width:                
                self.x=0                                                                                                        
            else:                            
                self.x=self.x + block_size
                                                                
        if key==K_LEFT:                                                        
            if self.x==0:                
                self.x = board_width                                            
            else:                    
                self.x = self.x - block_size
                
        if key==K_UP:                                                                                                                                                                                                     
            if self.y==0:                
                self.y = board_height                                            
            else:                
                self.y = self.y - block_size
                                    
        if key==K_DOWN:                                    
            if self.y==board_height:            
                self.y=0                                            
            else:                
                self.y=self.y + block_size
                
            
pygame.init()
surface = pygame.display.set_mode((board_width + block_size, board_height + block_size))
pygame.display.set_caption('Snake Game')

def draw_grid():
    for y in range(board_height + block_size):
        for x in range(board_width + block_size):
            rect = pygame.Rect(x*(block_size), y*(block_size), block_size, block_size)
            pygame.draw.rect(surface,RED,rect)

draw_grid()

snake_list=[]

def init_snake():
    x = random.randrange(0, board_width + block_size, block_size)
    y = random.randrange(0, board_height + block_size, block_size)    
    head = snake(x, y)
    snake_list.append(head)
init_snake()

head = snake_list[0]

a,b=generate_food()
                    
last_key=None

while True:
    sleep(0.2)
    pygame.display.update()
    
    for event in pygame.event.get():        
        if event.type==KEYDOWN:
            last_key=event.key

        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    for i in range(len(snake_list)-1, -1, -1):
        snake_list[i].erase_block()
        if i > 0:
            snake_list[i].x, snake_list[i].y = snake_list[i-1].x, snake_list[i-1].y        

    head.move_head(last_key)

    for i in range(len(snake_list)):
        snake_list[i].draw_block()
        game_over(snake_list)