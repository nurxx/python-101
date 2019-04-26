import unittest 
from playlist import *

class TestMusicLibrary(unittest.TestCase):
    def setUp(self):
        self.song1 = Song(title='Sorry',artist='Beyonce',album='Lemonade',length='4:25')
        self.song2= Song(title='Mockingbird',artist='Eminem',album='Encore',length='1:44:18')
        self.song3= Song(title='Fall',artist='Eminem',album='Kamikaze',length='5:11')
        self.playlist = Playlist('My Music')
        self.playlist.add_songs([self.song1,self.song2,self.song3])

    def test_when_adding_song(self):
        playlist = Playlist(name='Music')
        playlist.add_song(self.song1)
        playlist_dictionary = playlist.dictionary()
        expected_result = [{'title':'Sorry','artist':'Beyonce','album':'Lemonade','_length':'4:25'}]
        self.assertEqual(playlist_dictionary['songs'],expected_result)

    def test_when_adding_existing_song_to_playlist(self):
        playlist = Playlist(name='Music')
        playlist.add_song(self.song1)
        playlist_dictionary = playlist.dictionary()
        expected_result = [{'title':'Sorry','artist':'Beyonce','album':'Lemonade','_length':'4:25'}]
        self.assertEqual(playlist_dictionary['songs'],expected_result)


    def test_when_addind_multiple_songs(self):
        playlist = Playlist(name='Music')
        playlist.add_songs([self.song1,self.song2])
        playlist_dictionary = playlist.dictionary()
        expected_result = [{'title':'Sorry','artist':'Beyonce','album':'Lemonade','_length':'4:25'},
        {'title':'Mockingbird','artist':'Eminem','album':'Encore','_length':'1:44:18'}]
        self.assertEqual(playlist_dictionary['songs'],expected_result)

    def test_when_getting_song_length_in_seconds(self):
        expected_result = 6258
        self.assertEqual(self.song2.length(seconds=True),expected_result)

    def test_when_getting_song_length_in_minutes(self):
        expected_result = 104
        self.assertEqual(self.song2.length(minutes=True),expected_result)

    def test_when_getting_song_length_in_hours(self):
        expected_result = 1
        self.assertEqual(self.song2.length(hours=True),expected_result)

    def test_when_getting_total_length_of_playlist(self):
        expected_result = '01:53:54'
        self.assertEqual(self.playlist.total_length(),expected_result)

    def test_when_counting_artists_songs(self):
        expected_result = {'Eminem':2,'Beyonce':1}
        self.assertEqual(self.playlist.artists(),expected_result)

    def test_when_removing_song_from_playlist(self):
        playlist = Playlist('Music')
        playlist.add_songs([self.song1,self.song2,self.song3])
        playlist.remove_song(self.song3)
        playlist_dictionary = playlist.dictionary()
        expected_result = [{'title':'Sorry','artist':'Beyonce','album':'Lemonade','_length':'4:25'},
            {'title':'Mockingbird','artist':'Eminem','album':'Encore','_length':'1:44:18'}]
        self.assertEqual(playlist_dictionary['songs'],expected_result)

    def test_when_saving_and_loading_playlist_json(self):
        self.playlist.save()
        new_playlist = Playlist.load('My-Music.json')
        self.assertEqual(new_playlist.name,self.playlist.name)

    def test_existance_of_saved_playlists(self):
        self.assertTrue(True,os.path.isdir('./playlist_data'))
    
if __name__=='__main__':
    unittest.main()
