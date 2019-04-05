from random import randint
import operator
import json
import os.path
import os

class TypeError(Exception):
    pass

class Song:
    def __init__(self,title,artist,album,length):
        self.title = title
        self.artist = artist
        self.album = album
        self._length = length

    def __str__(self):
        return '{} - {} from {} - {}'.format(self.artist,self.title,self.album,self._length)

    def __eq__(self,other):
        return isinstance(self,type(other)) and self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.title,self.artist,self.album,self._length))

    def length(self,**kwargs):
        llist = self._length.split(':')
        llist = list(reversed(llist))
        for key,value in kwargs.items():
            if key == 'seconds' and value ==True:
                seconds = 0
                for index,item in enumerate(llist):
                    seconds += int(item)*60**index
                return seconds
            elif key == 'minutes' and value == True:
                llist= llist[1:]
                minutes = 0
                for index,item in enumerate(llist):
                    minutes += int(item)*60**index
                return minutes
            elif key =='hours' and value == True:
                if len(llist) == 3:
                    return int(llist[-1])
                else:
                    return 0

        return str(self._length)

class Playlist:
    def __init__(self,name,repeat=False,shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs= list()
        self.current_song_index = 0
        self.played = list()

    def add_song(self,song):
        if type(song) is not Song:
            raise TypeError('Only songs can be added to the playlist!')
        if song not in self.songs:
            self.songs.append(song)
        self.current_song_index = 0

    def add_songs (self,songs):
        for song in songs:
            self.add_song(song)

    def remove_song(self,song):
        self.songs.remove(song)

    def total_length(self):
        total_seconds=0
        for song in self.songs:
            total_seconds += song.length(seconds=True)

        hours = total_seconds//3600
        minutes = total_seconds//60%60
        seconds = total_seconds%60
        return '%02d:%02d:%02d'%(hours,minutes,seconds)

    def next_song(self):
        next_playing = None
        if self.repeat == True and self.current_song_index == len(self.songs) - 1:
            self.current_song_index = 0
            next_playing = self.songs[self.current_song_index]
        elif self.shuffle == True:
            count = len(self.songs)
            index = randint(0,count-1)
            if list(sorted(self.played,key=operator.attrgetter('artist'))) == list(sorted(self.songs,key=operator.attrgetter('artist'))):
                next_playing = self.songs[index]
            else:
                next_playing = self.songs[index]
                while next_playing in self.played:
                    index = randint(0,count-1)
                    next_playing = self.songs[index]
                self.current_song_index = index
                self.played.append(next_playing)
        else:
            next_playing = self.songs[self.current_song_index+1]
            self.current_song_index += 1
            self.played.append(next_playing)
        return next_playing

    def artists(self):
        histogram = dict()
        for song in self.songs:
            if song.artist in histogram.keys():
                histogram[song.artist] += 1
            else :
                histogram[song.artist] = 1
        return histogram

    def pprint_playlist(self):
        print('| Artist  |       Song       |  Length  |')
        print('| --------|------------------|----------|')
        for song in self.songs:
            print('| {:^7} | {:^16} | {:^8} |'.format(song.artist,song.title,song._length))

    def dictionary(self):
        songs_dicts = [song.__dict__ for index,song in enumerate(self.songs)]
        played_dicts = [played_song.__dict__ for index,played_song in enumerate(self.played)]
        data = dict()
        data['name'] = self.name
        data['repeat'] = self.repeat
        data['shuffle'] = self.shuffle
        data['songs'] = songs_dicts
        data['current_song_index'] = self.current_song_index
        data['played'] = played_dicts

        return data

    def save(self):
        save_path = 'playlist_data/'
        data = self.dictionary()
        filename = self.name
        filename = filename.replace(' ','-')
        complete_path = os.path.join(save_path,filename + '.json')
        os.makedirs(os.path.dirname(complete_path), exist_ok=True)
        with open(complete_path,'w') as json_file:
            json.dump(data,json_file,indent=4)

    @staticmethod
    def load(filename):
        save_path = 'playlist_data/'
        complete_path = os.path.join(save_path,filename)
        with open(complete_path,'r') as json_file:
            data = json.load(json_file)
        songs = list()
        for index,song in enumerate(data['songs']):
            s=Song(title = song['title'],artist = song['artist'],album = song['album'],length = song['_length'])
            songs.append(s)

        played = list()
        for index,played_song in enumerate(data['played']):
            s = Song(title = played_song['title'],artist = played_song['artist'],album = played_song['album'], length = played_song['_length'])
            played.append(s)

        playlist = Playlist(data['name'],data['repeat'],data['shuffle'])
        playlist.songs = songs
        playlist.played = played
        playlist.current_song_index = data['current_song_index']

        return playlist

