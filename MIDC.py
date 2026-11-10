import matplotlib.pyplot as plt
xc,yc,r=0,0,5
x=0
y=r
p=1-r
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
        p=p+2*x+3
    else:
        p=p+2*(x-y)+5
        y=y-1
    x=x+1

plt.scatter(x_points,y_points,color="Green")
plt.title("MidPoint Circle Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.show()