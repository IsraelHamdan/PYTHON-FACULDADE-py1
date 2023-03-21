import numpy as np 
import matplotlib as mat 

np.random.seed(1)
dados = np.random.standard_normal(loc = 20, scale = 2, size = 1000)
mat.hist(dados, color = "lightblue", ec="red")


