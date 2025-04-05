@echo off
echo [INFO] Disconnecting old ADB connections...
adb disconnect

echo [INFO] Setting device to TCP/IP mode on port 5555...
adb tcpip 5555

echo [INFO] Waiting for device to initialize...
timeout /t 3 > nul

echo [INFO] Getting device IP address...
FOR /F "tokens=2" %%G IN ('adb shell ip addr show wlan0 ^| find "inet "') DO set ipfull=%%G
FOR /F "tokens=1 delims=/" %%G in ("%ipfull%") DO set ip=%%G

echo [INFO] Connecting to device at %ip%...
adb connect %ip%

REM Optional: Restart ADB server
adb kill-server
adb start-server

REM Optional: Launch Chrome with YouTube
echo [INFO] Launching Chrome with YouTube...
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" https://www.youtube.com

REM Optional: Launch Google
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" https://www.google.com

pause
