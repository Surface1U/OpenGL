import pygame as pg
import pygame.key
import time
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import math


def draw():

    #голубой
    glColor3f(0.0, 0.5, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(-4, -2)
    glVertex2f(2, -2)
    glVertex2f(2, 2)
    glVertex2f(-4, 2)

    glEnd()

#зелёный треугольник

    glColor3f(0, 1, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-4, -2)
    glVertex2f(2, 2)
    glVertex2f(2, -2)
    glEnd()


#линия от двух углов
    glColor3f(1,1,0)
    glBegin(GL_QUADS)
    glVertex2f(-3.6, -2)
    glVertex2f(2, 1.6)
    glVertex2f(1.6, 2)
    glVertex2f(-4, -1.6)
    glEnd()





    glColor3f(1, 1, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-4, -1.6)
    glVertex2f(-3.6, -2)
    glVertex2f(-4, -2)

    glEnd()

    glColor3f(1, 1, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(2, 1.6)
    glVertex2f(1.6, 2)
    glVertex2f(2, 2)

    glEnd()





    # Звезда



def draw_star(x, y):
    glBegin(GL_TRIANGLES)
    glColor3f(1, 1, 1)
    glVertex2f(-2.26+x, 2+y)
    glVertex2f(-2.26+x, 1.3+y)
    glVertex2f(-1.9+x, 1+y)

    glVertex2f(-2.26+x, 1.3+y)
    glVertex2f(-2.7+x, 1.7+y)
    glVertex2f(-1.75+x, 1.7+y)

    glVertex2f(-2.26+x, 2+y)
    glVertex2f(-2.26+x, 1.3+y)
    glVertex2f(-2.6+x, 1+y)

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
        draw_star(0.5,0)
        draw_star(-1.2, 0)

        draw_star(-0.36, -0.5)


        draw_star(0.5, -0.9)
        draw_star(-1.2, -0.9)
        pygame.display.flip()


main()
