import re
from pathlib import Path

from mutagen.easyid3 import EasyID3

music_folder = Path(r'Z:\music\old_japanese')


def get_title_artist(name_split):
    if len(name_split) == 2:
        return name_split[1], name_split[0]
    else:
        return name_split, name_split


def update_tag(mp3):
    loaded = EasyID3(mp3.absolute())
    name_no_mp3 = mp3.name.replace('.mp3', '')
    name_split = name_no_mp3.split('-')
    title_artist = get_title_artist(name_split)

    loaded['title'] = title_artist[0]
    loaded['artist'] = title_artist[1]
    loaded['album'] = find_album(name_no_mp3, title_artist[1])

    loaded.save()


def main():
    # [mp3.rename(music_folder / replace_name(mp3.name)) for mp3 in music_folder.iterdir()]
    [update_tag(mp3) for mp3 in music_folder.iterdir()]


def replace_name(old_name):
    return re.sub(r'(.+)(-.{11}\.mp3)', '\g<1>.mp3', old_name)


def find_album(name, default_name):
    if name.find('(') > -1:
        strip = re.sub(r'.+\((.+?)\).*', '\g<1>', name).strip(' ')
        print(strip)
        return strip
    else:
        return default_name


if __name__ == '__main__':
    main()
    # find_album('')
