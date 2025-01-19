from abc import ABC, abstractmethod

class MusicPlayer(ABC):

    @abstractmethod
    def play(self, track: str):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def pause(self):
        pass


class LocalMusicPlayer(MusicPlayer):

    def play(self, track: str):
        print(f"Now play the track {track}")

    def pause(self):
        print("The track is in on the pause}")

    def stop(self):
        print("The music stoped")


class SpotifyPlayer(MusicPlayer):

    def play(self, track: str):
        print(f"Now play the track {track}")

    def pause(self):
        print("The track is in on the pause}")

    def stop(self):
        print("The music stoped")


player = SpotifyPlayer()
player.play("Imagen Dragon - Thunder")