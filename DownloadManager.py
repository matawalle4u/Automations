"""
This Helps to arrange downloaded files
The Arrangement is done in this Format 
Year/Month/User/Category
Author Adam Mustapha
matawalle4u@gmail.com
+2349028163380
tweeter:@sudo_nigeria
"""

import json,os,getpass
from typing import List

class DownloadManager:

    def __init__(self):

        self.downloads = os.listdir(os.path.expanduser('~/Downloads'))
        self.user = getpass.getuser()
        self.shekara = 2020
        self.wata = 'December'
        
    
    def create_dir(self, item:str):
        
        """
        Create Directory if note exist
        """
        item= 'Films'

        new_dir = os.path.expanduser('~/Downloads/{}/{}/{}/{}'.format(self.shekara, self.wata, self.user, item))
        
        
        try:
            os.makedirs(new_dir)
            """
            create and move the files to their repective folders

            """
        except FileExistsError:
            """
            Move all the files 
            """
            print('Akwai folder din')
        
    

    
        
        
    
            
mn= DownloadManager()
mn.create_dir('Littafi')
#print(mn.downloads)