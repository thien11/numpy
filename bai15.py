import numpy as np

scores = np.array([8, 6, 4, 3, 9, 4, 7, 4, 4, 9, 7, 3, 9, 4, 2, 3, 8, 5, 9, 6])

print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='lower'))
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='higher'))
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='linear'))
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='nearest'))
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='midpoint'))
#Bách phân vị thứ 70:  7
#Bách phân vị thứ 70:  8
#Bách phân vị thứ 70:  7.299999999999999
#Bách phân vị thứ 70:  7
#Bách phân vị thứ 70:  7.5