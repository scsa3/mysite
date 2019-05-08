from pathlib import Path
import xml.etree.ElementTree as ET
from my_av.models import Video, Genre, Actress


def nfo_importer(path: Path):
    tree = ET.parse(path)
    root = tree.getroot()

    fanart_url = root.find('fanart/thumb').text
    if 'pl.' in fanart_url:
        poster_url = fanart_url.replace('pl.', 'ps.')
    else:
        poster_url = ''

    video = Video(
        sample_url=root.find('trailer').text,
        fanart_url=fanart_url,
        poster_url=poster_url,
        dvd_id=root.find('id').text,
        title=root.find('title').text,
        release_date=root.find('releasedate').text,
    )
    video.save()
    for g in root.findall('genre'):
        if g.text:
            genre, created = Genre.objects.get_or_create(name=g.text)
            video.genre.add(genre)
    for a in root.findall('actor'):
        name = a.find('name').text or ''
        actress, created = Actress.objects.get_or_create(
            name=name,
            art_url=a.find('thumb').text
        )
        video.actress.add(actress)
    video.save()


if __name__ == '__main__':
    p = Path('/Users/weihan/mysite/temp/ABP-249.nfo')

# tree = ET.parse(p)
# root = tree.getroot()
# title = root.find('title').text
# trailer = root.find('trailer').text
# runtime = root.find('runtime').text
# release_date = root.find('releasedate').text
# fan_art = root.find('fanart/thumb').text
# genres = [g.text for g in root.findall('genre')]
# dvd_id = root.find('id').text
# director = root.find('director').text
