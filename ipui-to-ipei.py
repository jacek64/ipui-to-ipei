#debug
#ipui = '0370D46705'
#ipei = '14093 0288517 3'

import os, sys
from datetime import datetime

cwd = os.getcwd()
log_name = cwd + '\ipui-to-ipei.log'

while True:
    try:
        with open(log_name, mode="a", encoding="utf8") as log_file:
            ipui = input('Menu -> *#06# => IPUI \nIPUI: ')
            tel_name = input('Telphone name: ')
            now = datetime.now()
            if (len(ipui) == 10):
                emcHex = ipui[:5]
                psnHex = ipui[-5:]
                #print('EMC: %s | PSN: %s (hex)' % (emcHex, psnHex))
                emc = str(int(emcHex, 16)).zfill(5)
                psn = str(int(psnHex, 16)).zfill(7)
                #print('EMC: %s | PSN: %s (dec)' % (emc, psn))
                m = 1 #multiplier
                chksum = 0
                emcpsn = emc + psn
                for c in emcpsn:
                    chksum += int(c)*m
                    m += 1
                    #print('%s*%s' % (c,m))
                chkdgt = chksum % 11
                
                log_file.write('%s\n' % now.strftime('%Y-%m-%d %H:%M:%S'))
                log_file.write('Name: %s\n' % tel_name)
                log_file.write('IPUI: %s\n' % ipui)
                log_file.write('IPEI: %s %s %s\n\n' % (emc,psn,chkdgt))
                print('IPEI: %s %s %s' % (emc,psn,chkdgt))
                print('\n')
    except (KeyboardInterrupt, SystemExit):
        osCommandString = "notepad.exe " + log_name
        os.system(osCommandString)
        sys.exit()
