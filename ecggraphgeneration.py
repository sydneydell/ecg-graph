import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import os
import sys
import scipy.signal as signal

fig, ax = plt.subplots()

# plot your ECG
def parse(filepath):
    # load input file
    input_data = np.loadtxt(filepath + "\ecg.txt")
    ecg_data = pd.DataFrame()

    # Bandpass filter the ECG signal (0.5-50 Hz)
    b, a = signal.butter(2, [0.5, 60], btype='bandpass', fs=200)
    ecg_data['Ch1'] = signal.filtfilt(b, a, input_data[:, 1])
    ecg_data['Ch2'] = signal.filtfilt(b, a, input_data[:, 2])
    ecg_data['Ch3'] = signal.filtfilt(b, a, input_data[:, 3])

    t = np.linspace(0, len(ecg_data) / 200, len(ecg_data), endpoint=False)

    # save plots of each position
    plot_save_ecg(ecg_data, t, 10, 20, filepath, "-supine")
    plot_save_ecg(ecg_data, t, 40, 50, filepath, "-sit")
    plot_save_ecg(ecg_data, t, 70, 80, filepath, "-twist")
    plot_save_ecg(ecg_data, t, 100, 110, filepath, "-stand")
    plot_save_ecg(ecg_data, t, 130, 140, filepath, "-arms")


def plot_save_ecg(ecg_data, t, starttime, endtime, filepath, suffix):
    ts = np.linspace(0, 10, 200*10, endpoint=False)
    data = ecg_data.iloc[200*starttime:(200*endtime)]

    # Create a figure with three subplots
    fig, axs = plt.subplots(3, 1, figsize=(21, 7))

    for channel in range(3):
        # plot each graph on its own subplot
        axs[channel].plot(ts, (data.iloc[:, channel] / 1000), color='black')
        axs[channel].set_title('Channel ' + str(channel + 1))
        axs[channel].set_xlabel('Time (seconds)')
        axs[channel].set_ylabel('Millivolts')
        axs[channel].set_ylim(-1, 3)
        axs[channel].grid(True)

        # Set ticks
        major_ticks = np.arange(0, 10.1, 0.1)
        axs[channel].set_xticks(major_ticks)
        axs[channel].set_xticklabels([str(tick) if idx % 10 == 0 else '' for idx, tick in enumerate(major_ticks)])
        axs[channel].set_xticks(np.arange(0, 10, 0.02), minor=True)  # Minor ticks for every 0.02 seconds
        axs[channel].set_yticks(np.arange(-1, 2.6, 0.5))  # Major ticks for every 0.5 mV
        axs[channel].set_yticks(np.arange(-1, 2.5, 0.1), minor=True)  # Minor ticks for every 0.1 mV

        # Turn on the minor ticks on
        axs[channel].minorticks_on()

        # Make the major grid
        axs[channel].grid(which='major', linestyle='-', color='#FF7F7F', linewidth='1.0')
        # Make the minor grid
        axs[channel].grid(which='minor', linestyle=':', color='#FF7F7F', linewidth='0.5')

        axs[channel].margins(x=0)

    # Save the plot as an image
    plt.tight_layout()

    #plt.show()
    plt.savefig(f"{filepath}{suffix}.png")

    # Close the plot to release resources
    plt.close()

def process(folder):
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        parse(file_path)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder>")
        sys.exit(1)

    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print("Error: Folder does not exist.")
        sys.exit(1)

    process(folder_path)
