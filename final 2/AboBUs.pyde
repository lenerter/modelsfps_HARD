x=0
g=0
u=0
h=0
l=0
i = 0
c1=0
c2=0
c3=0
c=0
def setup():
    global i
    size(2000,1000)
    noStroke()
    background(255)
    frameRate(120000000)
def draw():
    global x, g, h, u, i ,l,c,c1,c2,c3
    background(255)
    i = loadImage("lox.jpg")
    fill(0)
    rect(200,200,400,400)
    rect(800,200,400,400)
    rect(500,600,400,400)
    if c1 == 0:
        fill(255,255,0)
        rect(610,400,180,180)
    fill(125)
    rect(500,0,400,200)
    fill(random(0,255),random(0,255),random(0,255))
    rect(x,g,100,100)
    textSize(40)
    text(c,100,100)
    if x+100 > 500 and x < 900 and g+100 > 600 and g < 900:
        l=1
    if x+100 > 200 and x < 600 and g+100 > 200 and g < 600:
        l=1
    if x+100 > 800 and x < 1200 and g+100 > 200 and g < 600:
        l=1
    if x+100 > 610 and x < 790 and g+100 > 400 and g < 580:
        if c < 1:
            c1=1
    if key == CODED:
        if keyCode == UP: 
            g-=2
        if keyCode == LEFT:
            x-=2
        if keyCode == RIGHT:
            x+=2
        if keyCode == DOWN:
            g+=2
    if c1 == 1:
        c+=1
        c1=2
    if c2 == 1:
        c+=1
        c2=2
    if c3 == 1:
        c+=1
        c3=2
    if c == 3:
        l=0                   #win
    if key == 'r':
        x=0
        g=0
        l=0
        c=0
        c1=0
        c2=0
        c3=0
    if l == 1:
        image(i,0,0,2000,1000)
