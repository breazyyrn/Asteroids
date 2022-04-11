
import turtle
import mosaic as mos
import turtle_interpreter as ti
import random

class Game():
    
    def __init__(self):
        mos.mosaic(-360, 360, scale=1,Nx=4, Ny=5)
        self.turtleInterpreter = ti.TurtleInterpreter(width=720,height=720,bgColor='white')
        screenObject = self.turtleInterpreter.getScreen()
        self.screen = screenObject

        '''enemy list'''
        self.enemyList = []        


        '''Player Object & Players speed'''
        self.player = Game.makePlayer(self)
        self.playerSpeed = 20
        
        
        '''Players turning rate by angle...Made this a list so that each keyboard command could have 
        its own angel turning point'''
        self.playerTurnRate = [180, 0, 90]
        self.ourSetupEventsMethodObject = Game.setupEvents(self)
        


        '''COORDINATES SHOWING TOP LEFT, TOP RIGHT, BOTTOM LEFT AND BOTTOM RIGHT'''
        # self.enemyBoundary = [-340, 340, 340, 340, -340, -340, 340, -340]
        '''minimum and maximum x and y positions that game enemies can occupy'''
        '''This is the enemy boundary'''
        self.minimumX = -340
        self.maximumX = 340
        self.minimumY = -340
        self.maximumY = 340

        '''Creates enemies'''
        self.n = 5
        self.makeEnemies(self.n)
        self.moveEnemiesRandomly()

        '''Collision Radius'''
        self.collisionRadius = 30


        
       

    def makePlayer(self):
        
        mainPlayerTurtleObject = turtle.Turtle()
        self.screen.register_shape('rocketship.gif')
        mainPlayerTurtleObject.shape('rocketship.gif')
        mainPlayerTurtleObject.penup()
        # mainPlayerTurtleObject.forward(25)
        return mainPlayerTurtleObject
    '''Keyboard Movements for Player'''
    def up(self):
        self.player.setheading(self.playerTurnRate[2])
        self.player.forward(self.playerSpeed)

    def down(self):
        self.player.setheading(self.playerTurnRate[2])
        self.player.back(self.playerSpeed)

    def left(self):
        # self.player.left(self.playerTurnRate)
        self.player.setheading(self.playerTurnRate[0])
        self.player.forward(self.playerSpeed)

    def right(self):
        # self.player.right(self.playerTurnRate)
        self.player.setheading(self.playerTurnRate[1])
        self.player.forward(self.playerSpeed)

    '''Setup Events method to execute event per keyboard button clicked'''

    def setupEvents(self):
        self.screen.onkey(self.up, 'Up')
        self.screen.onkey(self.down, 'Down')
        self.screen.onkey(self.left, 'Left')
        self.screen.onkey(self.right, 'Right')
        # self.screen.ontimer(self.moveEnemiesRandomly, 50)
        self.screen.ontimer(self.checkForCollisions, 50)
    
    

    def placeEnemyRandomly(self, turt):
        turt.shape('square')
        turt.color('red')
        xBoundary = random.randint(self.minimumX, self.maximumX)
        yBoundary = random.randint(self.minimumY, self.maximumY)
        turt.penup()
        turt.goto(xBoundary,yBoundary)
        return turt
        

    def makeEnemies(self, n):
        self.enemyList = []
        self.n = n
        for i in range(n):
            enemy = self.placeEnemyRandomly(turtle.Turtle())
            self.enemyList.append(enemy)
            # enemy.penup()
            # self.placeEnemyRandomly
        return self.enemyList
    
    def moveEnemiesRandomly(self):
        for enemies in self.enemyList:
            (x, y) = enemies.pos()
            enemies.goto(x+random.randint(-10, 10), y+random.randint(-10, 10))
        self.screen.ontimer(self.moveEnemiesRandomly, 50)

    def checkForCollisions(self):
        for index in range(len(self.enemyList)):
            self.enemy = self.enemyList[index]
            enemyXCor = self.enemy.xcor()
            enemyYCor = self.enemy.ycor()

            playerXCor = self.player.xcor()
            playerYCor = self.player.ycor()

            if abs(enemyXCor - playerXCor) < self.collisionRadius:
                if abs(enemyYCor - playerYCor) < self.collisionRadius:
                    print('FUCKED')
                    self.placeEnemyRandomly(self.enemy)

        self.screen.ontimer(self.checkForCollisions, 50)

        # for enemiesDistance in self.enemyList:
        #     (x, y) = enemiesDistance.pos()
        #     (xcor, ycor) = self.player.pos()
        #     if (x,y) == (xcor, ycor):
        #         print('the two have collided')
        #         print(enemiesDistance.pos())
        #         print(self.player.pos())
        '''TRY OUT THIS CODE TOO INORDDER TO INCRESE EFFICENCY OF CODE'''
            
        
        
    def play(self):
        
        '''Turns the tracer animations on (but speeds up animations) and starts the main game loop.
        '''
    # Call the tracer method on your `Screen` instance variable,
    # passing in True as the parameter to turn animations on.

    # Call the listen method on your `Screen` instance variable
    # so that keyboard presses are not registered as events

    # Call the mainloop method on your `Screen` instance variable.
        self.screen.tracer(True)
        self.screen.listen()
        '''Nothing happens to screen until a key is pressed'''
        self.screen.mainloop()

def main():
    gameObject = Game()
    gameObject.play()


if __name__ == '__main__':
    main()
        



        