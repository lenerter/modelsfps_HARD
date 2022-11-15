x=500
g=200

d=200
f=500

h=800
m=500

def setup():
    size(2000,1000)
    background(255)
    frameRate(1200)
def draw():
    global x, g, d, f, h, m
    background(255)
    fill(0)
    triangle(x,g,d,f,h,m)
    x+=1
    g+=1
    d+=1
    f-=1
    h-=1
    m+=1
    if x == 2000:
        x=500
        g=200
    if d == 2000:
        d=200
        f=500
    if h == 2000:
        h=800
        m=500

    
