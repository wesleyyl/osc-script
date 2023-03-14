@echo off


set /p input= Number of Runs:

FOR %%runs IN (0, 1, %input%) DO "/usr/bin/python3.8/python.exe" "/home/wesleyluk/oscillator/evolution/evolution/batchrun.py"


