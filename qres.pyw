import os
import subprocess

# Specify the full path to QRes.exe
QRES_PATH = r"C:\path\to\QRes.exe"

def get_current_resolution():
    output = subprocess.check_output(
        "wmic path Win32_VideoController get CurrentHorizontalResolution,CurrentVerticalResolution", shell=True
    )
    output = output.decode().splitlines()
    # Extracting the current screen resolution
    for line in output:
        if line.strip() and "CurrentHorizontalResolution" not in line:
            resolution = line.split()
            print(f"Current resolution: {resolution[0]}x{resolution[1]}")
            return int(resolution[0]), int(resolution[1])

def set_resolution(width, height, refresh_rate):
    try:
        command = f'"{QRES_PATH}" /x:{width} /y:{height} /r:{refresh_rate}'
        print(f"Executing command: {command}")
        os.system(command)
    except Exception as e:
        print(f"Error: Failed to change resolution: {str(e)}")

def toggle_resolution():
    current_width, current_height = get_current_resolution()

    if current_width == 1920 and current_height == 1080:
        print("Switching to 1440x1080")   # Specify the desired resolution and refresh rate
        set_resolution(1440, 1080, 165)
    elif current_width == 1440 and current_height == 1080:
        print("Switching to 1920x1080")
        set_resolution(1920, 1080, 165)     # Specify the desired resolution and refresh rate
    else:
        print("Unknown current resolution, no switch needed.")

# Run automatic switching on startup
toggle_resolution()
