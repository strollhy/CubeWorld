import pyglet

from pyglet.gl import *

fps = pyglet.clock.ClockDisplay()

# The game window
class Window(pyglet.window.Window):
    def __init__(self):
        super(Window, self).__init__(fullscreen=False, vsync = False)
        self.flipScreen = 0
        glClearColor(1.0, 1.0, 1.0, 1.0)
        # Run "self.update" 128 frames a second and set FPS limit to 128.
        pyglet.clock.schedule_interval(self.update, 1.0/128.0)
        pyglet.clock.set_fps_limit(128)


    def update(self, dt):
        self.flipScreen = not self.flipScreen
        pass

    def on_draw(self):
        pyglet.clock.tick() # Make sure you tick the clock!
        if self.flipScreen == 0:
            glClearColor(0, 1, 0, 1.0)
        else:
            glClearColor(1, 0, 0, 1.0)
        self.clear()
        fps.draw()

# Create a window and run
win = Window()
pyglet.app.run()