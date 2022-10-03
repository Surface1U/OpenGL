import pygame
import time
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def draw():
    glColor3f(1,0,0)
    glBegin(GL_QUADS)
    glVertex2f(-3, -2)
    glVertex2f(3, -2)
    glVertex2f(3, 2)
    glVertex2f(-3,2)

    glColor3f(1, 1, 1)
    glVertex2f(-1.5, -2)
    glVertex2f(-1, -2)
    glVertex2f(-1, 2)
    glVertex2f(-1.5, 2)

    glVertex2f(-3, -0.2)
    glVertex2f(3, -0.2)
    glVertex2f(3, 0.2)
    glVertex2f(-3, 0.2)

    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(-1.1, -2)
    glVertex2f(-1.4, -2)
    glVertex2f(-1.4, 2)
    glVertex2f(-1.1, 2)

    glVertex2f(-3, -0.1)
    glVertex2f(3, -0.1)
    glVertex2f(3, 0.1)
    glVertex2f(-3, 0.1)

    glEnd()


def draw1():
    glColor3f(1,1,0)
    glBegin(GL_POLYGON)
    glVertex2f(-3, -2)
    glVertex2f(3, -2)

    glVertex2f(3, 2)
    glVertex2f(-3,2)
    glColor3f(1, 0, 1)


    glEnd()

def main():
    pygame.init()
    display = 500,500
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL|RESIZABLE)

    gluPerspective(80,display[0]/display[1],1,10)
    glTranslate(0.0,0.0,-5)

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        draw()
        pygame.display.flip()
main()
