@echo off
REM Activate the virtual environment
CALL ".\venv\Scripts\activate.bat"

REM Run the Python script
echo Uruchamianie Steam Scraper...
python scraper.py

REM This line will make the window wait
echo.
echo Program zakonczyl dzialanie. Nacisnij dowolny klawisz, aby zakonczyc...
pause >nul