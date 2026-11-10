import matplotlib.pyplot as plt
xc,yc,r=0,0,5
x=0
y=r
p=3-2*r
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

while x<=y:
    draw(x,y)

    if p<0:
        p=p+4*x+6
    else:
        p=p+4*(x-y)+10
        y=y-1
    x=x+1

plt.scatter(x_points,y_points,color="Blue")
plt.title("Bresenham's Circle Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.show()