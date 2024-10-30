import os
import subprocess

# Укажите полный путь к QRes.exe
QRES_PATH = r"C:\путь\к\файлу\QRes.exe"

def get_current_resolution():
    output = subprocess.check_output(
        "wmic path Win32_VideoController get CurrentHorizontalResolution,CurrentVerticalResolution", shell=True
    )
    output = output.decode().splitlines()
    # Извлечение текущего разрешения экрана
    for line in output:
        if line.strip() and "CurrentHorizontalResolution" not in line:
            resolution = line.split()
            print(f"Текущее разрешение: {resolution[0]}x{resolution[1]}")
            return int(resolution[0]), int(resolution[1])

def set_resolution(width, height, refresh_rate):
    try:
        command = f'"{QRES_PATH}" /x:{width} /y:{height} /r:{refresh_rate}'
        print(f"Выполняем команду: {command}")
        os.system(command)
    except Exception as e:
        print(f"Ошибка: Не удалось сменить разрешение: {str(e)}")

def toggle_resolution():
    current_width, current_height = get_current_resolution()

    if current_width == 1920 and current_height == 1080:
        print("Переключаемся на 1440x1080")   # Укажите нужное разрешение и частоту обновления
        set_resolution(1440, 1080, 165)
    elif current_width == 1440 and current_height == 1080:
        print("Переключаемся на 1920x1080")
        set_resolution(1920, 1080, 165)     # Укажите нужное разрешение и частоту обновления
    else:
        print("Неизвестное текущее разрешение, переключение не требуется.")

# Запуск автоматического переключения при запуске
toggle_resolution()
