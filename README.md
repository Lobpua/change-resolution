for Russian-speaking users [Документация на русском](README_RU.md)

# Screen Resolution Switcher with QRes

This Python script uses `QRes.exe` to automatically switch between two screen resolutions and refresh rates based on the current display setting. If the screen is set to `1920x1080`, it will switch to `1440x1080` (or vice versa) with the specified refresh rate. This is helpful for quickly toggling between custom display modes without needing to adjust settings manually.

## Requirements

- **Python 3.x**: Make sure Python is installed. You can download it from [python.org](https://www.python.org/downloads/).
- **QRes.exe**: Download `QRes.exe` from SourceForge: [QRes on SourceForge](https://sourceforge.net/projects/qres/files/).
  
## Installation

1. **Download the Script**:

   - Click on the green "Code" button in this repository.
   - Choose "Download ZIP" and save the ZIP file to your computer.
   - Extract the ZIP file to a folder of your choice.

2. **Install QRes.exe**:

   - Download `QRes.exe` from [this SourceForge link](https://sourceforge.net/projects/qres/files/) and save it to a known location.
   - Make sure to note the full path to `QRes.exe`, as you’ll need it for the script configuration.

## Setup

1. **Specify the Path to QRes.exe**:
   
   - Open the script file (`qres.pyw`) in a text editor.
   - Replace `QRES_PATH` with the full path to `QRes.exe` on your system:
   
     ```python
     QRES_PATH = r"C:\path\to\QRes.exe"
     ```

2. **Adjust Resolution and Refresh Rate Settings**:

   - In the `toggle_resolution` function, you can customize the resolution and refresh rate. By default, the script toggles between `1920x1080` and `1440x1080` with a refresh rate of `165Hz`. Modify these values as needed:
   
     ```python
     set_resolution(1440, 1080, 165)
     set_resolution(1920, 1080, 165)
     ```

## Usage

1. **Run the Script**: 

   - Double-click on the `qres.pyw` script file to execute it. This will trigger an automatic resolution switch based on the current screen resolution.

2. **Note on NVIDIA Control Panel Configuration** (for custom resolutions):

   If you don’t see a custom resolution (like `1440x1080`) after running the script, you may need to create this resolution in the NVIDIA Control Panel:

   - Open the **NVIDIA Control Panel**.
   - Go to **Display > Change Resolution**.
   - In the **Change Resolution** window, click on **Customize** below the list of resolutions.
   - In the **Customize** window, check **Enable resolutions not exposed by the display**.
   - Click **Create Custom Resolution**.
   - Modify ONLY these fields in the **Display Mode (as reported by Windows)** section:
     - **Horizontal pixels**
     - **Vertical lines**
     - **Refresh rate (Hz)**
   - After setting the fields, click **Test**. Once validated, your custom resolution will appear in the list, making it usable by `QRes`.

## Important Notes

- **Supported Resolutions**: If `QRes` doesn’t switch to a specified resolution, ensure the resolution is supported by both your monitor and graphics card settings.
- **Custom Resolutions**: Some custom resolutions may need to be created manually (as described above) in the graphics settings for `QRes` to recognize them.
- **Laptops**: Often some laptops do not have a **Display > Change Resolution** section, usually this section appears when the monitor is connected.

## License

This project is licensed under the MIT License.
