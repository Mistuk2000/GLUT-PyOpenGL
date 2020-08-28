from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    BresenhamLine([10,10],[140,100]) #Any choice of coordinates
    glFlush()
    return
def drawLineLow(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    if x1 > x2:
        x, y = x2, y2
        x2, y2 = x1, y1
        x1, y1 = x, y
    x, y = x1, y1
    p = 2*dy - dx
    glBegin(GL_POINTS)
    glVertex2i(x,y)
    while x<=x2:
        x += 1
        if p < 0:
            p += 2 * dy
        else:
            if (dy/dx) > 0:
                y += 1
            else:
                y -= 1
            p += 2*(dy - dx)
        glVertex2i(x,y)
    glEnd()
    glFlush()

def drawLineHigh(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    if y1 > y2:
        x, y = x2, y2
        x2, y2 = x1, y1
        y1, y1 = x, y
    x, y = x1, y1
    p = 2*dx - dy
    glBegin(GL_POINTS)
    glVertex2i(x,y)
    while y<=y2:
        y += 1
        if p < 0:
            p = p + 2*dy
        else:
            if (dy/dx) > 0:
                x += 1
            else:
                x -= 1
            p = p + (2 * dy - 2 * dx)
        glVertex2i(x,y)
    glEnd()
    glFlush()

def BresenhamLine(start, dest):
    if(abs(dest[1]-start[1]) == 0):
        x = min(start[0], dest[0])
        glBegin(GL_POINTS)
        while x<max(start[0],dest[0]):
            x+=1
            glVertex2i(x,start[1])
        glEnd()
        glFlush()
    elif(abs(dest[0]-start[0]) == 0):
        y = min(start[1],dest[1])
        glBegin(GL_POINTS)
        while y<max(start[1],dest[1]):
            y+=1
            glVertex2i(start[0],y)
        glEnd()
        glFlush()
    elif(abs(dest[1]-start[1]) <= abs(dest[0]-start[0])):
        drawLineLow(start[0],start[1],dest[0],dest[1])
    else:
        drawLineHigh(start[0],start[1],dest[0],dest[1])
        
glutInit() # Initialize a glut instance which will allow us to customize our window
glutInitDisplayMode(GLUT_SINGLE  | GLUT_RGB);    # set Display mode
glutInitWindowSize(640, 480)   # Set the width and height of your window
glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
wind = glutCreateWindow("OpenGL Coding Practice") # Give your window a title
glutIdleFunc(display)     # Draw any graphics or shapes in the display function at all times
glClearColor(0.0, 0.0, 0.0, 1.0);  # set black background color
glColor3f(1.0, 1.0, 1.0); #  set the drawing color(white)
glPointSize(4.0);         # a 'dot' is 4 by 4 pixels
gluOrtho2D(0, 640, 0, 480);
glClear(GL_COLOR_BUFFER_BIT)
glutDisplayFunc(display)# Tell OpenGL to call the display method continuously
glFlush();
glutMainLoop()  # Keeps the window created above displaying/running in a loop
