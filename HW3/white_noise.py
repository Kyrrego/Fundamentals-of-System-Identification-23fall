import numpy as np
import matplotlib.pyplot as plt

# 步骤1：生成离散白噪声信号
num_samples = 1000  # 生成的信号点数
mean = 0  # 均值
std_deviation = 1  # 标准差

# 生成白噪声信号
white_noise = np.random.normal(mean, std_deviation, num_samples)

# 步骤2：统计分析
signal_mean = np.mean(white_noise)
signal_variance = np.var(white_noise)

# 步骤3：绘制信号图和自相关函数图
time = np.arange(0, num_samples)
plt.figure(figsize=(10, 8))

# 绘制信号图
plt.subplot(311)
plt.plot(time, white_noise)
plt.title('Generated White Noise Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

# 绘制自相关函数图
plt.subplot(312)
autocorrelation = np.correlate(white_noise, white_noise, mode='full')
lags = np.arange(-num_samples + 1, num_samples)
plt.plot(lags, autocorrelation)
plt.title('Autocorrelation Function')
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')

# 步骤4：计算并绘制功率谱密度函数
plt.subplot(313)
frequencies = np.fft.fftfreq(num_samples)
fft_values = np.fft.fft(white_noise)
psd = np.abs(fft_values) ** 2  # 功率谱密度函数

# 绘制功率谱密度函数
plt.plot(frequencies, psd)
plt.title('Power Spectral Density (PSD)')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.xlim(0, 0.5)  # 只显示正频率部分
plt.tight_layout()

plt.show()

# 输出统计分析结果
print(f"Signal Mean: {signal_mean}")
print(f"Signal Variance: {signal_variance}")
