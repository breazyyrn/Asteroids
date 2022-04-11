import shapes

def tile(x, y, scale):
    '''Creating square tile built up using the Shapes class in shapes.y'''
    tile = shapes.Square(color='purple')
    border = shapes.Square(color='yellow')
    triangle = shapes.Triangle(color='green')
    diamond = shapes.Diamond(color='sky blue')
    


    '''Draws the borde rof the Mosaic; We want this code outside the for loop'''
    border.draw(x,y,scale*7.2)

    
    tile.draw(150,50)
    triangle.draw(20, -50, heading=180)
    diamond.draw(-230, 50, scale=0.6)
            
            


    
    tile.TurtleInterpreter.hold()

def mosaic(x, y, scale, Nx, Ny):
    '''Creating square tile built up using the Shapes class in shapes.y'''
    tile = shapes.Square(color='purple')
    border = shapes.Square(color='yellow')
    triangle = shapes.Triangle(color='green')
    diamond = shapes.Diamond(color='sky blue')
    


    '''Draws the borde rof the Mosaic; We want this code outside the for loop'''
    border.draw(x,y,scale*7.2)

    for i in range(Nx):
        for j in range(Ny):
            tile.draw(x+i*(720/4)+50, y-j*(720/5)-50, scale=0.9)
            triangle.draw(x+i*(720/4)+140, y-j*(720/5)-130, scale=0.9, heading=180)
            diamond.draw(x+i*(720/4)+95, y-j*(720/5)-69, scale=0.35)
            


      
    # tile.TurtleInterpreter.hold()

    

# tile(-360, 360, scale=1)

# mosaic(-360, 360, scale=1,Nx=4, Ny=5)

  
