 #ceci est un commentaire
#pour faire une foction on ecrit "setup:"
BallX = 0
BallY = 0
BallSpeedX = 5
BallSpeedY = 2
BallRadius = 5 

racketwidth = 50 
racketheight = 20
racketX = 0 
racketY = 0


def setup():
    global BallX, BallY, BallSpeedX, BallSpeedY, BallRadius 
    global racketwidth, racketX, racketY, racketheight
    #ici on inscrit "print" pour écrire quelque chose
    #print("hello world")
    #ici on defini la taille de la fenetre 
    size(400,400) 
    clear()
    #on defini la couleur avec la quelle on vas definir les formes suivantes 
    fill(250, 0, 0)
    #dessiner une ellipse avec des parametre suivant : x, y, diamètre hauteur, diamètre largeur 
    frameRate(60)
    BallX = width/2
    BallY = height/2  
    
    racketX = mouseX - (racketwidth/2) 
    racketY = height - 50
    
    
    
def draw():
    clear() 
    fill(255)
    drawRacket() 
    
    drawBall()
    #ellipse(mouseX, mouseY, 80, 80)
    
    #ellipse(width/2 + cos(millis()*0.002) * 100, height/2 + cos(millis()*0.002) * 100, 40, 40) 
    #rect(mouseX - 40, height - 20, 80, 20)


def drawRacket():
    fill(255)
    global racketwidth, racketX, racketY, racketheight
    rect(racketX, racketY, racketwidth, 10) 
    racketX = mouseX - (racketwidth/2) 
    
    
    
    
def drawBall():
    global BallX, BallY, BallSpeedX, BallSpeedY, racketY
    circle(BallX, BallY, 2* BallRadius)
    
    BallX += BallSpeedX
    BallY += BallSpeedY 
    
    if(BallX+BallRadius > width):
        BallSpeedX *= -1
        BallX = width - BallRadius 
        
    elif(BallY+BallRadius > height):
        BallSpeedY *= -1
        BallY = height - BallRadius 
        
    if(BallY-BallRadius < 0):
        BallSpeedY *= -1
        BallY = BallRadius 
        
    elif(BallX-BallRadius < 0):
        BallSpeedX *= -1
        BallX = BallRadius 
        
    if(racketY < BallY-BallRadius < racketY + racketheight and BallSpeedY > 0):
        if(racketX < BallX < racketX + racketwidth):
            BallSpeedY *= -1 
            BallY = racketY - BallRadius
        
    
        
     
    
    
    
    
    
    
        
    
        
     
    

        
    
    
        
    
        
    
        

        
        
    
        
    

        
