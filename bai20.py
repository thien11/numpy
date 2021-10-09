import numpy as np

coins = np.random.randint(2, size=1000)
print(coins.shape)
print("% số lần tung được mặt ngửa: ", (coins == 0).mean() * 100)
print("% số lần tung được mặt úp: ", (coins == 1).mean() * 100)
#% số lần tung được mặt ngửa:  49.5
#% số lần tung được mặt úp:  50.5
