import turtle
import sys
import math
import random


class TurtleInterpreter:
    # global screen
    # global turtle
    turtleObject = turtle.Turtle()
    screen = turtleObject.getscreen()
    def __init__(self, width=720, height=720, bgColor='white'):
        
    
        

        '''TurtleInterpreter constructor.
    Creates instance variables for a Turtle object and a Screen object with a particular window
    `width`, `height`, and background color `bgColor`.
    '''
    # Create a Turtle object, set it as an instance variable

    # Create a Screen object, set it as an instance variable.
    # Set the screen's height, width, and color based on the parameters

    # Turn the screen's tracer off.
        TurtleInterpreter.turtleObject.hideturtle()
        '''Commented out because I made variable "screen" a global variable'''
        # self.screen = TurtleInterpreter.screen
        self.screen = TurtleInterpreter.screen
        self.width = width
        self.height = height
        self.bgColor = bgColor
        '''Commented out because I made variable "screen" a global variable'''
        # screen.screensize(self.width, self.height, self.bgColor)
        TurtleInterpreter.screen.screensize(self.width, self.height, self.bgColor)
        '''turn screen tracer off'''
        '''Commented out because I made variable "screen" a global variable'''
        # screen.tracer(False)
        TurtleInterpreter.screen.tracer(False)
        # self.positions = []
        # self.colors = []

    def setColor(self, c):
        TurtleInterpreter.turtleObject.pencolor(c)
        '''Commented out because I made variable "turtle" a global variable'''
        # turtle.pencolor(c)

    def setWidth(self, w):
        TurtleInterpreter.turtleObject.pensize(w)
        '''Commented out because I made variable "turtle" a global variable'''
        # turtle.pensize(w)


    def goto(self, x, y, heading=None):
        TurtleInterpreter.turtleObject.penup()
        TurtleInterpreter.turtleObject.goto(x,y)
        TurtleInterpreter.turtleObject.pendown()
        '''Commented out because I made variable "screen" a global variable'''
        # turtle.penup()
        # turtle.goto(x,y)
        # turtle.pendown()

        if(heading != None):
            TurtleInterpreter.turtleObject.setheading(heading)
            '''Commented out because I made variable "screen" a global variable'''
            # turtle.setheading(heading)
        # turtle.pendown()

    def setHeading(self, heading = None):
        if(heading != None):
            TurtleInterpreter.turtleObject.setheading(heading)
            '''Commented out because I made variable "screen" a global variable'''
            # turtle.setheading(heading)
    
    # def orient(self, angle):
    #     turtle.setheading(angle)

    '''Returns Screen'''
    def getScreen(self):
        return self.screen

    def getScreenWidth(self):
        return self.width

    def getScreenHeight(self):
        return self.height

    def place(self, xpos, ypos, angle=None):
        TurtleInterpreter.turtleObject.penup()
        TurtleInterpreter.turtleObject.goto(xpos, ypos)
        if angle != None:
            TurtleInterpreter.turtleObject.setheading(angle)
        TurtleInterpreter.turtleObject.pendown


    
    
    def drawString(self, lsysString, distance, angle):
        
        
        '''Interpret each character in an L-system string as a turtle command.

    Here is the starting L-system alphabet:
        F is forward by a certain distance
        + is left by an angle
        - is right by an angle
        [ saves the turtle heading and position
        ] restores the turtle's heading and position to the most recently saved heading and position
        < saves the turtle's color
        > restores the turtle's color
        g set the turtle's color to green
        y set the turtle's color to yellow
        r set the turtles color to yellow
        L draw a circle
        B draw a berry at the current turtle position
        { have the turtle start filling
        } have the turtle stop filling

        

    Parameters:
    -----------
    lsysString: str. The L-system string with characters that will be interpreted as drawing
        commands.
    distance: distance to travel with F command.
    angle: turning angle (in deg) for each right/left command.
    '''

    # Walk through the lsysString character-by-character and
    # have the turtle object (instance variable) carry out the
    # appropriate commands

    # Call the update method on the screen object to make sure
    # everything drawn shows up at the very end of the method
    # (remember: you turned off animations in the constructor)

        
        
        ourEmptyStack = []
        colorStack = []
        widthStack = []
        for i in lsysString:
            if i == 'F':
                TurtleInterpreter.turtleObject.forward(distance)
                '''Commented out because I made variable "turtle" a global variable'''
                # turtle.forward(distance)

            elif i == '+':
                TurtleInterpreter.turtleObject.left(angle)

            elif i == '-':
                TurtleInterpreter.turtleObject.right(angle)

            elif i == '[':
                ourEmptyStack.append(TurtleInterpreter.turtleObject.position())
                ourEmptyStack.append(TurtleInterpreter.turtleObject.heading())

            elif i == ']':
                heading = ourEmptyStack.pop()
                position = ourEmptyStack.pop()
                TurtleInterpreter.turtleObject.up()
                TurtleInterpreter.turtleObject.setheading(heading)
                TurtleInterpreter.turtleObject.goto(position)
                TurtleInterpreter.turtleObject.down()
            
            
            

            elif i == '<':
                colorStack.append(TurtleInterpreter.turtleObject.color()[0])
            elif i == '>':
                color = colorStack.pop(0)
                TurtleInterpreter.turtleObject.pencolor(color)
                # turtle.color(self.colors.pop(-1))
            elif i == 'g':
                TurtleInterpreter.turtleObject.pencolor(0.15, 0.5, 0.2)
                TurtleInterpreter.turtleObject.fillcolor(0.15, 0.5, 0.2)
            elif i == 'y':
                TurtleInterpreter.turtleObject.pencolor(0.8, 0.8, 0.3)
                TurtleInterpreter.turtleObject.fillcolor(0.8, 0.8, 0.3)
            elif i == 'r':
                TurtleInterpreter.turtleObject.pencolor(0.7, 0.2, 0.3)
                TurtleInterpreter.turtleObject.fillcolor(0.7, 0.2, 0.3)
            elif i == 'L':
                a = random.randint(1, 3)
                if a == 1:
                    TurtleInterpreter.turtleObject.fillcolor('red')
                    TurtleInterpreter.turtleObject.pencolor('red')
                elif a == 2:
                    TurtleInterpreter.turtleObject.fillcolor('yellow')
                    TurtleInterpreter.turtleObject.pencolor('yellow')
                elif a == 3:
                    TurtleInterpreter.turtleObject.fillcolor('green')
                    TurtleInterpreter.turtleObject.pencolor('green')
                widthStack.append(TurtleInterpreter.turtleObject.width())
                TurtleInterpreter.turtleObject.width(2)
                TurtleInterpreter.turtleObject.begin_fill()
                TurtleInterpreter.turtleObject.left(60)
                TurtleInterpreter.turtleObject.forward(distance*0.75)
                TurtleInterpreter.turtleObject.right(90)
                TurtleInterpreter.turtleObject.forward((distance*0.75)**0.5)
                TurtleInterpreter.turtleObject.right(60)
                TurtleInterpreter.turtleObject.forward((distance*0.75)**0.5)
                TurtleInterpreter.turtleObject.right(90)
                TurtleInterpreter.turtleObject.forward((distance*0.75))
                TurtleInterpreter.turtleObject.right(120)
                TurtleInterpreter.turtleObject.end_fill()
                oldWidth = widthStack.pop()
                TurtleInterpreter.turtleObject.width(oldWidth)
            
            
                
             

            elif i == 'B':
                ourEmptyStack.append(turtle.position())
                ourEmptyStack.append(turtle.heading())
                turtle.circle(distance/4)
                turtle.penup()
                turtle.setheading(ourEmptyStack.pop(-1))
                turtle.setposition(ourEmptyStack.pop(-1))
                turtle.pendown()
            
            elif i == '{':
                TurtleInterpreter.turtleObject.begin_fill()
            elif i == '}':
                TurtleInterpreter.turtleObject.end_fill()
           
            
        
        TurtleInterpreter.screen.update()
        '''Commented out because I made variable "screen" a global variable'''
        # screen.update()

                    



    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' key'''

    # Hide the turtle cursor and update the screen
        TurtleInterpreter.turtleObject.hideturtle()
        TurtleInterpreter.screen.update()

    # Close the window when users presses the 'q' key
        TurtleInterpreter.screen.onkey(turtle.bye, 'q')

    # Listen for the q button press event
        TurtleInterpreter.screen.listen()

    # Have the turtle listen for a click
        TurtleInterpreter.screen.exitonclick()

    



    



         




    



    

