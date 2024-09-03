# ECG Data Processing Script

This script processes ECG (Electrocardiogram) data stored in text files within a specified folder. It performs signal filtering, plots, and saves visualizations for different positions. Below is a breakdown of the script's functionality and usage.

## Features

- **ECG Data Processing**: The script reads ECG data from text files and applies a bandpass filter to the signals.
- **Plot Generation**: It generates plots for different positions (supine, sit, twist, stand, arms) based on the filtered ECG signals.
- **Customizable**: Users can specify the folder containing the ECG data files as a command-line argument.

## Requirements

- Python 3.x
- NumPy
- Pandas
- Matplotlib
- SciPy

## Usage

```bash
python script.py <folder_path>
```

## Script Overview

- **parse(filepath)**: 
    - Loads the ECG data from the specified file.
    - Applies a bandpass filter to the ECG signals.
    - Calls `plot_save_ecg()` to generate and save plots for different positions.

- **plot_save_ecg(ecg_data, t, starttime, endtime, filepath, suffix)**: 
    - Generates subplots for each channel of the ECG data.
    - Sets titles, labels, ticks, and grid for each subplot.
    - Saves the plots as image files with specified suffixes.

- **process(folder)**: 
    - Processes all files in the specified folder.
    - Calls `parse()` for each file found in the folder.

- **Main Execution**:
    - Checks if the correct number of command-line arguments is provided.
    - Verifies if the specified folder exists.
    - Calls `process()` to begin processing the ECG data files.

## Notes

- Ensure that the ECG data files are properly formatted and contain the necessary information.
- Adjust the bandpass filter parameters (`[0.5, 60] Hz`) as needed for specific signal characteristics.
- The script generates plot images for each position within the specified folder.
- Comment out or modify the `plt.show()` line if you prefer to display plots interactively.
- This script assumes that the ecg.txt files to plot are located within folders all in the main folder specified. Edit the parse function to change this.


