@echo off
start python d.py
ping -n 6 127.1 >nul
start iexplore www.baidu.com