import matplotlib.pyplot as plt
import numpy as np

xPoints = np.array([0,30,60,80])
yPoints = np.array([0,150,60,170])
nPoints = np.array([0,15,45,125])

plt.plot(xPoints, yPoints, linestyle= "dashed", color= "r", linewidth= "15")
plt.plot(nPoints, linestyle= "dotted", color="g", linewidth= "4")
plt.show()