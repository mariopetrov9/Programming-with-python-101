from tabulate import tabulate
import json
import mutagen
from os import listdir
from os.path import isfile, join


class Song:

    def __init__(self, title, artist, album, length):
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__length = length

    def __str__(self):
        return "{} - {} from {} - {}".format(self.__artist, self.__title, self.__album, self.__length)

    def __repr__(self):
        return str()

    def __eq__(self, other):
        if self.__hash__() == other:
            return True

    def __hash__(self):
        return hash(self.__str__())

    def get_length(self):
        return self.__length

    def get_title(self):
        return self.__title

    def get_artist(self):
        return self.__artist

    def convert_to_seconds(self):
        splitted = [int(x) for x in self.get_length().split(":")]
        if len(splitted) == 3:
            return splitted[0] * 3600 + splitted[1] * 60 + splitted[2]
        if len(splitted) == 2:
            return splitted[0] * 60 + splitted[1]
        else:
            return splitted[0]

    def convert_to_minutes(self):
        return self.convert_to_seconds() / 60

    def convert_to_hours(self):
        return self.convert_to_seconds() // 3600

    def length(self, seconds=False, minutes=False, hours=False):
        if seconds:
            return self.convert_to_seconds()
        if minutes:
            return self.convert_to_minutes()
        if hours:
            return self.convert_to_hours()
        return self.get_length()


class PLayList:

    def __init__(self, name, repeat=False, shuffle=False):
        self._name = name
        self._repeat = repeat
        self._shuffle = shuffle
        self._songs = []
        self._song_index = 0

    def get_songs(self):
        return self._songs

    def add_song(self, song):
        self.get_songs().append(song)

    def remove_song(self, song):
        self._songs.remove(song)

    def add_songs(self, songs):
        self._songs += songs

    def next_song(self):
        if self._song_index >= len(self._songs) and self._repeat:
            self._song_index = 0
        song = self._songs[self._song_index]
        self._song_index += 1
        return song

    def pprint(self):
        table = []
        for song in self._songs:
            table_i = [song.get_artist(), song.get_title(), song.get_length()]
            table.append(table_i)
        headers = ["Artist", "Song", "Length"]
        print(tabulate(table, headers, tablefmt="orgtbl"))

    def get_dict(self):
        dict_of_songs = []
        for song in self._songs:
            dict_of_songs.append(song.__dict__)
        result = {
                "name": self._name,
                "repeat": self._repeat,
                "shuffle": self._shuffle,
                "song_index": self._song_index,
                "songs": dict_of_songs,
        }
        return result

    def save(self, file_name):
        with open(file_name, 'w') as f:
            json.dump(self.get_dict(), f, indent=4)

    def load_from_dict(self, data_d):
        playlist = PLayList("Name")
        songss = data_d.pop('songs')
        playlist.__dict__ = data_d
        playlist._songs = []
        for song in songss:
            newsong = Song(song["_Song__title"], song["_Song__artist"], song["_Song__album"], song["_Song__length"])
            newsong.__dict__ = song
            playlist.add_song(newsong)
        return playlist

    @staticmethod
    def load(self, filename):
        with open(filename, 'r') as f:
            data_d = json.load(f)
        return self.load_from_dict(data_d)


class MusicCrawler:
    def __init__(self, path):
        self.path = path
        self.data = []

    def only_files(self):
        return [f for f in listdir(self.path) if isfile(join(self.path, f))]

    def get_names(self):
        pass

    def generate_playlist(self):
        playlist = PLayList("NEW SONGS")
        for i in self.only_files():
            audio = mutagen.File(self.path + "/" + i, easy=True)
            song_length = int(audio.info.length)
            song = Song(audio['title'][0], audio['artist'][0], audio['album'][0], song_length)
            playlist.add_song(song)
        return playlist


def main():
    song = Song("Odin", "Manowar", "The Sons of Odin", "33:15")
    song2 = Song("Odin2", "Manowar2", "The Sons of Odin2", "1:30")
    playlist = PLayList("Random_play_list", repeat=True)
    songs = [song, song2]
    playlist.add_songs(songs)
    # playlist.pprint()
    # playlist.save("data.json")
    # new_playlist = playlist.load("data.json")
    # new_playlist.pprint()
    crawler = MusicCrawler("/home/krasi_b2/HackBulgaria/week07/MUSIC")
    music = crawler.generate_playlist()
    music.pprint()

if __name__ == '__main__':
    main()
