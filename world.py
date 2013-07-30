import pyglet
from pyglet.gl import *
from pyglet import clock, window

'''
    http://www.learnersdictionary.com/search/aspect
    a dictionary site

    http://www.opengl.org/sdk/docs/man2/
    opengl api reference

'''

###
def vector(type, *args):
    '''
        return a ctype array
        GLfloat
        GLuint
        ...
    '''
    return (type*len(args))(*args)

###
def setup():
    # look for GL_DEPTH_BUFFER_BIT
    glEnable(GL_DEPTH_TEST)


def cube_vertices(x, y, z, n):
    """ Return the vertices of the cube at position x, y, z with size 2*n.

    """
    return [
        x-n,y+n,z-n, x-n,y+n,z+n, x+n,y+n,z+n, x+n,y+n,z-n,  # top
        x-n,y-n,z-n, x+n,y-n,z-n, x+n,y-n,z+n, x-n,y-n,z+n,  # bottom
        x-n,y-n,z-n, x-n,y-n,z+n, x-n,y+n,z+n, x-n,y+n,z-n,  # left
        x+n,y-n,z+n, x+n,y-n,z-n, x+n,y+n,z-n, x+n,y+n,z+n,  # right
        x-n,y-n,z+n, x+n,y-n,z+n, x+n,y+n,z+n, x-n,y+n,z+n,  # front
        x+n,y-n,z-n, x-n,y-n,z-n, x-n,y+n,z-n, x+n,y+n,z-n,  # back
    ]



#############
''' Model '''
#############
class model:
    def __init__(self, vertices, colorMatrix, indice):
        self.vertices = vector(GLfloat, *vertices)
        self.colorMatrix = vector(GLfloat, *colorMatrix)
        self.indice = vector(GLuint, *indice)
        self.angle = 0
        self.batch = pyglet.graphics.Batch()

    def update(self):
        self.angle += 3
        self.angle %= 360

    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glRotatef(self.angle, 1, 1, 1)

        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)

        glColorPointer(3, GL_FLOAT, 0, self.colorMatrix)
        glVertexPointer(3, GL_FLOAT, 0, self.vertices)
        glDrawElements(GL_QUADS, len(self.indice), GL_UNSIGNED_INT, self.indice)
        
        glDisableClientState(GL_COLOR_ARRAY)
        glDisableClientState(GL_VERTEX_ARRAY)


#############
''' World '''
#############
class world:
    def __init__(self):
        self.element = []

    def update(self, dt):
        for obj in self.element:
            obj.update()

    def addModel(self, model):
        self.element.append(model)

    def draw(self):
        for obj in self.element:
            obj.draw()


########################################################################
win = window.Window(fullscreen=False, vsync=True, resizable=True, height=600, width=600)
mWorld = world()

''' 
coordinates of vertices 
'''
cube = (
    1, 1, 1, #0
    -1, 1, 1, #1
    -1, -1, 1, #2
    1, -1, 1, #3
    1, 1, -1, #4
    -1, 1, -1, #5
    -1, -1, -1, #6
    1, -1, -1 #7
)

''' 
colors of vertices 
'''
color = (
    1, 1, 0,
    1, 1, 0,
    1, 0, 0,
    1, 0, 0,
    0, 1, 0,
    0, 1, 0,
    0, 0, 1,
    0, 0, 1
)

''' 
Define the vertex indices for the cube 
'''
indice = (
    0, 1, 2, 3, # front face
    0, 4, 5, 1, # top face
    4, 0, 3, 7, # right face
    1, 5, 6, 2, # left face
    3, 2, 6, 7, # bottom face
    4, 5, 6, 7, # back face
)

obj = model(cube, color, indice)
mWorld.addModel(obj)


@win.event
def on_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -10, 10)
    glMatrixMode(GL_MODELVIEW)
    return pyglet.event.EVENT_HANDLED

@win.event
def on_draw():
    # set background color
    glClearColor(0.6, 0.6, 0.6, 0.8)
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    mWorld.draw()


pyglet.clock.schedule(mWorld.update)
clock.set_fps_limit(30)
setup()
pyglet.app.run()