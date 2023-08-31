# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 20:22:26 2023

@author: Highhh0
"""

import h5py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter 
# 读取MAT文件
mat_data = h5py.File('untitled.mat', 'r')

# variable_names = list(mat_data.keys())
# print(variable_names)

data = mat_data['ans']
numpy_array = np.array(data)
VCtime=numpy_array[:,0]
VCdata=numpy_array[:,1]


plt.plot(VCtime,VCdata, 'k',linestyle='-',marker='.',label='test')    

# plt.grid(b=True)

x_major_locator=MultipleLocator(5)
y_major_locator=MultipleLocator(20)

ax=plt.gca()

ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)

plt.xlim(-0.1,21)
plt.ylim(-0.1,81)


plt.legend(loc='upper right',frameon=False,fontsize=20)
plt.xticks(size = 16)
plt.yticks(size = 16)
# plt.savefig("./new_result.tiff" , bbox_inches='tight',dpi=600)
plt.show()

