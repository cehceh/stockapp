@ECHO OFF
# Open development environment so you must use --settings 
# open command, activate env and run the project 
start cmd.exe /k "D:\Django\win_envs\salesenv\Scripts\activate && cd D:\Django\projects\stock\stockapp\kmastock\ && python manage.py runserver 0.0.0.0:8010 --settings=kmastock.settings.development"

# open Opera browser on windows 10
start C:\Users\Root\AppData\Local\Programs\Opera\launcher.exe "http://localhost:8010" 

       