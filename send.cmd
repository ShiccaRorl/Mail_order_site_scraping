echo %date%
echo %time%
 
set yyyy=%date:~0,4%
set mm=%date:~5,2%
set dd=%date:~8,2%
 
set time2=%time: =0%
 
set hh=%time2:~0,2%
set mn=%time2:~3,2%
set ss=%time2:~6,2%
 
set filename=%yyyy%-%mm%-%dd%_%hh%-%mn%-%ss%
 
rem echo test >> log_%filename%.txt

del .\資料*.*


.\..\tool\7z\7za.exe a  .\資料_%filename%.7z .\資料\ -r -paniki1119 -w.\ -ssc -ssw -mx=9 -mfb=128 -y
.\..\tool\7z\7za.exe a -v20m .\資料_%filename%.7z .\send_mail.py -r -paniki1119 -w.\ -ssc -ssw -mx=9 -mfb=128 -y
.\..\tool\7z\7za.exe a -v20m .\資料_%filename%.7z .\send.cmd -r -paniki1119 -w.\ -ssc -ssw -mx=9 -mfb=128 -y


python send_mail.py


copy /b .\資料_%filename%.zip.001 + .\資料_%filename%.zip.002 + .\資料_%filename%.zip.003 .\資料_%filename%.zip