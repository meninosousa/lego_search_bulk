# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 18:47:30 2016

@author: Sousaadm
"""

import webbrowser

#url = 'http://www.python.org/'
#
## Open URL in a new tab, if a browser window is already open.
#
#
#
#
#webbrowser.open_new_tab(url + 'doc/')
#
#webbrowser.open_new(url)

urls = ['https://www.fr.ricardo.ch/search/index/?SearchSentence=lego+','http://www.anibis.ch/fr/advertlist.aspx?fts=lego+']


sets = [8366,5600,5599,8475,8376,8184,4589,8675,8183,8369,8378,8676]

for each_set in sets:
    for each_url in urls:
        webbrowser.open_new_tab(each_url + str(each_set))
