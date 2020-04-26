import math
from display import *


  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    lighting = [0,0,0]
    alight = calculate_ambient(ambient, areflect)
    diffuse = calculate_diffuse(light, dreflect, normal)
    specular = calculate_specular(light, sreflect, view, normal)
    
    lighting[0] = int(alight[0] + diffuse[0] + specular[0])
    lighting[1] = int(alight[1] + diffuse[1] + specular[1])
    lighting[2] = int(alight[2] + diffuse[2] + specular[2])
    limit_color(lighting)
    return lighting

def calculate_ambient(alight, areflect):
    A = [0,0,0]
    A[0] = alight[0] * areflect[0]
    A[1] = alight[1] * areflect[1]
    A[2] = alight[2] * areflect[2]
    return A

def calculate_diffuse(light, dreflect, normal):
    L = light[0]
    normalize(normal)
    normalize(L)
    diffuse = [0, 0, 0]
    diffuse[0] = light[1][0] * dreflect[0] * dot_product(normal, L, True)
    diffuse[1] = light[1][1] * dreflect[1] * dot_product(normal, L, True)
    diffuse[2] = light[1][2] * dreflect[2] * dot_product(normal, L, True)
    return diffuse

def calculate_specular(light, sreflect, view, normal):
    L = light[0]
    normalize(normal)
    normalize(L)
    normalize(view)
    
    R = [0,0,0]
    R[0] = (2 * normal[0] * dot_product(normal, L, True) - L[0])
    R[1] = (2 * normal[1] * dot_product(normal, L, True) - L[1])
    R[2] = (2 * normal[2] * dot_product(normal, L, True) - L[2])
    
    normalize(R)
    
    prod = math.pow(dot_product(R, view, True), SPECULAR_EXP)
    
    specular = [0, 0, 0]
    specular[0] = light[1][0] * sreflect[0] * prod
    specular[1] = light[1][1] * sreflect[1] * prod
    specular[2] = light[1][2] * sreflect[2] * prod
    return specular

def limit_color(color):
    for x in range(3):
        if(color[x] < 0): color[x] = 0
        if(color[x] > 255): color[x] = 255

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b, check=False):
    temp = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
    if(check and temp < 0): temp = 0
    return temp

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
