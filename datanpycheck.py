import numpy as np

import sys
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import glob

import numpy
numpy.set_printoptions(threshold=sys.maxsize)
filename='/home/nudlesoup/005BU.npz'
x = np.load(filename)
print(x.files)