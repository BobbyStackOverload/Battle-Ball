import pygame

# Random is used to generate random numbers
import random

# Sys is needed to close the game properly
import sys

# Width of screen
x = 500
# Height of screen
y = 500
bat_width = 100
bat_height = 15
bat_x = 200
bat_y = 450
# Ball coordinate
ballx = int(x/2)
# This is used to center the ball when the game starts.
bally = int(y/2)
# Ball radius
ballrad = 15
speed = 0
ballxspeed = 1
ballyspeed = -2
# Player will have 3 lives.
lives = 3
# When working with pygame you have to initialize it first.
pygame.init()
# Set screen for game
screen = pygame.display.set_mode([x, y])
# Background screen color for game. All python game colors are in rgb. The screen color is black.
screen.fill((0, 0, 0))
# Draw ball for the first time. Ball will be yellow.
# 0 after ballrad means the ball will be filled.
pygame.draw.circle(screen, (255, 255, 0), (ballx, bally), ballrad, 0)
# Bat on game. The color is light red.
pygame.draw.rect(screen, (255, 40, 0),
                 (bat_x, bat_y, bat_width, bat_height), 0)
# In pygame everytime we draw something we have to flip the display it to see it.
pygame.display.flip()


def batblock():
    global speed
    if bat_x <= 0 or bat_x >= x-bat_width:
        speed = 0
# This is how the ball gets moved.


def ballmovement():
    global ballx, bally
    ballx += ballxspeed
    bally += ballyspeed
# The will reset everthing if the player has lost 1 time.


def reset():
    global ballyspeed, ballxspeed, ballx, bally, bat_x, bat_y, speed
    bat_x = 200
    bat_y = 450
    ballx = int(x/2)
    bally = int(y/2)
    speed = 0
    # Random.randint(-2,2) means a random number between -2 and 2.
    ballxspeed = random.randint(-2, 2)
    if ballxspeed == 0:
        # We want to set it at ballxspeed at 1 to keep the game going.
        ballxspeed = 1
    ballyspeed = random.randint(-2, 2)
    if ballyspeed == 0:
        # We want to set it at ballyspeed at 2 to keep the game going.
        ballyspeed = 2
    screen.fill((0, 0, 0))
    # 0 after ballrad means the ball will be filled.
    pygame.draw.circle(screen, (255, 255, 0), (ballx, bally), ballrad, 0)
    # Bat on game. The color is light red.
    pygame.draw.rect(screen, (255, 40, 0),
                     (bat_x, bat_y, bat_width, bat_height), 0)
    # In pygame everytime we draw something we have to flip the display it to see it.
    pygame.display.flip()
    # The game will pause for 1 second before the play have the ability to play again
    pygame.time.wait(1000)


def ballblock():
    global ballyspeed, ballxspeed, lives
    if bally-ballrad <= 0:
        ballyspeed *= -1
    if ballx-ballrad <= 0:
        ballxspeed *= -1
    if ballx+ballrad >= x:
        ballxspeed *= -1

    # If the ball hits the bottom.
    if bally >= 435 and bally <= 440:
        if ballx >= bat_x-15 and ballx <= bat_x+bat_width+15:
            ballyspeed *= -1
        else:
            lives -= 1
            reset()


def batmove():
    global bat_x
    bat_x += speed


while lives > 0:
    for event in pygame.event.get():
        # If the player click the cross in the right corner the game will be closed correctly.
        if event.type == pygame.QUIT:
            sys.exit()
        # Checking to see which key is pressed on the key board.
        if event.type == pygame.KEYDOWN:
            # Left key arrow
            if event.key == pygame.K_LEFT:
                speed = -2
            # Right key arrow
            if event.key == pygame.K_RIGHT:
                speed = 2

    screen.fill((0, 0, 0))
    batmove()
    batblock()
    pygame.draw.rect(screen, (255, 40, 0),
                     (bat_x, bat_y, bat_width, bat_height), 0)
    ballmovement()
    ballblock()
    pygame.draw.circle(screen, (255, 255, 0), (ballx, bally), ballrad, 0)
    pygame.display.flip()
    pygame.time.wait(5)

print("You have lost!")
