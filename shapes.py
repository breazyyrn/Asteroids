
from turtle import Screen, color
import turtle_interpreter as ti




class Shape():
    
    def __init__(self, distance=100, angle=90, color=(0, 0, 0), lsysString=''):
        '''Shape constructor

    Parameters:
    -----------
    distance: float. Distance in pixels to go when moving the turtle forward
    angle: float. Angle in degrees to turn when turning the turtle left/right
    color: tuple of 3 floats. Default turtle pen color
    lsysString: str. The L-system string of drawing commands to draw the shape
        (e.g. made up of 'F', '+', '-', ...)
    '''
        self.distance = distance
        self.angle = angle
        self.color = color
        self.string = lsysString
        self.TurtleInterpreter = ti.TurtleInterpreter(width=720, height=720, bgColor='white')
    
        
    def getTI(self):
        '''This function returns the Turtle Interpreter'''
        return self.TurtleInterpreter
    
    def getString(self):
        '''This function returns the LsysString'''
        return self.string
    
    def setColor(self, c):
        self.color = c
        self.TurtleInterpreter.turtle.begin_fill()
        self.TurtleInterpreter.turtle.fillcolor(c)
        self.TurtleInterpreter.turtle.end_fill()
    
    def setDistance(self, dist):
        self.distance = dist
        '''This function sets the Shapes edge distance'''
        self.TurtleInterpreter.setWidth(dist)
        

    def setAngle(self, a):
        self.angle = a
    
    def setString(self, s):
        self.string = s
    
    def draw(self, x, y, scale=1.0, heading=0):
        '''Draws the L-system string at the position `(x, y)` = `(x_pos, y_pos)` with the turtle
    facing the heading `heading`. The turtle drawing distance is scaled by `scale`.

    '''
        self.TurtleInterpreter.turtleObject.hideturtle()
        self.TurtleInterpreter.goto(x, y)
        self.TurtleInterpreter.setHeading(heading)
        self.TurtleInterpreter.turtleObject.color(self.color)

        self.TurtleInterpreter.drawString(self.string, self.distance*scale, self.angle)
        
        

        

class Square(Shape):
    def __init__(self, distance=100, angle = 90, color=(0, 0, 0), lsysString='F-F-F-F-', fill=True):
        super().__init__(distance, angle, color, lsysString)
        '''Commented this out because you dont need both functions Draw and Drawstring to draw any of these
        shapes.... plus remember that the function drawstring is actually from turtle itnerpreter and not 
        class: Shape'''
        # self.TurtleInterpreter.drawString(self.string, distance, angle)
        if fill == True:
            self.string = "{"+lsysString+"}"

        self.TurtleInterpreter.turtleObject.begin_fill()
        self.TurtleInterpreter.turtleObject.fillcolor(color)
        self.TurtleInterpreter.turtleObject.end_fill()
        
  
        
        
class Triangle(Shape):
    def __init__(self, distance=100, angle=120, color=(0, 0, 0), lsysString='{F-F-F-}', fill=True):
        super().__init__(distance, angle, color, lsysString)
        '''Commented this out because you dont need both functions Draw and Drawstring to draw any of these
        shapes.... plus remember that the function drawstring is actually from turtle itnerpreter and not 
        class: Shape'''
         # self.TurtleInterpreter.drawString(self.string, distance, angle)

        if fill == True:
            self.string = "{"+lsysString+"}"

        self.TurtleInterpreter.turtleObject.begin_fill()
        self.TurtleInterpreter.turtleObject.fillcolor(color)
        self.TurtleInterpreter.turtleObject.end_fill()
        
        


class Diamond(Shape): 
    def __init__(self, distance=100, angle=30, color=(0, 0, 0), lsysString='{----F++F++++F++F+++++}', fill=True):
        super().__init__(distance, angle, color, lsysString)
        if fill == True:
            self.string = "{"+lsysString+"}"

        self.TurtleInterpreter.turtleObject.begin_fill()
        self.TurtleInterpreter.turtleObject.fillcolor(color)
        self.TurtleInterpreter.turtleObject.end_fill()
        
        

def main():

    
    '''Draws Square'''
    squareLeft = Square(color='blue', fill=True)
    squareLeft.draw(0,0)
    
    '''Draws Triangle'''
    triangle = Triangle(color='green', fill=True)
    triangle.draw(-50, -100, scale=1, heading=180)

    '''Draws Diamond'''
    diamond = Diamond(color='purple', fill=True)
    diamond.draw(190, -105, scale = 1, heading=180)


    ti.TurtleInterpreter.hold(main)


if __name__ == '__main__':
    main()





