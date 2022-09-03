#bloco da função:
  #def é para funções e sua declaração
  def parabola(x, a, b, c):
      par = a*x**2 + b*x + c
      return par
#Bloco principal:
  import matplotlib.pyplot as plt
  import numpy as np
  x = np.linspace (-2, 2, 10)
  y = parabola(x, 2, 1, 1)
  plt.plot (x, y, linewidth = 2, color = 'orange', linestyle = 'dashed')
  plt.plot (x, parabola(x, -2, 1, 3), color = 'lightblue', linestyle = 'dotted')
  plt.xlabel ('eixo x'), plt.ylabel('eixo y')
