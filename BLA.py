import matplotlib.pyplot as plt
x1=int(input("Enter x1 "))
y1=int(input("Enter y1 "))
x2=int(input("Enter x2 "))
y2=int(input("Enter y2 "))
def drawline(x1,y1,x2,y2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    sx=1 if x2>x1 else -1
    sy=1 if y2>y1 else -1
    x=x1
    y=y1
    x_points=[]
    y_points=[]
    if dx>=dy:
        p=2*dy-dx
        while x!= x2:
            x_points.append(x)
            y_points.append(y)

            if p>=0:
                y+=sy
                p+=2*(dy-dx)
            else:
                p+=2*dy
            x+=sx

        x_points.append(x2)
        y_points.append(y2)

    else:
        p=2*dx-dy
        while y!=y2:
            x_points.append(x)
            y_points.append(y)

            if p>=0:
                x+=sx
                p+=2*(dx-dy)

            else:
                p+=2*dx
            y+=sy
        x_points.append(x2)
        y_points.append(y2)

    plt.scatter(x_points,y_points,color="Blue")
    plt.plot(x_points,y_points,color="Red")
    plt.title("Bresenham's Line Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid("True")
    plt.axis("equal")
    plt.show()

drawline(x1,y1,x2,y2)
