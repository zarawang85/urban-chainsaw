import random
import matplotlib.pyplot as plt

x = [random.normalvariate(0,1) for i in range(100000)]
plt.hist(x, 50)
plt.show()
