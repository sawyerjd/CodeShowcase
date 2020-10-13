Do {

    Do {
	Set-ExecutionPolicy bypass
    clear-host
    Write-Host "
  ======================== 300 Campaign Controller ========================= 
  =                                                                       =
  =  1 = Start the campaigns                                              =
  =  2 = Pause the campaigns                                              =
  =  3 = Unpause the campaigns                                            =
  =  4 = Stop the campaigns                                               =
  =  5 = Exit                                                             =
  =                                                                       =
  =========================================================================" -foregroundcolor "green"

    $choice1 = read-host -prompt "Select an option and press enter"
    
    if ($choice1 -eq "5") {break}
    
    } until ($choice1 -eq "1" -or $choice1 -eq "2" -or $choice1 -eq "3" -or $choice1 -eq "4")

    Switch ($choice1) {

    ##################### Option 1 - Start Campaigns ###############################
    "1" {

        clear-host
        write-host ""
        write-host "Starting campaigns..." -foregroundcolor "yellow" 
        write-host ""

        Invoke-Expression "& `"D:\I3\IC\Server\CampaignController.exe`" revengeadmin 1234 campaign 1 300 1 1 start"
       
        write-host ""
        Write-Host -NoNewLine 'Campaigns ' 
        write-host -NoNewLine 'started! ' -foregroundcolor "green" 
        write-host ""
        write-host 'Press any key to return to the menu...';
        $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown');


    } # End main menu option 1

    ############################### Option 2 - Pause campaigns ####################################

    "2" {
        
        clear-host
        write-host ""
        write-host "Pausing campaigns..." -foregroundcolor "yellow"
        write-host ""

        Invoke-Expression "& `"D:\I3\IC\Server\CampaignController.exe`" revengeadmin 1234 campaign 1 300 1 1 pause"
                    
        write-host ""
        Write-Host -NoNewLine 'Campaigns ' 
        write-host -NoNewLine 'paused! ' -foregroundcolor "green" 
        write-host ""
        write-host 'Press any key to return to the menu...';
        $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown');
        
        } # end main menu option 2
            

    ##################### Option 3 - Unpause campaigns ###############################

    "3" {
    
        clear-host
        write-host ""
        write-host "Unpausing campaigns..." -foregroundcolor "yellow"
        write-host ""

        Invoke-Expression "& `"D:\I3\IC\Server\CampaignController.exe`" revengeadmin 1234 campaign 1 300 1 1 unpause"
        
        write-host ""
        Write-Host -NoNewLine 'Campaigns ' 
        write-host -NoNewLine 'unpaused! ' -foregroundcolor "green" 
        write-host ""
        write-host 'Press any key to return to the menu...';
        $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown');
           
        } # End main menu option 3
    
    ##################### Option 4 - Stop campaigns ###############################
        
    "4" {
    
        clear-host
        write-host ""
        write-host "Stopping campaigns..." -foregroundcolor "yellow"
        write-host ""

        Invoke-Expression "& `"D:\I3\IC\Server\CampaignController.exe`" revengeadmin 1234 campaign 1 300 1 1 stop"
        
        write-host ""
        Write-Host -NoNewLine 'Campaigns ' 
        write-host -NoNewLine 'stopped! ' -foregroundcolor "green" 
        write-host ""
        write-host 'Press any key to return to the menu...';
        $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown');    
    
        
        } # End main menu option 4
    
    } # end main menu switch
    
} while ($choice1 -ne "5") 
