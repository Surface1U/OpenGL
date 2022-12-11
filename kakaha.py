import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *
import math
import sys



def draw_cylinder(radius, height, num_slices):
    r = radius
    h = height
    n = float(num_slices)

    circle_pts = []
    for i in range(int(n) + 1):
        angle = 2 * math.pi * (i/n)
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        pt = (x, y)
        circle_pts.append(pt)

    glBegin(GL_TRIANGLE_FAN)#drawing the back circle
    glColor(1, 1, 0)
    glVertex(0, 0, h/2.0)
    for (x, y) in circle_pts:
        z = h/2.0
        glVertex(x, y, z)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)#drawing the front circle
    glColor(1,1, 0)
    glVertex(0, 0, h/2.0)
    for (x, y) in circle_pts:
        z = -h/2.0
        glVertex(x, y, z)
    glEnd()

    glBegin(GL_TRIANGLE_STRIP)#draw the tube
    glColor(1, 1, 0)
    for (x, y) in circle_pts:
        z = h/2.0
        glVertex(x, y, z)
        glVertex(x, y, -z)
    glEnd()


global program

pygame.init()
(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height), OPENGL | DOUBLEBUF)
clock = pygame.time.Clock()
rotation = 0.0
# program = compileProgram(
#     compileShader(vertex_shader,GL_VERTEX_SHADER),
#     compileShader(fragment_shader,GL_FRAGMENT_SHADER)
# )

glLight(GL_LIGHT0, GL_POSITION, (0,0,1,0.6))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0, 0.5, 0.1, 0))

glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (1,1,0,0))
glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 128)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rotation += 1.0
    glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(30, float(width)/height, 1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(0, 0, -50)#move back far enough to see this object 
    glRotate(rotation, 0, 1, 0)#NOTE: this is applied BEFORE the translation due to OpenGL multiply order

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        glTranslatef(0,3,0)
    elif keys[pygame.K_RIGHT]:
        glTranslatef(0,-3,0)


    draw_cylinder(5, 10, 20)

    glDisable(GL_LIGHT0)
    glDisable(GL_LIGHTING)
    glDisable(GL_COLOR_MATERIAL)

    pygame.display.flip()
    clock.tick(60)
