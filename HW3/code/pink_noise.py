import numpy as np
import matplotlib.pyplot as plt

# 产生白噪声（White Noise）信号
num_samples = 1000
mean = 0
std_deviation = 1

white_noise = np.random.normal(mean, std_deviation, num_samples)

# 产生粉红噪声（1/f Noise）信号
pink_noise = np.cumsum(white_noise)

# 计算自相关函数
lags = np.arange(-num_samples + 1, num_samples)
white_autocorrelation = np.correlate(white_noise, white_noise, mode='full')
pink_autocorrelation = np.correlate(pink_noise, pink_noise, mode='full')

# 计算功率谱密度函数（PSD）
frequencies = np.fft.fftfreq(num_samples)
white_fft_values = np.fft.fft(white_noise)
pink_fft_values = np.fft.fft(pink_noise)
white_psd = np.abs(white_fft_values) ** 2 
pink_psd = np.abs(pink_fft_values) ** 2 

# 绘制白噪声的自相关函数
plt.figure(figsize=(8, 6))
plt.plot(lags, white_autocorrelation)
plt.title('White Noise Autocorrelation Function')
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.show()

# 绘制粉红噪声的自相关函数
plt.figure(figsize=(8, 6))
plt.plot(lags, pink_autocorrelation)
plt.title('Pink Noise Autocorrelation Function')
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.show()

# 绘制白噪声的时域图
plt.figure(figsize=(8, 6))
plt.plot(np.arange(0, num_samples), white_noise)
plt.title('White Noise Time Domain Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

# 绘制粉红噪声的时域图
plt.figure(figsize=(8, 6))
plt.plot(np.arange(0, num_samples), pink_noise)
plt.title('Pink Noise Time Domain Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

# 绘制白噪声的功率谱密度函数
plt.figure(figsize=(8, 6))
plt.plot(white_psd)
plt.title('White Noise Power Spectral Density (PSD)')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.xlim(0, 0.5)
plt.show()

# 绘制粉红噪声的功率谱密度函数
plt.figure(figsize=(8, 6))
plt.plot(frequencies, pink_psd)
plt.title('Pink Noise Power Spectral Density (PSD)')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.xlim(0, 0.5)
plt.show()
