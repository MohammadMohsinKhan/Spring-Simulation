# Import and initialize the pygame library
import random
import pygame
from pygame.locals import *
from scipy.integrate import odeint
from matplotlib import pyplot
import numpy
import time

#important variables for simulation
mass = 0
while mass <=0:
    mass = int(input('Mass of the weight in kg: '))
    if mass <=0:
        print('mass cannot be less than or equal to 0')

spring_f = -1*int(input('spring force coefficient: '))
visc_f = -1*int(input('viscous force coefficient: '))
initial_pos = int(input('initial position in metres: '))
initial_v = int(input('initial velocity in metres/second: '))
ind = 0

def yd_prime(u,x):
    return (u[1],(visc_f/mass)*u[1]+(spring_f/mass)*u[0])
inc = 2000
t = 10
y0 = [initial_pos, initial_pos]
xs = numpy.linspace(1,t,inc)
us = odeint(yd_prime,y0,xs)
ys = us[:,0]

pygame.init()
pygame.display.set_caption("Spring Simulation")

#variables for timer
current_time = 0
button_press_time = 0
timer = "start"
clock = pygame.time.Clock()
button_press_time = pygame.time.get_ticks()

# RGB value for colours.
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Set up the drawing window
w = 1280
h = 720
screen = pygame.display.set_mode([w, h])

# what state is the program in
game_state = "menu"
running = True

#function for displaying text
def display_text(string, colour, x, y):
    # create a font object.
    font = pygame.font.Font('freesansbold.ttf', 32)
 
    # create a text suface object, on which text is drawn on it.
    text = font.render(string, True, colour, white)

    # copying the text surface object to the display surface object at the center coordinate.
    textRect = text.get_rect()
    
    # set the center of the rectangular object.
    textRect.center = (x, y)

    screen.blit(text, textRect)

def menu():
    global game_state, button_press_time
    screen.fill(white)
    key = pygame.key.get_pressed()
    if key[pygame.K_r]:
        game_state = "game"
        button_press_time = pygame.time.get_ticks()
#function for the simulation
def game():
    global ys, running,ind
    timer = pygame.time.get_ticks()
    screen.fill(white)
    pygame.draw.rect(screen,(black),(w//2,h//2 + int(ys[ind]*50),10,10))
    pygame.draw.rect(screen, (black), (w//2 - 20, h//5, 50, 10 ))
    pygame.draw.rect(screen, (blue), (w//2 + 2 , h//5 + 10, 5, (h//2 + int(ys[ind]*50)) -  (h//5 + 10)))
    
    if ind >=len(ys) - 1:
        print(timer - button_press_time)
        pyplot.plot(xs,ys,'-')
        pyplot.show()
        running = False
    else:
        ind += 1


#function for what to display during the results screen



while running:
    events = pygame.event.get()
    clock.tick(200)
    if game_state == "game":
        game()
    elif game_state == 'menu':
        menu()
    
    pygame.display.flip()


pygame.quit()


