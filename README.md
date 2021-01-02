# song-looper

 Loops songs so that you dont have to smash the replay button everytime.

## Prerequisites

* [Download Python 3.7.4](https://www.python.org/downloads/release/python-374/)
* [Install tinytag](https://pypi.org/project/tinytag/)

## Usage

* Select a MP3 file from the "Choose file" button

* Provide the amount of times you want to loop the song. (If you want to match it to a certain time period you can watch the "Estimated File Length After Loop" to determine whether the song is long enough for your needs)

## Known issues

* The program doesnt parse files over 24 hours. 

> This is a deliberate restriction in place to prevent weird behavior. Feel free to fork and remove lines 57-59(the if statement that handles the limitation)

* The program can only handle MP3 files

> There are plenty of online converters out there for other formats and I found it quite meaningless to implement multiple format support.