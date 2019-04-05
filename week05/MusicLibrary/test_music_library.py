from playlist import *
import unittest 

class TestMusicLibrary(unittest.TestCase):
    def test_when_adding_song(self):
        playlist = Playlist(name='Music')
        playlist.add_song(Song(title='Sorry',artist='Beyonce',album='Lemonade',length='4:25'))
        playlist_dictionary = playlist.dictionary()
        expected_result = [{'title':'Sorry','artist':'Beyonce','album':'Lemonade','_length':'4:25'}]
        self.assertEqual(playlist_dictionary['songs'],expected_result)

    def test_when_adding_existing_song_to_playlist(self):
        playlist = Playlist(name='Music')
        playlist.add_song(Song(title='Sorry',artist='Beyonce',album='Lemonade',length='4:25'))
        playlist.add_song(Song(title='Sorry',artist='Beyonce',album='Lemonade',length='4:25'))
        playlist_dictionary = playlist.dictionary()
        expected_result = [{'title':'Sorry','artist':'Beyonce','album':'Lemonade','_length':'4:25'}]
        self.assertEqual(playlist_dictionary['songs'],expected_result)


    def test_when_addind_multiple_songs(self):
        playlist = Playlist(name='Music')
        playlist.add_songs([Song(title='Sorry',artist='Beyonce',album='Lemonade',length='4:25'),
            Song(title='Mockingbird',artist='Eminem',album='Encore',length='4:18')])
        playlist_dictionary = playlist.dictionary()
        expected_result = [{'title':'Sorry','artist':'Beyonce','album':'Lemonade','_length':'4:25'},
        {'title':'Mockingbird','artist':'Eminem','album':'Encore','_length':'4:18'}]
        self.assertEqual(playlist_dictionary['songs'],expected_result)

    def test_when_getting_song_length_in_seconds(self):
        song = Song(title='Mockingbird',artist='Eminem',album='Encore',length='4:18')
        expected_result = 258
        self.assertEqual(song.length(seconds=True),expected_result)

    def test_when_getting_song_length_in_minutes(self):
        song = Song(title='Mockingbird',artist='Eminem',album='Encore',length='1:44:18')
        expected_result = 104
        self.assertEqual(song.length(minutes=True),expected_result)

    def test_when_getting_song_length_in_hours(self):
        song = Song(title='Mockingbird',artist='Eminem',album='Encore',length='1:44:18')
        expected_result = 1
        self.assertEqual(song.length(hours=True),expected_result)

    def test_when_getting_total_length_of_playlist(self):
        playlist = Playlist('Music')
        playlist.add_songs([Song(title='Sorry',artist='Beyonce',album='Lemonade',length='4:25'),
            Song(title='Mockingbird',artist='Eminem',album='Encore',length='4:18'),
            Song(title='Fall',artist='Eminem',album='Kamikaze',length='5:11')])
        expected_result = '00:13:54'
        self.assertEqual(playlist.total_length(),expected_result)

    def test_when_counting_artists_songs(self):
        playlist = Playlist('Music')
        playlist.add_songs([Song(title='Sorry',artist='Beyonce',album='Lemonade',length='4:25'),
            Song(title='Mockingbird',artist='Eminem',album='Encore',length='4:18'),
            Song(title='Fall',artist='Eminem',album='Kamikaze',length='5:11')])
        expected_result = {'Eminem':2,'Beyonce':1}
        self.assertEqual(playlist.artists(),expected_result)

    def test_when_removing_song_from_playlist(self):
        playlist = Playlist('Music')
        song1,song2,song3 = Song(title='Sorry',artist='Beyonce',album='Lemonade',length='4:25'),Song(title='Mockingbird',artist='Eminem',album='Encore',length='4:18'),Song(title='Fall',artist='Eminem',album='Kamikaze',length='5:11')
        playlist.add_songs([song1,song2,song3])
        playlist.remove_song(song3)
        playlist_dictionary = playlist.dictionary()
        expected_result = [{'title':'Sorry','artist':'Beyonce','album':'Lemonade','_length':'4:25'},
            {'title':'Mockingbird','artist':'Eminem','album':'Encore','_length':'4:18'}]
        self.assertEqual(playlist_dictionary['songs'],expected_result)

    def test_when_saving_and_loading_playlist_json(self):
        playlist = Playlist('My Music')
        song1,song2,song3 = Song(title='Sorry',artist='Beyonce',album='Lemonade',length='4:25'),Song(title='Mockingbird',artist='Eminem',album='Encore',length='4:18'),Song(title='Fall',artist='Eminem',album='Kamikaze',length='5:11')
        playlist.add_songs([song1,song2,song3])
        playlist.save()
        new_playlist = Playlist.load('My-Music.json')
        self.assertEqual(new_playlist.name,playlist.name)

    def test_existance_of_saved_playlists(self):
        os.path.isdir('./playlist_data')
    
if __name__=='__main__':
    unittest.main()
