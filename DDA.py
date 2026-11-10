import matplotlib.pyplot as plt
x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))
x2=int(input("Enter x2: "))
y2=int(input("Enter y2: "))
def dda_line(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    steps=max(abs(dx),abs(dy))
    xincr=dx/steps
    yincr=dy/steps
    x_points=[]
    y_points=[]
    x=x1
    y=y1
    for i in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x+=xincr
        y+=yincr
    plt.scatter(x_points,y_points,color="blue")
    plt.plot(x_points,y_points)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis("equal")
    plt.show()
dda_line(x1,y1,x2,y2)
