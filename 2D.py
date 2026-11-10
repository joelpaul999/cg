import matplotlib.pyplot as plt
import numpy as np
import math

triangle=np.array([
    [1,5],
    [3,6],
    [5,8],
    [1,5]
])

translated=triangle + [2,-1]
scaled=triangle * [2,2]
theta=math.radians(45)
R=np.array([
    [math.cos(theta),-math.sin(theta)],
    [math.sin(theta),math.cos(theta)]
])
rotated=triangle @ R.T
reflected=triangle * [1,-1]
fig,axs=plt.subplots(2,2,figsize=(10,8))
def draw(ax,transformed,title):
    ax.plot(triangle[:,0],triangle[:,1],'bo-',label="Original")
    ax.plot(transformed[:,0],transformed[:,1],'ro-',label="Transformed")
    ax.set_title(title)
    ax.grid(True)
    ax.axis("equal")
    ax.legend()
draw(axs[0,0],translated,"Translation")
draw(axs[0,1],scaled,"Scaling")
draw(axs[1,0],rotated,"Rotation")
draw(axs[1,1],reflected,"Reflection")
plt.tight_layout()
plt.show()
