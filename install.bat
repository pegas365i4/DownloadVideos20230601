@echo off

REM Создаем виртуальное окружение
python -m venv venv

REM Активируем виртуальное окружение
call venv\Scripts\activate.bat

REM Устанавливаем библиотеку pyautogui
pip install yt-dlp

REM Деактивируем виртуальное окружение
call venv\Scripts\deactivate.bat

REM Завершаем выполнение скрипта
exit
