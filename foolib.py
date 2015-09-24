__author__ = 'Ashton'

from urllib import request as rqst
from downloader.dwdfoo import rqstfoo
from downloader.dwdtypes import files


def get_audio_list(post_id):
    audio_object_list = []
    request = rqstfoo.wall_get_by_id(post_id)
    response = rqst.urlopen(request)

    response_text = response.read()
    post_meta = eval(response_text)
    attachments = post_meta['response']['wall'][0]['attachments']

    if not len(attachments) and \
            not any(attachment['type'] == 'audio' for attachment in attachments):
        return audio_object_list

    audio_attachment_list = [attachment for attachment in attachments if \
                             attachment['type'] == 'audio']

    for attachment in audio_attachment_list:
        audio = attachment['audio']
        audio_id = str(audio['owner_id']) + '_' + str(audio['aid'])
        name = audio['artist'] + ' - ' + audio['title']

        audio_object = files.Audiofile(name, '', '', id=audio_id, owner_id=audio['owner_id'], \
                                       format='.mp3', duration=audio['duration'], composer=audio['artist'], \
                                       artist=audio['artist'], title=audio['title'], dwd_link=u'' + audio['url'].replace('\\', ''))
        audio_object_list.append(audio_object)

    return audio_object_list


def dwd_audio_files(audio_objects):
    dwd_folder = 'F:\\Pycharm\\Projects\\mdloader\\download\\ForCoding\\'
    for audio_object in list(audio_objects):
        print(audio_object.title)
        # Fix the unicode symbols in file name trouble
        result = rqst.urlretrieve(audio_object.dwd_link, dwd_folder + audio_object.artist + ' - ' + audio_object.title + '.mp3')
        print(result[0])

        print('Done')
        print('-' * 30)
