import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate discrete white noise signal
num_samples = 1000  # Number of signal points
mean = 0  # Mean
std_deviation = 1  # Standard deviation

# Generate white noise signal
white_noise = np.random.normal(mean, std_deviation, num_samples)

# Step 2: Statistical analysis
signal_mean = np.mean(white_noise)
signal_variance = np.var(white_noise)

# Step 3: Plot signal, autocorrelation, and PSD separately
time = np.arange(0, num_samples)

# Plot the white noise signal
plt.figure(figsize=(8, 4))
plt.plot(time, white_noise)
plt.title('Generated White Noise Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

# Plot autocorrelation function
autocorrelation = np.correlate(white_noise, white_noise, mode='full')
lags = np.arange(-num_samples + 1, num_samples)
plt.figure(figsize=(8, 4))
plt.plot(lags, autocorrelation)
plt.title('Autocorrelation Function')
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.show()

# Calculate and plot the Power Spectral Density (PSD)
frequencies = np.fft.fftfreq(num_samples)
fft_values = np.fft.fft(white_noise)
psd = np.abs(fft_values) ** 2

# Plot Power Spectral Density (PSD)
plt.figure(figsize=(8, 4))
plt.plot(frequencies, psd)
plt.title('Power Spectral Density (PSD)')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.xlim(0, 0.5)  # Show only positive frequencies
plt.show()

# Output statistical analysis results
print(f"Signal Mean: {signal_mean}")
print(f"Signal Variance: {signal_variance}")
