import pygame as pg
import pygame.key
import time
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import math


def draw():
    glColor3f(0, 0.2, 0)
    glBegin(GL_QUADS)
    glVertex2f(-3, -0.5)
    glVertex2f(2, -0.5)
    glVertex2f(2, 2)
    glVertex2f(-3, 2)

    glEnd()


    glColor3f(1, 1, 0)
    glBegin(GL_QUADS)
    glVertex2f(-3, 0.5)
    glVertex2f(2, 0.5)
    glVertex2f(2, 0)
    glVertex2f(-3, 0)
    glEnd()


    glColor3f(1, 1,0)
    glBegin(GL_QUADS)
    glVertex2f(-3, 1.5)
    glVertex2f(2, 1.5)
    glVertex2f(2, 1)
    glVertex2f(-3, 1)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glVertex2f(-3, 0.5)
    glVertex2f(-1.5, 0.5)
    glVertex2f(-1.5, 2)
    glVertex2f(-3, 2)
    glEnd()




    # Звезда

    glBegin(GL_TRIANGLES)
    glColor3f(1, 1, 1)
    glVertex2f(-2.26, 2)
    glVertex2f(-2.26, 1.3)
    glVertex2f(-1.9, 1)

    glVertex2f(-2.26, 1.3)
    glVertex2f(-2.7, 1.7)
    glVertex2f(-1.75, 1.7)

    glVertex2f(-2.26, 2)
    glVertex2f(-2.26, 1.3)
    glVertex2f(-2.6, 1)

    glEnd()


def main():
    pygame.init()
    display = 500, 500
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)

    gluPerspective(80, display[0] / display[1], 1, 10)
    glTranslate(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw()
        pygame.display.flip()


main()
