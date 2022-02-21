#pip install python-vlc

from vlc import Instance
import os

class VLC:
    def __init__(self):
        self.Player = Instance('--loop')

    def addPlaylist(self):
        self.mediaList = self.Player.media_list_new()
        path = r"C:/Users/ajays/Desktop/music"
        songs = os.listdir(path)
        for s in songs:
            self.mediaList.add_media(self.Player.media_new(os.path.join(path,s)))
        self.listPlayer = self.Player.media_list_player_new()
        self.listPlayer.set_media_list(self.mediaList)

    def play(self):
        self.listPlayer.play()

    def next(self):
        self.listPlayer.next()

    def pause(self):
        self.listPlayer.pause()

    def previous(self):
        self.listPlayer.previous()

    def stop(self):
        self.listPlayer.stop()


player = VLC()
player.addPlaylist()

while True:
    command = input("Enter:")
    if "play" in command:
        player.play()
    elif "pause" in command:
        player.pause()
    elif "stop" in command:
        player.stop()
    elif "next" in command:
        player.next()
    elif "previous" in command:
        player.previous()
