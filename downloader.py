# SAFE TEAM
# distributed under license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)

import argparse
import os
import sys
from subprocess import call

class Downloader:

    def __init__(self):

        self.apt_url = "https://drive.google.com/file/d/1t4_FS0_8DIPAyG5guGbK6UcJO52B5fRf/view?usp=sharing"
        self.base_path = "data"
        self.path_data = os.path.join(self.base_path, "")
        self.apt_compress_name='apt_data.tar.bz2'

    @staticmethod
    def download_file(id,path):
        try:
            print("Downloading from "+ str(id) +" into "+str(path))
            call(['./godown.pl',id,path])
        except Exception as e:
            print("Error downloading file at url:" + str(id))
            print(e)

    @staticmethod
    def decompress_file(file_src,file_path):
        try:
            call(['tar','-xvf',file_src,'-C',file_path])
        except Exception as e:
            print("Error decompressing file:" + str(file_src))
            print('you need tar command e b2zip support')
            print(e)

    def download(self):
        print('Making the godown.pl script executable, thanks:'+str('https://github.com/circulosmeos/gdown.pl'))
        call(['chmod', '+x','godown.pl'])
        print("SAFE --- downloading models")

        print("Downloading apt data.... in the folder data/")
        if not os.path.exists(self.path_data):
            os.makedirs(self.path_data)
        Downloader.download_file(self.apt_url, os.path.join(self.path_data,self.apt_compress_name))
        print("Decompressing data and placing in" + str(self.path_data))
        Downloader.decompress_file(os.path.join(self.path_data,self.apt_compress_name), self.path_data)

if __name__=='__main__':
    a=Downloader()
    a.download()