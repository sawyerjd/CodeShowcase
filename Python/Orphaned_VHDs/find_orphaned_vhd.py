import os

path = r"D:\Hyper-V"

vmdirectories = [each for each in os.listdir(path)] #search for the vm directories in the base path

for vmdirectory in vmdirectories:

    if os.path.isdir(path + "\\" + vmdirectory):

        vhdfolder = ""
        isvmfolder = [each for each in os.listdir(path + "\\" + vmdirectory)]

        if "Virtual Hard Disks" in isvmfolder:
            vhdfolder = "\\Virtual Hard Disks"

        #search the vm directory for virtual hard disk files
        vhdfilenames = [each for each in os.listdir(path + "\\" + vmdirectory + vhdfolder) if (each.endswith('.avhd') or each.endswith('.avhdx') or each.endswith('.vhdx') or each.endswith('.vhd') )]
        orphans = [] #initialize a variable to store the orphaned filenames

        for vhdfilename in vhdfilenames: 

            snapconfigdirectory = "\\Snapshots"
            vmconfigdirectory = "\\Virtual Machines"        
            orphan_check = []

            if os.path.isdir(path + "\\" + vmdirectory + snapconfigdirectory):
            
                snapshotfolderfiles = [each for each in os.listdir(path + "\\" + vmdirectory + snapconfigdirectory) if (each.endswith('.xml') or each.endswith('.XML'))] #get names of xml files in snap dir
                
                #if os.path.isdir(path + "\\" + vmdirectory + snapconfigdirectory):
                for snapshotxml in snapshotfolderfiles:     
                    searchsnapfolder = open(path + "\\" + vmdirectory + snapconfigdirectory + "\\" + snapshotxml, "rb").read() #open the xml file as binary
                    mytext = searchsnapfolder.decode('utf-16') #convert the binary file to utf-16 so its readable
                    if vhdfilename in mytext:
                        #print("The virtual disk file " + vhdfilename + " is referenced in " + snapshotxml + " for vm " + vmdirectory )
                        orphan_check.append("True")

            if os.path.isdir(path + "\\" + vmdirectory + vmconfigdirectory):

                vmfolderfiles = [each for each in os.listdir(path + "\\" + vmdirectory + vmconfigdirectory) if (each.endswith('.xml') or each.endswith('.XML'))] # get names of xml files in VM directory
                            
                #if os.path.isdir(path + "\\" + vmdirectory + vmconfigdirectory):
                for vmxml in vmfolderfiles:
                    searchvmfolder = open(path + "\\" + vmdirectory + vmconfigdirectory + "\\" + vmxml, "rb").read()
                    vmxmltext = searchvmfolder.decode('utf-16')
                    if vhdfilename in vmxmltext:
                        #print("The virtual disk file " + vhdfilename + " is referenced in " + vmxml + " for vm " + vmdirectory)
                        orphan_check.append("True")

            #check to see if the orphan_check array is empty, if empty, the vhdfilename does not exist in any config files and is orpaned
            if not orphan_check:
                orphans.append(vhdfilename)

        if orphans:
            print("\nThe following files are orphaned for the VM " + vmdirectory + ":")
            for orphan in orphans:
                print(orphan)
