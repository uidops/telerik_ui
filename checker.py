# -*- coding: UTF-8 -*-

import urllib.request
import sys
import urllib.error
from urllib.parse import urlparse
import os

class color : 
   GREEN = '\033[92m'
   RED = '\033[91m'
   WHITE = '\033[0m'

class reverse_ip:
    def __init__(self,website):
        a = urlparse(website).netloc
        if a=='':
            a = urlparse(website).path
        else:
            pass
        print("check site: [%s]"%(a))
        try:
            test_l = urllib.request.urlopen('http://%s'%(a))
            print ("success with code (%d)" %(test_l.code))
        except urllib.error.URLError:
            print("site is not available")
        print("Preparing to find sites")
        irl = urllib.request.urlopen("https://api.hackertarget.com/reverseiplookup/?q=%s"%(a))
        #print("Sites:")
        detail = irl.read() #; print(detail.decode('utf-8'))
        if 'error check your search parameter' in detail.decode('utf-8') or "No DNS A records found for" in detail.decode("utf-8"):
            print("no site found!")
            sys.exit(0)
        print('\033[0m'"%d site found" %(len(detail.decode('utf-8').split('\n'))))
        file_j = open("jet_%s.txt"%(a),'w')
        file_j.write(detail.decode('utf-8'))
        file_j.close()
        print("saved to %s/jet_%s.txt"%(os.getcwd(),a))
        sys.exit('\n')

class tester:
    def __init__(self,file_w):
        try:
            file_j = open(file_w,'r')
            sites = file_j.readlines()
        except FileNotFoundError:
            print("Error: File not found")
            sys.exit(0)
        print ("'\033[0m'%d site found in %s"%(len(sites),file_w))
        dork = "/DesktopModules/Admin/RadEditorProvider/DialogHandler.aspx"
        g_sites = []
        for site in sites:
            try:
                site_u = 'http://%s%s'%(site.strip(),dork)
                test_l = urllib.request.urlopen(site_u)
                print ("[%d] %s" %(test_l.code,site_u))
                if test_l.code==200:
                    if 'Loading the dialog'.upper() in test_l.read().decode('utf-8').upper():
                        print("'\033[92m' **** [exploitable] %s "%(site_u))
                        g_sites.append(site_u)
            #except urllib.error.URLError or urllib.error.HTTPError:
                    #print("%s is not available"%(site_u))
            except:
                    print("'\033[91m'[Error/404] %s"%(site_u))
        print('\033[0m'"Done ...")
        file_name = "sites_%s" %(file_w)
        file_l = open(file_name,'w')
        file_l.write("\n".join(g_sites))
        file_l.close()
        print('\033[0m'"Exploitable sites saved in %s"%(file_name))
        sys.exit("\n")
       
       
if __name__ == '__main__':
    help = """
		
	 usage:
		python3 jet.py i http://site.com
		python3 jet.py f jet_site.com.txt
		
"""
    if len(sys.argv)<3:
        print(help)
        sys.exit(0)
    if sys.argv[1]=='i':
        reverse_ip(sys.argv[2])
    elif sys.argv[1]=='f':
        tester(sys.argv[2])
    else:
        print(help)
else:
    sys.exit(0)
        
