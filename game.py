import pygame

from pygame.locals import *
from random import randint
from sense_hat import SenseHat

pygame.init()
pygame.display.set_mode((640, 480))

sense = SenseHat()
sense.clear()

running = True

score = 0

# x and y position of player
pY = 0
pX = 0

enemies = []

class Enemy(object):
    def __init__(self, x, y):
            self.x = x
            self.y = y

# Create the enemies, with x the number of enemies
def setupEnemies(x):
    global enemies

    i = 0
    
    while i < x :
        enemies.append(Enemy(6,6))
        i = i + 1

# Update the player position
def updatePlayer():
    sense.clear()
    sense.set_pixel(pX, pY, [0, 0, 255])
    #print("PLAYER:  x = " + str(pX) + " y = " + str(pY))

# Update the enemy positions
def updateEnemy():

    global enemies

    for enemy in enemies :

        moved = False

        while moved == False :
            
            rand = randint(0,3)

            if rand == 0 and enemy.y < 7:
                enemy.y = enemy.y + 1
                moved = True
            
            if rand == 1 and enemy.y > 0:
                enemy.y = enemy.y - 1
                moved = True

            if rand == 2 and enemy.x > 0:
                enemy.x = enemy.x - 1
                moved = True

            if rand == 3 and enemy.x < 7:
                enemy.x = enemy.x + 1
                moved = True

        sense.set_pixel(enemy.x, enemy.y, [255, 0, 0])
        #print("ENEMY:  x = " + str(enemy.x) + " y = " + str(enemy.y))

# Check if the player has collided with an enemy
def checkClash():
    global score
    global enemies

    for enemy in enemies :

        if enemy.x == pX and enemy.y == pY :
            endGame()
            return
    
    score = score + 1
    #print("Score = " + str(score))

# End the game and report score
def endGame():
    running = False
    sense.clear()
    msg = "You lose!"
    scoreMsg = "Final score: " + str(score)
    sense.show_message(msg, scroll_speed=0.07 ,text_colour=[0,255,0])
    sense.show_message(scoreMsg, scroll_speed=0.07, text_colour=[0,255,0])
    
    
    

# The game is initialised
setupEnemies(14)
updatePlayer()
updateEnemy()

# The game starts
while True:
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                
                if event.key == K_DOWN and pY < 7:
                    pY = pY + 1

                if event.key == K_UP and pY > 0:
                    pY = pY - 1

                if event.key == K_LEFT and pX > 0:
                    pX = pX - 1

                if event.key == K_RIGHT and pX < 7:
                    pX = pX + 1

                updatePlayer()
                updateEnemy()
                checkClash()
                
    # Game has ended, reset the game
    score = 0


            
                


            
