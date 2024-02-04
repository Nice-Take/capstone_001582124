@echo off
start "Docker" cmd /c docker run -p 8000:80 nicetake/estimator:latest
timeout /t 2 /nobreak >nul
start "" ".\estimator.html"
