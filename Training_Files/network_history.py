import os
import re
import winreg
import codecs
from Registry.Registry import Registry



def network_history(reg_handle):
    reg_results=[]
    regkey=r"Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
    for eachsubkey in reg_handle.open(regkey).subkey():
        DefaultGatewayMac=eachsubkey.value("DefaultGatewayMac").value()
        BSSID=':'.join(codecs.encode(DefaultGatewayMac, "HEX").decode() [i:i+2] for i in range(0,12,2))
        Description=eachsubkey.value("Description").value()
        DnsSuffix=eachsubkey.value("DnsSuffix").value()
        SSID=eachsubkey.value("FirstNetwork").value()
        ProfileGuid=eachsubkey.value("ProfileGuid").value()
        nettype,first,last=get_profile_info(reg_handle, ProfileGuid)
        reg_results.append(BSSID,SSID,Description,DnsSuffix,nettype,first,last)
    return reg_results


def get_profile_info(reg_handle, ProfileGuid):
    nametype={'47':"Wireless", "06":"Wired", "17":"Broadband"}
    guid=r"{}".format(ProfileGuid)
    regkey=reg_handle.open(guid)
    NameType="%02x" % regkey.value("NameType").value()
    nettype=nametypes.get(str(NameType), "Unknown Type"+str(NameType))
    FirstConnect = reg_binary_date(regkey.value("DateCreated").value())
    LastConnect=reg_binary_date(regkey.value("DateLastConnected").value())
    return nettype, FirstConnect, LastConnect


def reg_binary_date(dateblob):
    weekday=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    year,mth,day,date,hr,min,sec,micro=struct.unpack('<8H', dateblob)
    dt="%s, %02/%02/%04d %02:%02:%02.%s" % (weekday[day],mth,date,year,hr,min,sec,micro)
    dtp=datetime.datetime.strptime(dt,"%A, %m/$d/%Y %H:%M:%S.%f")
    return dtp

reg_handle=Registry("SOFTWARE")


network_history(reg_handle)