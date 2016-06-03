import unittest
from song import Song, PLayList


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Odin", "Manowar", "The Sons of Odin", "1:30:00")
        self.song2 = Song("Odin2", "Manowar2", "The Sons of Odin2", "1:30")
        self.playlist = PLayList("Random_play_list", repeat=True)
        self.songs = [self.song, self.song2]

    def test_length(self):
        self.assertEqual(self.song.length(seconds=True), 5400)
        self.assertEqual(self.song.length(minutes=True), 90)
        self.assertEqual(self.song.length(hours=True), 1)
        self.assertEqual(self.song.length(), "1:30:00")

    def test_add_song(self):
        self.playlist.add_song(self.song)
        self.assertIn(self.song, self.playlist.get_songs())

    def test_remove_song(self):
        self.playlist.add_song(self.song)
        self.playlist.remove_song(self.song)
        self.assertNotIn(self.song, self.playlist.get_songs())

    def test_add_songs(self):
        self.playlist.add_songs(self.songs)
        self.assertIn(self.song, self.playlist.get_songs())
        self.assertIn(
            self.song2, self.playlist.get_songs())

    def test_next_song(self):
        self.playlist.add_songs(self.songs)
        self.assertIn(self.playlist.next_song(), self.songs)

    def test_next_song_many_times(self):
        self.playlist.add_songs(self.songs)
        self.assertEqual(self.playlist.next_song(), self.song)
        self.assertEqual(self.playlist.next_song(), self.song2)
        self.assertEqual(self.playlist.next_song(), self.song)

    # def test_next_song_many_times_repeat_on(self):
    #     playlist = Playlist()
    #     self.playlist.add_songs(self.songs)
    #     self.assertIn(self.playlist.next_song(), self.song)
    #     self.assertIn(self.playlist.next_song(), self.song2)


if __name__ == '__main__':
    unittest.main()
