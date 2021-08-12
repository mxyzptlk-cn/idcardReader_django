@echo off
cd C:\Users\mxyzptlk\PycharmProjects\idcardReader_django\
start C:\Users\mxyzptlk\PycharmProjects\idcardReader_django\venv\Scripts\python.exe manage.py runserver
ping -n 6 127.1 >nul
start iexplore http://127.0.0.1:8000/index/