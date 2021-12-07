
rem cd C:\\Users\\user\\Downloads\\バックアップ\\プログラム\\Chrome拡張\\Mail_order_site_scraping\\config\\stock\\source\\
rem cd R:\\L\Program\\Chrome拡張\\スクレイピング通販サイト\\Mail_order_site_scraping\\config\\stock\\source
rem cd Z:\\L\\Program\\Chrome拡張\\Mail_order_site_scraping\\GUI\\在庫管理\\

cd C:\\Users\\user\\Downloads\\バックアップ\\プログラム\\Chrome拡張\\Mail_order_site_scraping\\GUI\\在庫管理\\

call C:\\tools\\Anaconda3\\Scripts\\activate.bat
call C:\\Users\\user\\anaconda3\\Scripts\\activate.bat
call C:\\Users\\ban\\anaconda3\\Scripts\\activate.bat

rem call python ./za_Rakuma_test_002.py %1 %2
call python ./za_Rakuma_test.py %1 %2 > log.txt

pause