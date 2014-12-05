#!/usr/bin/python
import re
from os import listdir, makedirs, link, walk
from os.path import isdir,isfile


torrent_directory = '/mnt/multimedia/tri/'
file_list = listdir(torrent_directory)
#file_list = listdir('/mnt/multimedia/torrent')
TV_show_directory = ('/mnt/multimedia/Serie_TV/')

for f in file_list:
    m = re.search('^(.+)(\.| | - )[Ss]?(\d{1,2})([eE]|[Xx])(\d{2}).+\.(mkv|mp4|avi)',f)
        if m:
            folder = ''.join((TV_show_directory,m.group(1),'/S',m.group(3),'/'))
            if not isdir(folder):
                makedirs(folder)
            dst= ''.join((folder,m.group(0)))
        src = ''.join((torrent_directory,'/',f))
        print(src,' ',dst)
        if not isfile(dst):
            link(src,dst)