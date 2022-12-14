import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x, y, linewidth = 2, color = 'lightpink', linestyle = 'dashed')
plt.plot(x, y, linewidth = 0, color = 'darkblue', markersize = 3, marker = 's')
plt.xlabel('eixo x'), plt.ylabel('eixo y')
plt.title('f(x) = sin (x)')
plt.show()
