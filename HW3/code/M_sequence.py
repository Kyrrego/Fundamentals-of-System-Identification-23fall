import numpy as np
import matplotlib.pyplot as plt

def generate_m_sequence(register, feedback_taps):
    """Generate an M-sequence using a linear feedback shift register (LFSR)."""
    sequence = []
    for _ in range(2**len(register) - 1):
        feedback = sum(register[tap] for tap in feedback_taps) % 2
        sequence.append(register[-1])
        register = [feedback] + register[:-1]
    return sequence

# Define LFSR parameters for an example 7-bit LFSR
register_length = 7
feedback_taps = [0, 2, 3, 6]

# Generate M-sequence
initial_state = [1] * register_length  # Initial state, can be changed as needed
m_sequence = generate_m_sequence(initial_state, feedback_taps)

# Generate white noise with specified mean and standard deviation
num_samples = 1000
mean = 0
std_deviation = 1
white_noise = np.random.normal(mean, std_deviation, num_samples)

# Compute auto-correlation functions
m_sequence_auto_corr = np.correlate(m_sequence, m_sequence, mode='full')
white_noise_auto_corr = np.correlate(white_noise, white_noise, mode='full')

# Compute power spectra
m_sequence_power_spectrum = np.abs(np.fft.fft(m_sequence_auto_corr))
white_noise_power_spectrum = np.abs(np.fft.fft(white_noise_auto_corr))

# Plot M-sequence
plt.figure(figsize=(8, 4))
plt.plot(m_sequence, label='M-sequence')
plt.title('M-sequence')
plt.show()

# Plot White Noise
plt.figure(figsize=(8, 4))
plt.plot(white_noise, label='White Noise')
plt.title('White Noise')
plt.show()

# Plot M-sequence Auto-correlation
plt.figure(figsize=(8, 4))
plt.plot(m_sequence_auto_corr, label='M-sequence Auto-correlation')
plt.title('Auto-correlation of M-sequence')
plt.show()

# Plot White Noise Auto-correlation
plt.figure(figsize=(8, 4))
plt.plot(white_noise_auto_corr, label='White Noise Auto-correlation')
plt.title('Auto-correlation of White Noise')
plt.show()

# Plot M-sequence Power Spectrum
plt.figure(figsize=(8, 4))
plt.plot(m_sequence_power_spectrum, label='M-sequence Power Spectrum')
plt.title('Power Spectrum of M-sequence')
plt.show()

# Plot White Noise Power Spectrum
plt.figure(figsize=(8, 4))
plt.plot(white_noise_power_spectrum, label='White Noise Power Spectrum')
plt.title('Power Spectrum of White Noise')
plt.show()
