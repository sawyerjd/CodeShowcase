$ExchangeServer = "qp-mailboxb2010.qperf.test"
#$UserCredential = Get-Credential
$pw = convertto-securestring -AsPlainText -Force -String testing
$cred = new-object -typename System.Management.Automation.PSCredential -argumentlist "qperf\administrator",$pw
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri "http://$ExchangeServer/PowerShell/" -Authentication Kerberos -Credential $cred
Import-PSSession $Session

Search-Mailbox -Identity "Connectadmin" -DeleteContent -Force
Search-Mailbox -Identity "connect_email" -DeleteContent -Force

Remove-PSSession $Session

Read-Host "Emails cleared, press any key to exit..."
exit
