#!/usr/bin/python
import re
from os import listdir, makedirs, link, walk, rename
from os.path import isdir,isfile


cam_directory = '/home/poclement/Dropbox/Camera Uploads'
file_list = listdir(cam_directory)
archive_directory = ('/home/poclement/Dropbox/Images/Archive_Camera')

for f in file_list:
    m = re.search('^(\d{4}-\d{2})-\d{2} \d{2}\.\d{2}\.\d{2}\.(jpg|jpeg|png|mp4)$',f)
    if m:
        folder = ''.join((archive_directory,'/',m.group(1),'/'))
        if not isdir(folder):
            makedirs(folder)
        dst= ''.join((folder,m.group(0)))
        src = ''.join((cam_directory,'/',f))
        print(src,' ',dst)
        if not isfile(dst):
            rename(src,dst)
