class AudioFileMixin:
    """
    Mixin providing audio playback functionality.
    """

    def play_audio(self):
        """
        Return formatted audio playback information.

        Raises:
            ValueError:
                If no audio files are available.
        """
        if not hasattr(self, "audio_files") or not self.audio_files:
            raise ValueError("No audio files available.")

        tracks1 = "\n\n".join(f"<{track}>" for track in self.audio_files)

        return (
            f"Audio playing for <{self.__class__.__name__}>\n\n"
            f"{tracks1}\n"
        )


class VideoFileMixin:
    """
    Mixin class that provides video playback functionality.

    Classes inheriting from this mixin are expected to define
    a `video_files` attribute containing a list of video file names.

    Methods:
        play_video():
            Prints all available video files for the object.
            Raises:
                AttributeError: If no video files are available.
    """
    def play_video(self):
        """
        Return formatted video playback information.

        Raises:
            ValueError:
                If no video files are available.
        """
        if not hasattr(self, "video_files") or not self.video_files:
            raise ValueError("No video files available.")

        videos = "\n\n".join(f"<{video}>" for video in self.video_files)

        return (
            f"Playing video for <{self.__class__.__name__}>\n\n"
            f"{videos}\n"
        )


class MediaPlayer(AudioFileMixin):
    """
    Media player class with audio playback support.

    Inherits:
        AudioFileMixin

    Attributes:
        audio_files (list[str]):
            Collection of audio tracks available to the media player.
    """
    def __init__(self, audio_files):
        self.audio_files = audio_files

class Laptop(AudioFileMixin, VideoFileMixin):
    """
    Laptop class capable of playing both audio and video files.

    Inherits:
        AudioFileMixin
        VideoFileMixin

    Attributes:
        audio_files (list[str]):
            Collection of audio tracks.
        video_files (list[str]):
            Collection of video files.
    """
    def __init__(self, audio_files, video_files):
        self.audio_files = audio_files
        self.video_files = video_files


tracks = ["track1.mp3", "track2.mp3"]

movies = ["movie.mp4", "trailer.mov"]


player = MediaPlayer(tracks)

laptop = Laptop(tracks, movies)

print(player.play_audio())

print(laptop.play_audio())
print(laptop.play_video())
