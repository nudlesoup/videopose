from scipy.io import loadmat
D = loadmat("/home/nudlesoup/Research/datasets/Real_Dataset/Annotations/Set3/Ego_0/Ego_0_fc7.mat")
print(D.keys())
print(D['__globals__'])