

rem cd 実行するプログラムの階層
rem call C:\\Users\\ban\\anaconda3\\Scripts\\activate.bat
call C:\\Users\\user\\anaconda3\\Scripts\\activate.bat

:loop

python Flask_index.py

rem powershell sleep 5

goto :loop