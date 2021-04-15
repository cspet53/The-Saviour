import pygame
from pygame.event import *
import sys
import random
import math

pygame.init()


# Game Display
screen = pygame.display.set_mode((1300, 700))
icon = pygame.image.load("F:\programming\PYTHON\GAMES\The Saviour\Icon.png")
pygame.display.set_caption("The Saviour")
pygame.display.set_icon(icon)

# Score
global score
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textx = 380
texty = 10


# misses
global misses
misses = 0
font = pygame.font.Font("freesansbold.ttf", 32)
missx = 380 * 2
missy = 10

# fonts win and lose
win_font = pygame.font.Font("freesansbold.ttf", 50)
lose_font = pygame.font.Font("freesansbold.ttf", 50)

# Pong
meteor = pygame.image.load("F:\programming\PYTHON\GAMES\The Saviour\Meteor.png")
meteorX = random.randint(1, 1200)
meteorY = random.randint(1, 200)
num_of_meteors = random.randint(10, 20)


# Paddle
paddle = pygame.image.load("F:\programming\PYTHON\GAMES\The Saviour\SpaceShip.png")
paddleX = 0
paddleY = 551

# backdrops
backdrop_col = pygame.image.load("GAMES\The Saviour\BackG.png")
india = pygame.image.load("GAMES\The Saviour\Flag.png")
celbg = pygame.image.load("F:\programming\PYTHON\GAMES\The Saviour\Celebration BG.png")


def isCollision(meteorX, paddleX, meteorY, paddleY):
    distance = math.sqrt(
        (math.pow(paddleX - meteorX, 2)) + (math.pow(meteorY - paddleY, 2))
    )
    if distance < 27:
        return True
    else:
        return False


def score_text(x, y):
    score_text = font.render(f"Score: " + str(score), True, (255, 255, 0))
    screen.blit(score_text, (x, y))


def miss_text(x, y):
    miss_text = font.render(f"Misses: " + str(misses), True, (255, 255, 0))
    screen.blit(miss_text, (x, y))


def win_txt(x, y):
    win = win_font.render(f"You are 'THE SAVIOUR'!!!", True, (0, 0, 255))
    screen.blit(win, (x, y))


def lost(x, y):
    lose = lose_font.render(f"Mission Unsuccessfull!!!", True, (255, 0, 0))
    screen.blit(lose, (x, y))


running = True
while running:
    screen.blit(backdrop_col, (0, 0))
    screen.blit(meteor, (meteorX, meteorY))
    screen.blit(paddle, (paddleX, paddleY))
    score_text(textx, texty)
    miss_text(missx, missy)

    meteorX += 8
    meteorY += 8

    collison = isCollision(meteorX, paddleX, meteorY, paddleY)

    if collison:
        if meteorY >= 551 and meteorY <= 560:
            score += 4
    else:
        if meteorY >= 551 and meteorY <= 560:
            misses += 1

    if meteorX > 1290 or meteorX < 1:
        meteorX = random.randint(1, 500)
        meteorY = random.randint(30, 200)

    if paddleX <= 0:
        paddleX = 0
    if paddleX >= 953:
        paddleX = 953

    if score >= 100:
        screen.blit(celbg, (0, 0))
        screen.blit(india, (315, 340))
        win_txt(450, 350)
    if misses >= 30:
        screen.fill("black")
        lost(355, 350)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddleX -= 100
            if event.key == pygame.K_RIGHT:
                paddleX += 100

    pygame.display.update()
