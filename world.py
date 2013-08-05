import pygame
from pygame.locals import *
from sys import exit

SCREEN_SIZE = (800, 600)

# OpenGL stuff
from OpenGL.GL import *
from OpenGL.GLU import *

def resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60., float(width)/height, 1., 10000.)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(1.0, 1.0, 1.0, 0.0)

    glShadeModel(GL_FLAT)
    glEnable(GL_COLOR_MATERIAL)


# clock from pygame
clock = pygame.time.Clock()

###
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE|OPENGL|DOUBLEBUF)
    pygame.display.set_caption("Hello, World!")

    resize(*SCREEN_SIZE)
    init()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        time_passed = clock.tick(30)


if __name__ == "__main__":
    main()