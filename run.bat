@echo off
SETLOCAL

REM Define path to venv relative to this script
SET "VENV_DIR=.\venv"
SET "REQUIREMENTS_FILE=.\requirements.txt"

REM Check if venv exists, if not, create it
IF NOT EXIST "%VENV_DIR%\Scripts\activate.bat" (
    echo Creating virtual environment in %VENV_DIR%...
    python -m venv "%VENV_DIR%"
    IF ERRORLEVEL 1 (
        echo Nie udalo sie aktywowac wirtualnego srodowiska. Upewnij sie ze python, oraz modul venv sa dostepne.
        pause
        GOTO :EOF
    )
)

REM Aktywowanie wirtualnego srodowiska
echo Aktywowanie wirtualnego srodowiska...
CALL "%VENV_DIR%\Scripts\activate.bat"
IF ERRORLEVEL 1 (
    echo Nie udalo sie aktywowac wirtualnego srodowiska.
    pause
    GOTO :EOF
)

REM Install requirements if requirements.txt exists
IF EXIST "%REQUIREMENTS_FILE%" (
    echo Instalowanie/sprawdzanie wymaganych pakietow z %REQUIREMENTS_FILE%...
    pip install -r "%REQUIREMENTS_FILE%"
    IF ERRORLEVEL 1 (
        echo Nie udalo sie zainstalowac pakietow. Sprawdz polaczenie z internetem, i requirements.txt
        pip list
        pause
        GOTO :EOF
    )
) ELSE (
    echo Warning: requirements.txt nie zostalo znalezione. Pomijanie instalacji pakietow.
)

REM Run the Python script
echo Uruchamianie Steam Scraper...
python scraper.py

REM Koniec dzialania
echo.
echo Program zakonczyl dzialanie. Nacisnij dowolny klawisz, aby zakonczyc...
pause >nul

ENDLOCAL
:EOF