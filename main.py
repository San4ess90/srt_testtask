import os
import platform
import time
import pyautogui

def open_calculator():
    """
    Открывает приложение "Калькулятор" в зависимости от операционной системы.
    """
    system = platform.system()
    if system == "Windows":
        os.system("start calc")
    elif system == "Linux":
        os.system("gnome-calculator &")  # Для GNOME. Замените на другой калькулятор, если используете KDE/XFCE.
    elif system == "Darwin":
        os.system("open -a Calculator")
    else:
        raise OSError("Операционная система не поддерживается")
    time.sleep(2)

def perform_calculation():
    """
    Автоматически выполняет сложение 12 + 7 с использованием pyautogui.
    """
    try:
        images = {
            "1": "images/1.png",
            "2": "images/2.png",
            "7": "images/7.png",
            "+": "images/plus.png",
            "=": "images/equal.png",
        }

        for key in ["1", "2", "+", "7", "="]:
            button_location = pyautogui.locateOnScreen(image=images[key], confidence=0.95)
            if button_location:
                pyautogui.click(pyautogui.center(button_location))
                time.sleep(0.5)
            else:
                print(f"Кнопка '{key}' не найдена на экране. Проверьте изображение.")
                return

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    try:
        open_calculator()
        perform_calculation()
    except OSError as e:
        print(f"Ошибка: {e}")
