import numpy as np
import matplotlib.pyplot as plt

# 生成M序列
def generate_m_sequence(N):
    # 初始化状态寄存器（LFSR）
    register = np.ones(N)
    m_sequence = []

    for _ in range(2**N - 1):
        feedback_bit = register[0] ^ register[N - 1]
        m_sequence.append(register[-1])
        register = np.roll(register, -1)
        register[-1] = feedback_bit

    return np.array(m_sequence)

# 产生M序列
N = 5  # 寄存器长度
m_sequence = generate_m_sequence(N)

# 生成白噪声
num_samples = len(m_sequence)
white_noise = np.random.choice([0, 1], size=num_samples)

# 绘制M序列和白噪声
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
