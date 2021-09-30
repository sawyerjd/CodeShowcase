#####################################################################################
# This script searches the uninstall registry keys to see if Wireshark is installed #
# and if it is an older version than 3.0, uninstalls it                             #
#####################################################################################

$regPathWireshark = "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Wireshark"
$regTestWireshark = Test-Path $regPathWireshark
$regPathWinpcap = "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\WinPcapInst"
$regTestWinpcap = Test-Path $regPathWinpcap

# Test to see if wireshark is installed and up to date, if not up to date, uninstall it
if ($regTestWireshark){

    $regValueWireshark = Get-ItemProperty -Path $regPathWireshark | select-object -ExpandProperty DisplayVersion

    if ($regValueWireshark -lt 3){
    
        $uninstallPathWireshark = Get-ItemProperty -Path $regPathWireshark | select-object -ExpandProperty UninstallString
        $silentUninstallWireshark = $uninstallPathWireshark + " /S"

        Invoke-Expression "& $silentUninstallWireshark"
        #Invoke-Expression "& '\\path\to\wireshark\install' /S"
    
    }
}

# Test to see if WinPcap is installed and remove it if it is
#if ($regTestWinpcap){
##
#    $uninstallPathWinpcap = Get-ItemProperty -Path $regPathWinpcap | select-object -ExpandProperty UninstallString
#
#    Invoke-Expression "& '$uninstallPathWinpcap' \S"
#
#}
