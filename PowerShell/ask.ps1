# Powershell test script
function Get-Response {
	[CmdletBinding()]
	param(
		[Parameter()]
		[string] $Prompt = "Do you want to continue (Y/N)"
	)
	
	$Response = Read-Host -Prompt $Prompt
    if ($Response -like "*y*") {
        return $true
    } else {
        return $false
    }
}

$Date = Get-Date
Write-Host "Date: '$Date'"

if (Get-Response -Prompt "Keep going") {
    Write-Host 'Okay'
} else {
    Write-Output "Stopped"
}

switch(Read-Host "Select a menu item"){
    1 {"File will be deleted"}
    2 {"File will be displayed"}
    3 {"File is write protected"}
    Yes {"You typed yes"}
    default {"Invalid entry"}
}
