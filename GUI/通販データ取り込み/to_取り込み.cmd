call C:\\Users\\user\\anaconda3\\Scripts\\activate.bat
call C:\\Users\\ban\\anaconda3\\Scripts\\activate.bat

:loop

python core.py

rem python directory_seed_アマゾン.py
rem python directory_seed_ストアーズ.py
python directory_seed_ヤフオク.py
python directory_seed_ラクマ.py
rem python directory_seed_楽天.py

rem timeout 1800
rem goto :loop