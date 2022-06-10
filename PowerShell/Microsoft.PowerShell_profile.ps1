Set-Alias -name l -value ls
$Scripts="C:\Users\{UserID}\AppData\Local\Microsoft\WindowsApps\"
Set-PSReadlineKeyHandler -Key Ctrl+d -Function DeleteCharOrExit
