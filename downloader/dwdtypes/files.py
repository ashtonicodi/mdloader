"""files.py
Class contains a set of data types for the files,
such as audio files and images. The most basic class - "File",
which inherited the rest.
"""
__author__ = 'Ashton'

class File:
    """Basic class"""

    def __init__(self, name, create_time, description):
        """
        To create an instance of the class, you must pass to the constructor:
        :param name: the name of the file (string)
        :param create_time: The creation (format string dd-mm-yyyy hh:mm:ss)
        :param description: a text description of the file (string)
        :return:
        """
        self.__name = name
        self.__create_time = create_time
        self.__description = description

    def __str__(self):
        return ""

    def get_name(self):
        return self.__name.capitalize()

    def get_create_time(self):
        return self.__create_time

    def get_descrition(self):
        return self.__description


class Audiofile(File):
    def __init__(self, name, create_time, description, **rows):
        """
        :param name: the name of the file (string)
        :param create_time: The creation (format string dd-mm-yyyy hh:mm:ss)
        :param description: a text description of the file (string)
        :param rows: dictionary of audio

        :param format: audio format(string)
        :param duration: duration of audio(integer)
        :param size: size of audio(integer)
        :param bitrate: bitrate of audio(integer)
        :param composer: composer(string)
        :param artist: artist(string)
        :param title: title of audio(string)
        :param dwd_link: download link audio(string)
        :param post_id: post id(string)
        :param id: audio id(string)
        """
        super().__init__(name, create_time, description)
        self.format = rows.get('format', '.mp3')
        self.duration = rows.get('duration', 0)
        self.size = rows.get('size', 0)
        self.bitrate = rows.get('bitrate', 0)
        self.composer = rows.get('composer', 'unknown')
        self.artist = rows.get('artist', 'unknown')
        self.title = rows.get('title', 'unnamed')
        self.dwd_link = rows.get('dwd_link', '')
        self.post_id = rows.get('post_id', '')
        self.id = rows.get('id', '')

    def __str__(self):
        return self.artist + ' - ' + self.title


class Imagefile(File):
    def __init__(self, name, create_time, description, **rows):
        """
        :param name: the name of the file (string)
        :param create_time: The creation (format string dd-mm-yyyy hh:mm:ss)
        :param description: a text description of the file (string)
        :param rows: dictionary of image

        :param width: width of image(integer)
        :param height: height of image(integer)
        :param dwd_link: download link(string)
        """
        super().__init__(name, create_time, description)
        self.width = rows.get('width', 0)
        self.height = rows.get('height', 0)
        self.dwd_link = rows.get('dwd_link', '')