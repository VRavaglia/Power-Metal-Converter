from __future__ import unicode_literals
#https://ffmpeg.org/ - ffmpeg video converter
#https://pypi.python.org/pypi/ffmpy - ffmpeg python command line wrapper
import ffmpy
#https://rg3.github.io/youtube-dl/ - youtubedl video downloader
import youtube_dl
import os
import datetime

#File with the urls of videos to be converted placed in the working directory.
url_file = 'urls.txt'
#Destination folder path, change it to desired path, as default it will use the working directory.
#Windows pattern: 
#dest_path = 'C:\\Users\\User\\Desktop\\'
dest_path = os.getcwd()

if os.path.exists(os.getcwd() + '\\' + url_file):
    with open(os.getcwd() + '\\' + url_file) as f:
        urls = f.readlines()

    for u in range(0, len(urls)):

        divisions = []
        titles = []

        url = urls[u]

        #Downloads information about the video including the video itself

        ydl = youtube_dl.YoutubeDL({'outtmpl': '%(title)s.%(ext)s','format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]})
        with ydl:
            video = ydl.extract_info(
                url,
                download=True
            )

        print  ('\nConverting: ' + video['title'] + '...\n')

        #Converts the full description into usable timestamps, used to split it into single tracks.
        #This will only work with the pattern used in the "Power Metal Collection" videos but can be changed
        #to work with other videos.

        timestamps = video['description']
        timestamps_lines =  timestamps.splitlines()

        for i in range(4, len(timestamps_lines)):
            line_contents = timestamps_lines[i].split()
            if len(line_contents) > 0:
                if line_contents[0].isdigit():
                    divisions.append(line_contents[len(line_contents)-1])
                    titles.append('')
                    for j in range(1, (len(line_contents) -1)):
                        titles[i-4] = titles[i-4] + line_contents[j] + ' '
                    titles[i - 4] = titles[i - 4][:-1].title()

        divisions.append(str(datetime.timedelta(seconds=video['duration'])))

        if not os.path.exists(dest_path + video['title']):
            os.makedirs(dest_path + video['title'])

        for i in range(0, (len(divisions) - 1)):
            print('\n'+titles[i]+': '+ divisions[i]+' to ' + divisions[i+1])

        #Splits the video into multiple files.
        for i in range(0, (len(divisions) -1)):
            ff = ffmpy.FFmpeg(
                inputs={video['title']+'.mp3': None},
                outputs={dest_path + video['title']+'\\' + titles[i]+'.mp3': '-ss '+divisions[i]+' -to '+divisions[i+1]+' -async 1'}
            )
            ff.run()

        os.remove(os.getcwd()+'\\'+video['title']+'.mp3')
    print('\n\nFinished converting.')    
else:
    print('No url file, please create one named: ' + url_file + ' in the working directory.')

