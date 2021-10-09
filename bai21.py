import numpy as np

coins = np.random.choice([0, 1], size=1000, p=[0.2, 0.8])
print("% số lần tung được mặt ngửa: ", (coins == 0).mean() * 100)
print("% số lần tung được mặt úp: ", (coins == 1).mean() * 100)
#% số lần tung được mặt ngửa:  19.900000000000002
#% số lần tung được mặt úp:  80.10000000000001
