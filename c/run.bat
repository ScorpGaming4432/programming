@ECHO off
CLS
TITLE jestem kurwa haker
:2
IF %errorlevel%==2 ECHO Chosen "N", looping...
SET /p TCCLOCATION=Set the tcc.exe file location (by default "E:\infos\tcc-0.9.27\tcc.exe"): 
IF /i "%TCCLOCATION%"=="" (
    ECHO No TCCLOCATION given, defaulting to "E:\infos\tcc-0.9.27\tcc.exe"
    SET TCCLOCATION="E:\infos\tcc-0.9.27\tcc.exe"
)
SET /p ARGS=Which args? 
CHOICE /M "Run %TCCLOCATION% -run %1 %ARGS%?"
CLS
GOTO %errorlevel%
:1
ECHO Running %TCCLOCATION% -run %1 %ARGS%...
%TCCLOCATION% -run %1 %ARGS%
PAUSE