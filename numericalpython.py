import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr)
print(type(arr))

goals = np.array([5,2,8,6,2,9])
print("Most Goals: ", np.max(goals))
print("Least Goals: ",np.min(goals))
print("Total Goals: ",np.sum(goals))
print("Average Goals: ",np.mean(goals))
print("Increasing Goals: ",np.sort(goals))
print("Decreasing Goals: ",np.sort(goals)[::-1])