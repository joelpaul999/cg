import matplotlib.pyplot as plt
xc,yc,r1,r2=0,0,5,7
x1=0
y1=r1
x2=0
y2=r2
p1=1-r1
p2=1-r2
x_points=[]
y_points=[]

def draw(x,y):
    pts = [
        (xc+x,yc+y),
        (xc-x,yc-y),
        (xc+x,yc-y),
        (xc-x,yc+y),
        (xc+y,yc+x),
        (xc-y,yc-x),
        (xc+y,yc-x),
        (xc-y,yc+x)
    ]
    for px,py in pts:
        x_points.append(px)
        y_points.append(py)

while x1<=y1:
    draw(x1,y1)

    if p1<0:
        p1=p1+2*x1+3
    else:
        p1=p1+2*(x1-y1)+5
        y1=y1-1
    x1=x1+1

while x2<=y2:
    draw(x2,y2)

    if p2<0:
        p2=p2+2*x2+3
    else:
        p2=p2+2*(x2-y2)+5
        y2=y2-1
    x2=x2+1

plt.scatter(x_points,y_points,color="Green")
plt.title("MidPoint Circle Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.show()