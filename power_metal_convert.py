from __future__ import unicode_literals
import ffmpy
import youtube_dl
import os
import datetime


with open(os.getcwd()+'\\urls.txt') as f:
    urls = f.readlines()

for u in range(0, len(urls)):
    #with open(os.getcwd()+'\\timestamps.txt') as f:
     #   timestamps = f.readlines()

    divisions = []
    titles = []

    #url = raw_input('Enter the video url')
    url = urls[u]

    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(title)s.%(ext)s','format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]})
    with ydl:
        video = ydl.extract_info(
            url,
            download=False
        )
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
                #print (i-3)
                titles[i - 4] = titles[i - 4][:-1].title()

    divisions.append(str(datetime.timedelta(seconds=video['duration'])))
    #print  (video['title']+'.mp3')
    #print (divisions[len(divisions)-1])
    if not os.path.exists('C:\\Users\\Victor\\Desktop\\' + video['title']):
        os.makedirs('C:\\Users\\Victor\\Desktop\\' + video['title'])
    for i in range(0, (len(divisions) - 1)):
        print(titles[i]+': '+ divisions[i]+' to ' + divisions[i+1])
    for i in range(0, (len(divisions) -1)):
        ff = ffmpy.FFmpeg(
            inputs={video['title']+'.mp3': None},
            outputs={'C:\\Users\\Victor\\Desktop\\'+video['title']+'\\'+titles[i]+'.mp3': '-ss '+divisions[i]+' -to '+divisions[i+1]+' -async 1'}
        )
        ff.run()
    os.remove(os.getcwd()+'\\'+video['title']+'.mp3')
