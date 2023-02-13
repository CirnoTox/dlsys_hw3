# from needle.backend_ndarray.ndarray import NDArray
import needle as ndl
import needle.backend_ndarray.ndarray as ndarray
import numpy as np

nda=ndarray.NDArray(np.reshape(np.arange(1,10),(1,9)))
print('*'*60)
print(nda)
print(nda.permute((1,0)))
print(nda)