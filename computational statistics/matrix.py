import numpy as np
arr2D=np.array([[1,3,5],[2,4,6],[3,5,7]])
arr1D=np.array([1,2,3,])
result=arr2D+arr1D
scalar=5
result2=scalar*arr2D
arr3D=np.array([[[1,3,5],[2,4,6]],[[3,5,7],[1,3,5]]])
arr1D=np.array([1,2,3,])
result3=arr3D+arr1D
print("Broadcasted Addition result1\n",result)
print("Broadcasted Scalar Multiplication result\n",result2)
print("Broadcasted Addition result2\n",result3)