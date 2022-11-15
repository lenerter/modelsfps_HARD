x=500
g=500

def setup():
    size(1000,1000)
    background(255)
    frameRate(1200)
def draw():
    global x, g
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(x,x,50,50)
    ellipse(g,g,50,50)
    ellipse(g,x,50,50)
    ellipse(x,g,50,50)
    x+=1
    g-=1
