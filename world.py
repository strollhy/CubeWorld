from pyglet import clock, image
from pyglet.gl import *
    

class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        
        self.angle = 0
        # A Batch is a collection of vertex lists for batched rendering.
        self.batch = pyglet.graphics.Batch()
        
        
    def on_draw(self):
        self.clear()
        

        glRotatef(self.angle, 0, 1, 0)
        
        self.batch.add(4, GL_QUADS, None,  ('v3f/static', (300,300,0,  300,350,0,  350,350,0, 350,300,0)), ('c3B', (255,0,0, 0,0,255, 255,0,0, 0,0,255 )))
        self.batch.add(4, GL_QUADS, None,  ('v3f/static', (300,300,100,  300,350,100,  300,350,200, 300,300,200)), ('c3B', (255,0,0, 0,0,255, 255,0,0, 0,0,255 )))        
        self.batch.add(4, GL_QUADS, None, ('v2i/static', (100,100, 100,150, 150,150, 150,100)), ('c3B', (255,0,0, 0,255,0, 0,0,255, 255,255,255)))
        self.batch.draw()
        

        
    def update(self, dt):
        self.angle += 45
        self.angle %= 90
        

################################################
def setup2d():
    glDisable(GL_DEPTH_TEST)
    

def setup():
    # Set the color of "clear", i.e. the sky, in rgba.
    glClearColor(0.5, 0.69, 1.0, 1)

    
def main():
    window = Window(width=800, height=600)
    #pyglet.clock.schedule(window.update)
    #clock.set_fps_limit(10)
    setup()
    pyglet.app.run()
    

if __name__ == '__main__':
    main()