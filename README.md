#Power Metal Converter#

Python script made to donwload, convert and split youtube videos from [this](https://www.youtube.com/playlist?list=PL0hmqRkh_vnVn6i2kUYzvEQvppE2NFdWA) playlist.

This script uses [Youtube-dl](http://rg3.github.io/youtube-dl/) to download the video and its informations and [ffmpeg](http://ffmpeg.org/) to convert and split the files.

## Usage ##

* Requires Youtube-DL, ffmpeg and python 2.7 to work.

* Create a file named urls.txt in the same directory as the scrip with the desired videos to be converted
* Execute the script
* Change the dest_path variable to the desired destination of the output files
* Execute the script
* The script will then download, convert to mp3 and split the file into separated music files by tracks.
