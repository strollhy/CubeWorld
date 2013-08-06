# OpenGL stuff
from OpenGL.GL import *
from OpenGL.GLU import *

from gameobjects.matrix44 import * 
from gameobjects.vector3 import *

class Cube(object):
	
	def __init__(self, position, color):
		self.position = position
		self.color = color

	# Cube information
	num_faces = 6
	vertices = [ (0.0, 0.0, 1.0),
				 (1.0, 0.0, 1.0),
				 (1.0, 1.0, 1.0),
				 (0.0, 1.0, 1.0),
				 (0.0, 0.0, 0.0),
				 (1.0, 0.0, 0.0),
				 (1.0, 1.0, 0.0),
				 (0.0, 1.0, 0.0) ]

	vertex_indices = [ (0, 1, 2, 3),	# front
					   (4, 5, 6, 7),	# back
					   (1, 5, 6, 2), 	# right
					   (0, 4, 7, 3),	# left
					   (3, 2, 6, 7),	# top
					   (0, 1, 5, 4)	]	# bottom
	
	def render(self):
		# Set the cube color, applies to all vertices till next call
		glColor(self.color)

		# Adjust all the vertices so that the cube is at self.position
		vertices = []
		for v in self.vertices:
			vertices.append(tuple(Vector3(v) + self.position))

		# Draw all 6 faces of the cube
		glBegin(GL_QUADS)

		for face_no in xrange(self.num_faces):
			#glNormal3dv(self.normals[face_no])

			v1, v2, v3, v4 = self.vertex_indices[face_no]

			glVertex(vertices[v1])
			glVertex(vertices[v2])
			glVertex(vertices[v3])
			glVertex(vertices[v4])

		glEnd()


class Map(object):

	def __init__(self):
		self.cubes = []
		
		cube = Cube((1.0, 0.0, 1.0), (1.0, 0.0, 0.0))
		self.cubes.append(cube)

	def render(self):
		for cube in self.cubes:
			cube.render()