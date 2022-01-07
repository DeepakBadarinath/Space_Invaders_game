# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 15:19:09 2020

@author: deepa
"""
import pygame
import numpy as np

# Initialize the game
pygame.init()

#Set display
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('EDA_mindmap_small.png')
pygame.display.set_icon(icon)


#Player 
playerImg=pygame.image.load('cat.jpg')
playerX=380
playerY=320


#Player 2
player2Img=pygame.image.load('dog.jpg')
player2X=380
player2Y=100

#Background
backgroundImg=pygame.image.load('lawn.jpg')
backgroundX=0
backgroundY=0

ballImg=pygame.image.load('ball.png')

def player(x,y):
    screen.blit(playerImg,(x,y))

def player2(x,y):
    screen.blit(player2Img,(x,y))
    
def show_background():
    screen.blit(backgroundImg,(backgroundX,backgroundY))
    
def ballprinter(balls):
    if balls == []:
        return
    for ball in balls:
        screen.blit(ballImg,(ball[0],ball[1]))
        
def ballremover(balls):
    if balls == []:
        return
    for ball in balls:
        if ball[1]<0:
            balls.remove(ball)
            
def ballspeeder(balls,ball_speed):
    if balls == []:
        return
    for ball in balls:
        ball[1]=ball[1]-ball_speed

def show_balls_fired(balls_fired):
    total=font.render("Total balls fired: " + str(balls_fired),True,(200,0,250))
    screen.blit(total,(10,10))

#Game over
def print_game_over():
    total=font2.render("GAME OVER ",True,(250,0,0))
    screen.blit(total,(300,200))

def game_over(balls_positions,player2X,player2Y):
    for ball in balls_positions:
        if(abs(ball[0]-player2X)<10 and abs(ball[1]-player2Y)<10):
            print("GAME OVER!")
            return True
    return False


#create the screen
screen = pygame.display.set_mode((800,500))

#initialize values
player_speed=0.8
time=0
running = True
ball_positions=[]
ball_speed=1
balls_fired=0
#game_over=False

font=pygame.font.Font('freesansbold.ttf',21)
font2=pygame.font.Font('freesansbold.ttf',40)

while running:
    #RGB values
    pygame.time.delay(1)
    screen.fill((0,251,0))
    show_background()
    
    #Boundary and velocity
    playerX=playerX+player_speed
    ballspeeder(ball_positions,ball_speed)
    
    #Boundary Conditions
    if playerX>780 or playerX<0:
        player_speed=-player_speed
    ballremover(ball_positions)
    
    #Input Detection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
        #If keyrstroke is left pressed or right pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                clock_start=time
                print("Clock Started at ",clock_start)
                print("Speed now is ", player_speed)
            elif event.key == pygame.K_SPACE:
                ballX=playerX
                ballY=playerY
                balls_fired=balls_fired+1
                ball_positions.append([ballX,ballY])
                #print("Ball posn is ",ball_positions)

        #Acceleration        
        if event.type == pygame.KEYUP:
            clock_end=time
            #print("Key release noted at time",clock_end)
            if event.key == pygame.K_LEFT:
                player_speed = player_speed - 0.005*(clock_end-clock_start)
                #print("Boost in speed", 0.005*(clock_end-clock_start))
                #print("Speed now is ", player_speed)
            elif event.key == pygame.K_RIGHT:
                player_speed = player_speed + 0.005*(clock_end-clock_start)
                #print("Boost in speed", 0.005*(clock_end-clock_start))
                #print("Speed now is ", player_speed)
    
    #Print on screen
    if game_over(ball_positions,player2X,player2Y)==False:
        show_balls_fired(balls_fired)
        ballprinter(ball_positions)
        player2(player2X,player2Y) 
        player(playerX,playerY)
        time=time+1
    else:
       i=0
       while i in range(1000):
           print_game_over()
           pygame.display.update()
       
       running=False    
    pygame.display.update() 
pygame.quit()







''' Debug - 1) Center the bullet space on the dog
    2) RL algos gotta be implemented
    3) Make dog "smart"'''
    
    
    







