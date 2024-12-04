import os
import platform
import time
import pyautogui


def open_calculator():
    '''
    Открывает приложение 'Калькулятор' в зависимости от операционной системы.
    '''
    system = platform.system()
    if system == 'Windows':
        os.system('start calc')
        user_system = 'windows'
    elif system == 'Linux':
        os.system('gnome-calculator &')  # Для GNOME. Замените на другой калькулятор, если используете KDE/XFCE.
        user_system = 'linux'
    elif system == 'Darwin':
        os.system('open -a Calculator')
        user_system = 'macos'
    else:
        raise OSError('Операционная система не поддерживается')

    time.sleep(2)
    return user_system


def perform_calculation(user_system):
    """
    Автоматически выполняет сложение 12 + 7 с использованием pyautogui.
    """
    try:
        # Используем переменную user_system для формирования путей
        images = {
            '1': f'images/{user_system}/1.png',
            '2': f'images/{user_system}/2.png',
            '7': f'images/{user_system}/7.png',
            '+': f'images/{user_system}/plus.png',
            '=': f'images/{user_system}/equal.png',
        }

        for key in ['1', '2', '+', '7', '=']:
            button_location = pyautogui.locateOnScreen(image=images[key], confidence=0.95)
            if button_location:
                pyautogui.click(pyautogui.center(button_location))
                time.sleep(0.5)
            else:
                print(f"Кнопка '{key}' не найдена на экране. Проверьте изображение.")
                return

    except Exception as e:
        print(f'Ошибка: {e}')


if __name__ == '__main__':
    try:
        user_system = open_calculator()
        perform_calculation(user_system)
    except OSError as e:
        print(f'Ошибка: {e}')
