
from pytube import YouTube

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

    print(yellow_bold+r"""                  ________   __            __        ______
             /  ______|  | |          /  \      |  ___ \            
            /  /   ____  | |         / /\ \     | |   | | 
            | |   |__ |  | |        / /__\ \    | |   | |
            | \_____| |  | |____   / /____\ \   | |___| |
             \________/  |______| / /      \ \  |______/         """)
    print("")
    print(blue_bold+"           ******************************************************")
    print(blue_bold+"           * Made by Hadinon                                    *")
    print(blue_bold+"           * find more tools on https://hadinon.itch.io         *")
    print(blue_bold+"           * https://gladnews.000webhostapp.com                 *")
    print(blue_bold+"           ******************************************************")
    print("")

    youtube_download()


slogan()

