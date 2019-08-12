import requests
import re
from pyfiglet import Figlet
import vlc
import time

# figlet font , text
def app_name():
    f = Figlet(font='isometric1')
    print(f.renderText("Music"))

# youtube Api_key , initialization

def app_name_stop():
    for j in range(100):
        print("\n")
    app_name()
    print('\n\n\n\n\n\n\n\n\n\n\n\n')

def vlc_player(url):
    print(url)
    instance = vlc.Instance('--novideo')
    media = instance.media_new(url)
    media_list = instance.media_list_new([url])
    player = instance.media_player_new() 
    player.set_media(media)
    list_player =  instance.media_list_player_new()
    list_player.set_media_player(player)
    list_player.set_media_list(media_list)
    
    player.play()    
    time.sleep(3)

def searchSong(song_name):

    # get Song Page
    print("ID\tTitle")
    page = requests.get('https://www.youtube.com/results?search_query=' + song_name)
    print('https://www.youtube.com/results?search_query=' + song_name)
    # get song Links
    urls = [] 
    video_id = re.findall(r'href=[\'"]/watch\?v=?([^\'" >&]+)', page.text)
    for i in range(0 , len(video_id) , 2):
        urls.append("https://www.youtube.com/watch?v=" + video_id[i])
        
    # get video title    
    title = re.findall(r'dir="ltr">[\'"]?([^\'">]+)</a>',  page.text)
    
    song_list = {}

    for i in range(10):
        print(str(i) + "\t" + title[i] + urls[i])

        song_list.update({title[i] : urls[i]})
    
    vlc_player(urls[1])



def start():
    print("Enter Song Name preceded by '.'")
    song_name = input()
    if(song_name[0] == '.'):
        searchSong(song_name)
    else:
        print('Query Error')

# show app name 
app_name()
start()