:loop

powershell -NoProfile -ExecutionPolicy Unrestricted .\to_Flask.ps1

timeout 1800
goto :loop