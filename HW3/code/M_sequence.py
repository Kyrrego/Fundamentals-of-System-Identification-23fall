import numpy as np
import matplotlib.pyplot as plt

# Generate M-sequence
def generate_m_sequence(N):
    # Initialize the state register (LFSR)
    register = np.array([1] * N, dtype=int)  # Initialize with binary values
    m_sequence = []

    for _ in range(2**N - 1):
        feedback_bit = register[0] ^ register[N - 1]
        m_sequence.append(register[-1])
        register = np.roll(register, -1)
        register[-1] = feedback_bit

    return np.array(m_sequence)

# Generate an M-sequence
N = 5  # Register length
m_sequence = generate_m_sequence(N)

# Generate white noise
num_samples = len(m_sequence)
white_noise = np.random.choice([0, 1], size=num_samples)

# Plot the M-sequence and white noise
time = np.arange(0, num_samples)

plt.figure(figsize=(12, 6))

plt.subplot(211)
plt.stem(time, m_sequence, linefmt='-b', markerfmt='ob', basefmt=' ')
plt.title('Generated M Sequence')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(212)
plt.stem(time, white_noise, linefmt='-g', markerfmt='og', basefmt=' ')
plt.title('Generated White Noise')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

#