@echo off
goto :init

:help
    echo (You must run this in the current directory where the main.py is)
    echo Usage: "runGodScript.bat [options]"
    echo    -f        Target file to run
    echo    -h        Show this prompt
    echo    -git      Show the link to the github page
    echo    --debug   Show the debug log
    echo.
    goto :end

:show_git
    echo This is the github page:
    echo    https://github.com/FirefoxyLeGibus/god-script
    goto :end

:missing_file
    echo File specified not found.
    goto :end

:run_script
    echo Trying to run "%~1"
    if not exist %~1 call :missing_file & goto :end

    if /i "%~2" == "--debug" py main.py %~1 & py log_debug.py & goto :end
    py main.py %~1 & goto:end
    goto :end

:missing_argument
    echo Missing argument, See usage for running this thing.
    goto :end

:parse
    if "%~1"=="" call :missing_argument & goto :end

    if /i "%~1"=="-h"    call :help     & goto :end
    if /i "%~1"=="/h"    call :help     & goto :end
    if /i "%~1"=="?"     call :help     & goto :end
    if /i "%~1"=="-git"  call :show_git & goto :end
    if /i "%~1"=="/git"  call :show_git & goto :end

    @REM Show debug stacktrace
    if /i "%~1" == "--debug" py log_debug.py & goto :end

    @REM Running a gsc program
    if "%~2"==""         call :missing_argument & goto :end
    if /i "%~1"=="/f"    call :run_script %~2 %~3 & goto :end
    if /i "%~1"=="-f"    call :run_script %~2 %~3 & goto :end
    GOTO end

:init
    echo.
    echo == WELCOME TO GODSCRIPT FELLOW CULTIST ==
    echo.
    goto :parse

:end