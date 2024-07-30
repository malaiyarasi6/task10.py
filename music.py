class Audio:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)

    def average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.audios = []
        self.ratings = []

    def add_audio(self, audio):
        self.audios.append(audio)

    def search_audio(self, name):
        for audio in self.audios:
            if audio.name.lower() == name.lower():
                return audio
        return None

    def add_rating(self, rating):
        self.ratings.append(rating)

    def average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

class MusicPlayer:
    def __init__(self):
        self.playlists = []

    def create_playlist(self, name, genre):
        playlist = Playlist(name, genre)
        self.playlists.append(playlist)
        return playlist

    def add_audio_to_playlist(self, playlist_name, audio):
        playlist = self.search_playlist_by_name(playlist_name)
        if playlist:
            playlist.add_audio(audio)
        else:
            print("Playlist not found")

    def search_audio_by_name(self, name):
        for playlist in self.playlists:
            audio = playlist.search_audio(name)
            if audio:
                return audio
        return None

    def search_playlist_by_name(self, name):
        for playlist in self.playlists:
            if playlist.name.lower() == name.lower():
                return playlist
        return None

    def add_rating_to_audio(self, audio_name, rating):
        audio = self.search_audio_by_name(audio_name)
        if audio:
            audio.add_rating(rating)
        else:
            print("Audio not found")

    def add_rating_to_playlist(self, playlist_name, rating):
        playlist = self.search_playlist_by_name(playlist_name)
        if playlist:
            playlist.add_rating(rating)
        else:
            print("Playlist not found")

# Sample usage
player = MusicPlayer()

# Creating playlists
pop_playlist = player.create_playlist("Pop Hits", "Pop")
rock_playlist = player.create_playlist("Rock Anthems", "Rock")

# Adding audios
audio1 = Audio("Song 1", "http://example.com/song1")
audio2 = Audio("Song 2", "http://example.com/song2")

player.add_audio_to_playlist("Pop Hits", audio1)
player.add_audio_to_playlist("Rock Anthems", audio2)

# Searching audios and playlists
print(player.search_audio_by_name("Song 1"))  # Should print the audio object
print(player.search_playlist_by_name("Pop Hits"))  # Should print the playlist object

# Adding ratings
player.add_rating_to_audio("Song 1", 5)
player.add_rating_to_playlist("Pop Hits", 4)

# Getting average ratings
print(audio1.average_rating())  # Should print the average rating of audio1
print(pop_playlist.average_rating())  # Should print the average rating of pop_playlist