@echo off
setlocal

title Instalador e Executor - Projeto Python

echo ==========================================
echo     INSTALADOR E EXECUTOR AUTOMATICO
echo ==========================================
echo.

REM ==============================
REM Encontrar Python
REM ==============================

where py >nul 2>&1

if %errorlevel%==0 (
    set "PY=py"
    goto PYTHON_OK
)

where python >nul 2>&1

if %errorlevel%==0 (
    set "PY=python"
    goto PYTHON_OK
)

echo [ERRO] Python nao encontrado!
echo.
echo Instale Python 3.11 ou superior:
echo https://www.python.org/downloads/windows/
echo.
pause
exit /b 1


:PYTHON_OK

echo [OK] Python encontrado:
%PY% --version
echo.


REM ==============================
REM Criar ambiente virtual
REM ==============================

if not exist ".venv" (

    echo [1/4] Criando ambiente virtual...

    %PY% -m venv .venv

    if errorlevel 1 (
        echo [ERRO] Falha ao criar ambiente virtual.
        pause
        exit /b 1
    )

) else (

    echo [1/4] Ambiente virtual ja existe.

)

echo.


REM ==============================
REM Atualizar pip
REM ==============================

echo [2/4] Atualizando pip...

call ".venv\Scripts\python.exe" -m pip install --upgrade pip

if errorlevel 1 (
    echo [ERRO] Falha ao atualizar pip.
    pause
    exit /b 1
)

echo.


REM ==============================
REM Instalar dependencias
REM ==============================

echo [3/4] Instalando dependencias...

if not exist "requirements.txt" (
    echo [ERRO] requirements.txt nao encontrado!
    pause
    exit /b 1
)

call ".venv\Scripts\python.exe" -m pip install -r requirements.txt

if errorlevel 1 (
    echo [ERRO] Falha ao instalar dependencias.
    pause
    exit /b 1
)

echo.

REM ==============================
REM Executar projeto
REM ==============================

echo [4/5] Iniciando projeto...
echo.
echo ==========================================
echo             PROJETO INICIADO
echo ==========================================
echo.

".venv\Scripts\python.exe" main.py


REM ==============================
REM Abrir dashboard
REM ==============================

echo.
echo [5/5] Abrindo dashboard...

if exist "dashboard_percepcao.html" (
    start "" "dashboard_percepcao.html"
) else (
    echo [AVISO] dashboard_percepcao.html nao encontrado!
)

echo.
echo ==========================================
echo              FINALIZADO
echo ==========================================
echo.

pause
