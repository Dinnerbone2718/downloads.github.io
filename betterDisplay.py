import pygame
import random
import os
import time
import randfacts

width=800
height=480

pygame.init()
pygame.mouse.set_visible(False)

screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()



def draw_text(text, text_col, size, x, y):
    font = pygame.font.SysFont("arialblack",size)
    words = [word.split(' ') for word in text.splitlines()] 
    space = ("")
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, text_col)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= 800:
                x = 0
                y += 50
            screen.blit(word_surface, (x,y))
            x += word_width + 20
        x = 0  
        y += 30 

nextFact = 0
randFact = randfacts.get_fact()
color = (random.randrange(100,255),random.randrange(100,255),random.randrange(100,255))
run = True
while run:
    nextFact+=1
    screen.fill(color)
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pass    
    draw_text(f"{time.ctime()}", (0,0,0), 50, 0,400)
    draw_text(randFact, (0,0,0), 50, 0 ,50)
    if nextFact > 100:
        randFact = randfacts.get_fact()
        nextFact = 0
        color = (random.randrange(100,255),random.randrange(100,255),random.randrange(100,255))

    #Final Lines Needed
    pygame.display.flip()
pygame.quit()