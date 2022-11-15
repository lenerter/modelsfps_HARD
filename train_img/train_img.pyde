x=0
g=0

def setup():
    size(2000,1000)
    background(255)
    frameRate(1200)
def draw():
    global x, g
    background(255)
    translate(x,g)
    fill(55,99,0)
    rect(100,100,200,100)
    fill(0)
    ellipse(150,200,50,50)
    ellipse(250,200,50,50)
    rect(110,10,10,90)
    fill(0,50,105)
    rect(170,10,90,90)
    x+=1
    g+=0.5
    if x == 2000:
        x=0
    if g == 2000:
        g=0 
    
