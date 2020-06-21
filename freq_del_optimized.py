#Author - Sumanth Govind (sumanth.govind@sprint.com)
#DO NOT EDIT THIS FILE

import enmscripting
from getpass import getpass
import sys

"""user_name = input('ENM User Name: ')
user_password = getpass('ENM User Password: ')"""

user_name='n30864oc'
user_password='Keyboard123!'

try:
    session = enmscripting.open('https://syl9launcher.syl9enm1.mgmt/').with_credentials(enmscripting.UsernameAndPassword(str(user_name),str(user_password)))
except (NameError,ValueError):
    sys.exit("Invalid Login/Connectivity to ENM failed")
channel = input("Enter Frequency to be deleted: ")
#channel_type = input("Is the above channel FDD or TDD: ").upper()
if int(channel)<10000:
    channel_type ='FDD'
else:
    channel_type='TDD'

"""coll_or_node = input("Enter Collection name or Node name: ")"""

coll_or_node='TPA'

def freq_del(inputt):
    response = session.terminal().execute(inputt)
    for line in response.get_output():
        if "FDN" in line:
            inputt='cmedit delete ' +line.replace("FDN : ","")+ ' -ALL'
            #print(inputt)
            response = session.terminal().execute(inputt)
            print(response.get_output()) 

def idlemoderel(user_input):
    response = session.terminal().execute(user_input)
    for line in response.get_output():
        if "FDN" in line:
            user_input = 'cmedit set '+line.replace("FDN : ","")+' idleModePrioAtReleaseRef=""'
            #print(user_input)
            response = session.terminal().execute(user_input)
            print(response.get_output())

def idelmodedel(user_input2):
    response=session.terminal().execute(user_input2)
    for line in response.get_output():
        if "FDN" in line:
            user_input2='cmedit delete ' +line.replace("FDN : ","")
            #print(user_input2)
            response = session.terminal().execute(user_input2)
            print(response.get_output())
            

#idlemoderel('cmedit get '+str(coll_or_node)+' EUtranCellFDD.idleModePrioAtReleaseRef')
#idelmodedel('cmedit get '+str(coll_or_node)+' IdleModePrioAtRelease')
freq_del('cmedit get '+str(coll_or_node)+' EUtranFreqRelation='+str(channel))
freq_del('cmedit get '+str(coll_or_node)+' ExternalEUtranCell'+str(channel_type)+'.eutranFrequencyRef==*'+str(channel))
freq_del('cmedit get '+str(coll_or_node)+' EUtranFrequency='+str(channel))

enmscripting.close(session) 