#!/usr/bin/env python3

import csv
import xml.etree.cElementTree as ET
from xml.etree.ElementTree import Element, SubElement
from xml.etree import ElementTree
from xml.dom import minidom

# Node server login parameters
nodeserver = 'NodeServer'
sqlserver = 'SQLServer'
nodeserverport = '3030'
sqlusername = 'username'
sqlpassword = 'password'
sqldbname = 'SimRunner'

# Campaign login parameters
finishagentratio = '0.3'
skillratio = '0.5'
simskill = 'SimSkill'
gridsratio = '0'
clconnectionid = '{A0000000-0000-0000-0000-000000000000}'
cltablename = 'newstuff'
cldispname = 'newstuff'
ccid = '5'

# Campaign logoff parameters
timetologout = '1800'  # seconds until sim ends

# Disposition parameters
scalefactor = '60'
extension = '40903'

def main():

    csvdatafile = csv.DictReader(open('test.csv'))
    for row in csvdatafile:

        id = row['campaignid']
        setname = row['behaviorsetname']

        behaviorset = Element('BehaviorSet', {'name': setname})  # top level of BehaviorSet    TODO: populate name from file?

        # Start of sequential activities
        sequential = SubElement(behaviorset, 'Sequential', {'loop': 'false'})   # Sequential activities tag for BehaviorSet

        # Node Server Login Activity
        nodelogin = SubElement(sequential, 'SequentialActivity', {'lang': 'js',   # SequentialActivity tag for node server login
                                                                  'type': 'ClientJS.dialer.icScripter-startSimSessionId',
                                                                  'name': 'logging sim session id onto server',
                                                                  'num_loops': '1',
                                                                  'min_delay_before_execution': '5',
                                                                  'max_delay_before_execution': '5',
                                                                  'repeat': 'false'})

        nodelogin_conf = SubElement(nodelogin, 'ConfigData')  # ConfigData tag for node server login

        nodelogin_conf_nodehostname = SubElement(nodelogin_conf, 'nodeServerHostName')  # Node Server Hostname
        nodelogin_conf_nodehostname.text = nodeserver

        nodelogin_conf_nodeport = SubElement(nodelogin_conf, 'nodeServerPortNo')   # Node Server Port Number
        nodelogin_conf_nodeport.text = nodeserverport

        nodelogin_conf_sqlhost = SubElement(nodelogin_conf, 'sqlServerHostName')  # SQL Server Hostname
        nodelogin_conf_sqlhost.text = sqlserver

        nodelogin_conf_sqlusername = SubElement(nodelogin_conf, 'sqlServerUserName')  # SQL Server Username
        nodelogin_conf_sqlusername.text = sqlusername

        nodelogin_conf_sqlpass = SubElement(nodelogin_conf, 'sqlServerPassword')  # SQL Server Password
        nodelogin_conf_sqlpass.text = sqlpassword

        nodelogin_conf_sqldbname = SubElement(nodelogin_conf, 'sqlServerDatabaseName')  # SQL Server DB Name
        nodelogin_conf_sqldbname.text = sqldbname

        # Setup Scripter Session Activity
        SubElement(sequential, 'SequentialActivity', {'lang': 'js',   # SequentialActivity tag for scripter session setup
                                                      'type': 'ClientJS.dialer.icScripter-initSession',
                                                      'name': 'Setup Scripter Session',
                                                      'num_loops': '1',
                                                      'min_delay_before_execution': '5',
                                                      'max_delay_before_execution': '5',
                                                      'repeat': 'false'})

        # Campaign Login Activity
        campaignlogin = SubElement(sequential, 'SequentialActivity', {'lang': 'js',   # SequentialActivity tag for campaign login
                                                                      'type': 'ClientJS.dialer.icScripter-campaignLogin',
                                                                      'name': 'Login to Campaign',
                                                                      'num_loops': '1',
                                                                      'min_delay_before_execution': '20',
                                                                      'max_delay_before_execution': '30',
                                                                      'repeat': 'false'})

        campaignlogin_conf = SubElement(campaignlogin, 'ConfigData')   # ConfigData tag for campaign login

        campaignlogin_conf_id = SubElement(campaignlogin_conf, 'CampaignID')  # Login campaign ID
        campaignlogin_conf_id.text = id  # TODO: this needs to be poulated from CSV somehow

        campaignlogin_conf_finishratio = SubElement(campaignlogin_conf, 'FinishingAgentRatio')   # Finishing agent ratio
        campaignlogin_conf_finishratio.text = finishagentratio

        campaignlogin_conf_skillratio = SubElement(campaignlogin_conf, 'SkillRatio')   # Skill ratio
        campaignlogin_conf_skillratio.text = skillratio

        campaignlogin_conf_skillname = SubElement(campaignlogin_conf, 'SkillName')   # Skill name
        campaignlogin_conf_skillname.text = simskill

        campaignlogin_conf_gridsratio = SubElement(campaignlogin_conf, 'GridsAgentRatio')   # Grids agent ratio
        campaignlogin_conf_gridsratio.text = gridsratio

        campaignlogin_conf_clid = SubElement(campaignlogin_conf, 'contactListConnectionId')   # Contact list connection ID
        campaignlogin_conf_clid.text = clconnectionid

        campaignlogin_conf_cltablename = SubElement(campaignlogin_conf, 'contactListTableName')   # Contact list table name
        campaignlogin_conf_cltablename.text = cltablename

        campaignlogin_conf_cldispname = SubElement(campaignlogin_conf, 'contactListDisplayName')   # Contact list display name
        campaignlogin_conf_cldispname.text = cldispname

        # Campaign logoff activity
        campaignlogoff = SubElement(sequential, 'SequentialActivity', {'lang': 'js',  # SequentialActivity tag for campaign logoff
                                                                       'type': 'ClientJS.dialer.icScripter-campaignLogout',
                                                                       'name': 'campaignLogoff',
                                                                       'num_loops': '1',
                                                                       'min_delay_before_execution': timetologout,
                                                                       'max_delay_before_execution': timetologout,
                                                                       'repeat': 'false'})

        campaignlogoff_conf = SubElement(campaignlogoff, 'ConfigData')

        campaignlogoff_conf_id = SubElement(campaignlogoff_conf, 'CampaignId')   # Logoff campaign ID
        campaignlogoff_conf_id.text = id   # TODO: this needs to populate from CSV somehow

        # Set available activity
        setavailable = SubElement(sequential, 'SequentialActivity', {'lang': 'js',  # SequentialActivity tag for set available
                                                                     'type': 'ClientJS.dialer.icScripter-setStatus',
                                                                     'name': 'Set Available',
                                                                     'num_loops': '1',
                                                                     'min_delay_before_execution': '30',
                                                                     'max_delay_before_execution': '30',
                                                                     'repeat': 'false'})

        setavailable_conf = SubElement(setavailable, 'ConfigData')    # ConfigData tag for set available activity

        setavailable_conf_status = SubElement(setavailable_conf, 'Status')   # Set status to available
        setavailable_conf_status.text = 'Available'

        # Teardown scripter session activity
        SubElement(sequential, 'SequentialActivity', {'lang': 'js',
                                                      'type': 'ClientJS.dialer.icScripter-teardownSession',
                                                      'name': 'Teardown Scripter Session',
                                                      'num_loops': '1',
                                                      'min_delay_before_execution': '1200',
                                                      'max_delay_before_execution': '1200',
                                                      'repeat': 'false'})

        # Submit sim stats activity
        SubElement(sequential, 'SequentialActivity', {'lang': 'js',
                                                      'type': 'ClientJS.dialer.icScripter-submitSimStats',
                                                      'name': 'submit Sim Stats',
                                                      'num_loops': '1',
                                                      'min_delay_before_execution': '1',
                                                      'max_delay_before_execution': '1',
                                                      'repeat': 'false'})

        # Stop logging to Node server activity
        SubElement(sequential, 'SequentialActivity', {'lang': 'js',
                                                      'type': 'ClientJS.dialer.icScripter-endSimSessionId',
                                                      'name': 'stopping logging of sim session id onto server',
                                                      'num_loops': '1',
                                                      'min_delay_before_execution': '5',
                                                      'max_delay_before_execution': '5',
                                                      'repeat': 'false'})
        # End sequential activities

        # Start triggered activities
        triggered = SubElement(behaviorset, 'Triggered')

        # Disposition triggered activity
        disposition = SubElement(triggered, 'TriggeredActivity', {'lang': 'js',
                                                                  'type': 'ClientJS.dialer.icScripter-breakAndDisposition',
                                                                  'name': 'Break and Disposition',
                                                                  'trigger_discriminator': 'dispositionRandomTrigger',
                                                                  'trigger_type': 'ININ.SimRunner.JavaScriptPlugin.JavaScriptTrigger',
                                                                  'num_loops': '1'})

        disposition_conf = SubElement(disposition, 'ConfigData')   # ConfigData tag for disposition activity

        disposition_conf_scale = SubElement(disposition_conf, 'ScaleFactor')   # Scale factor tag
        disposition_conf_scale.text = scalefactor

        disposition_conf_extension = SubElement(disposition_conf, 'WorkgroupExtension')   # Workgroup extension tag
        disposition_conf_extension.text = extension

        disposition_conf_id = SubElement(disposition_conf, 'CampaignId')   # Campaign ID tag for disposition activity
        disposition_conf_id.text = id   # TODO: this needs to populate from CSV somehow

        disposition_conf_finishratio = SubElement(disposition_conf, 'FinishingAgentRatio')   # Finishing agent ratio for disposition activity
        disposition_conf_finishratio.text = finishagentratio

        # print(prettyxml(behaviorset))

        xmlstr = minidom.parseString(ET.tostring(behaviorset)).toprettyxml(indent="   ")
        with open('output.xml', 'a') as f:
            f.write(xmlstr)

def prettyxml(elem):
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


if __name__ == '__main__': main()
