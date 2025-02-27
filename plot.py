# plot.py
import matplotlib.pyplot as plt

def plot_time_domain(pressure, start_idx, end_idx):

    time = range(start_idx, end_idx)  

    for index, p in enumerate(pressure):
        plt.plot(time, p[start_idx:end_idx], label=f'p_{index + 1}')

    plt.title('Pressure vs Time')
    plt.xlabel('Time')
    plt.ylabel('Air Pressure')

    plt.legend()

    plt.show()

def plot_frequency_domaine(freq, magnitude, start_freq, end_freq):

    plt.plot(freq[start_freq:end_freq], magnitude[start_freq:end_freq])  

    plt.title("Frequency Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")

    plt.show()

def plot_original_filtered(original, filtered):

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 1, 1)
    plt.plot(original)
    plt.title('Original Signal')
    plt.xlabel('Time')
    plt.ylabel('Pressure')
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(filtered)
    plt.title('Filtered Signal (keep 0.2-0.33 Hz and 1-1.67 Hz)')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid()

    plt.tight_layout()
    plt.show()