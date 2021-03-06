import numpy as np

x = np.array([[14, 96],
               [46, 82],
               [80, 67],
               [77, 91],
               [99, 87]])
print("x = ", x)

print("Range = ", np.ptp(x))
print("Range (axis = 0) = ", np.ptp(x, axis=0))
print("Range (axis = 1) = ", np.ptp(x, axis=1))
#x =  [[14 96]
 #[46 82]
 #[80 67]
 #[77 91]
 #[99 87]]
#Range =  85
#Range (axis = 0) =  [85 29]
#Range (axis = 1) =  [82 36 13 14 12]