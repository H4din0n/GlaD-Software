
from pytube import YouTube
import os

#Creating video lists

no_colored = ""
white_bold = ""
blue_bold = ""
green_bold = ""
red_bold = ""
yellow_bold = ""


def youtube_download():

    global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

    print('')

    video_name = input(yellow_bold+'video_url> '+no_colored)

    print(yellow_bold+'')

    folder_name = input('folder_name> '+no_colored)
    print('')

    video_list = [video_name]

    #Looping through the list
    for i in video_list:

        try:

            yt = YouTube(i)
            print(green_bold+'Downloading Link: ' + i)
            print(green_bold+'Downloading video: ' + yt.streams[0].title)
        except:
            print(red_bold+"Connection Error")

         #filters out all the files with "mp4" extension
        stream = yt.streams.filter(res="360p").first()
        stream.download(folder_name)
    print(blue_bold+
        '[*] download finished')


def slogan():

    global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

    print(yellow_bold)

    os.system("figlet G l a D")
    print("")
    print(blue_bold+"******************************************************")
    print(blue_bold+"* Made by Hadinon                                    *")
    print(blue_bold+"* find more tools on https://github.com/H4din0n      *")
    print(blue_bold+"*                                                    *")
    print(blue_bold+"******************************************************")
    print("")
    #2e7dbc2ad6ffd4647b7435b5912126f415b365ab4372758a9eed4e82a3f0d63f

    youtube_download()

    


slogan()

