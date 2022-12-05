import pathlib 
import matplotlib.pyplot as plt 
import numpy as np

A=10 
xmin= -5.12
xmax= 5.12
dx=   0.1



def f(x):     
    return A + x**2 - A*np.cos(2*np.pi*x) 


x=np.arange(xmin,xmax+dx,dx)
y=f(x)
    
res = pathlib.Path("results") 
res.mkdir(exist_ok=True) 
file = res / "results.txt" 

with file.open("w") as f: 
    for a, b in zip(x, y): 
        f.write(f"{a}    {b}\n") 

plt.plot(x, y) 
plt.grid() 
plt.savefig("results/results.png")
plt.show()