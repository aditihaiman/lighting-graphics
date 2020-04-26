from display import *
from draw import *
from parser import *
from matrix import *
import math


# lighting values
view = [0, #view vector
        0,
        1];
ambient = [50,
           50,
           50]
light = [[0.5, 0.75, 1], #light vector
         [0,255,255]] #color of point light
areflect = [0.1, #Ka
            0.1,
            0.1]
dreflect = [0.5, #Kd
            0.5,
            0.5]
sreflect = [0.5, #Ks
            0.5,
            0.5]



screen = new_screen()
zbuffer = new_zbuffer()
color = [ 0, 255, 0 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]


parse_file( 'script2', edges, polygons, csystems, screen, zbuffer, color, view, ambient, light, areflect, dreflect, sreflect)
