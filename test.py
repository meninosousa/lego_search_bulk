# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 18:47:30 2016

@author: Sousaadm
"""

import webbrowser
import sys
import time

urls = ['https://www.fr.ricardo.ch/search/index/?SearchSentence=lego+',\
'http://www.anibis.ch/fr/advertlist.aspx?fts=lego+']

sets_rc = [4589,5599,5600,8366,8369,8376,8378,8475,8675,8676,'rc','racers']
sets_super = [853,956,8070,8145,8448,8466,8653,8860,8865,8880,42056,'super',
              5218]
sets_control = [8485,8094,'control']
sets_ms1 = [3800,3801,3803,3804,3805,8527,8528,8529,8547,9713,9719,9730,9731]
sets_ms2 = [9732,9735,9736,9738,9739,9747,9748,9749,9754,9755,9756,9757,9758]
sets_ms3 = [9798,9833,9841,9842,9843,9844,9845,9846,9847,9889,9911,10285,10286]
sets_ms4 = [10287,31313,45500,45502,45503,45504,45505,45506,45507,45508,45509]
sets_ms5 = [45517,2852724,2852725,2852726,2853216,2855040,4524081,'mindstorms']



def openner():
    option = int(input('1_rc, 2_super, 3_control, 4_8_mindstorms, 0_exit. pls choice: '))
    sets = []

    if option == 1:
        sets = sets_rc
    elif option == 2:
        sets = sets_super
    elif option == 3:
        sets = sets_control
    elif option == 4:
        sets = sets_ms1
    elif option == 5:
        sets = sets_ms2
    elif option == 6:
        sets = sets_ms3
    elif option == 7:
        sets = sets_ms4
    elif option == 8:
        sets = sets_ms5
    elif option == 0:
        sys.exit()
    else:
        print('not an option')
        openner()

    for each_set in sets:
        for each_url in urls:
            webbrowser.open_new_tab(each_url + str(each_set))
        time.sleep(1)
    openner()
   
def main():
    openner()
    
    
if __name__ == "__main__":
    main()
