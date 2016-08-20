# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 18:47:30 2016

@author: Sousaadm
"""

import webbrowser
import sys

urls = ['https://www.fr.ricardo.ch/search/index/?SearchSentence=lego+','http://www.anibis.ch/fr/advertlist.aspx?fts=lego+']

sets_rc = [4589,5599,5600,8366,8369,8376,8378,8475,8675,8676,'rc']
sets_super = [853,956,8070,8145,8448,8466,8653,8860,8865,8880,42056,'super',5218]
sets_control = [8485,8094,'control']



def openner():
    option = int(input('1_rc, 2_super, 2_control, 4_exit. pls choice: '))
    sets = []

    if option == 1:
        sets = sets_rc

    elif option == 2:
        sets = sets_super

    elif option == 3:
        sets = sets_control

    elif option == 4:
        sys.exit()

    else:
        print('not an option')
        openner()

    for each_set in sets:
         for each_url in urls:
             webbrowser.open_new_tab(each_url + str(each_set))
    openner()
   
def main():
    openner()
    
    
if __name__ == "__main__":
    main()
