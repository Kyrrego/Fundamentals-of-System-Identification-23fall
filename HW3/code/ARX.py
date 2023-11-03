import numpy as np
from scipy.signal import lfilter
from sklearn.metrics import mean_squared_error

# 定义ARX模型的参数
a = np.array([1, -0.5, 0.2])  # 自回归部分的系数
b = np.array([0.5, 0.2])     # 外生输入部分的系数

# 模拟时间步长和输入信号
num_samples = 100
u = np.random.randn(num_samples)  # 随机输入信号

# 生成ARX系统的仿真数据
e = np.random.randn(num_samples)  # 随机误差信号
z = lfilter(b, a, u) + e  # 计算输出信号

# 计算一步最优预测信号
z_pred_arx = np.zeros_like(z)
for k in range(1, num_samples):
    y = lfilter(b, a, u[:k+1])
    z_pred_arx[k] = y[-1]

# 计算滞后预测信号
z_pred_lag = np.roll(z, -1)  # 使用滞后预测

# 计算均方误差
mse_arx = mean_squared_error(z, z_pred_arx)
mse_lag = mean_squared_error(z, z_pred_lag)

print("ARX模型的均方误差:", mse_arx)
print("滞后预测的均方误差:", mse_lag)

# 可以根据其他性能指标来进一步比较预测性能
