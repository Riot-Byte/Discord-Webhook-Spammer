@echo off
cls
title Run Webhook Spammer
color 0a

echo Install requests? (y/n)
set /p prompt=

if %prompt% == y goto yes
if %prompt% == n goto no
:yes
python3 -m pip install requests
python3 webhook-spammer.py

:no
python3 webhook-spammer.py