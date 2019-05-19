import xml.etree.ElementTree as ET
from pathlib import Path

from my_av.models import Video, Genre, Actress


def import_nfo(path: Path) -> None:
    tree = ET.parse(path)
    root = tree.getroot()

    fanart_url = root.find('fanart/thumb').text
    if 'pl.' in fanart_url:
        poster_url = fanart_url.replace('pl.', 'ps.')
    else:
        poster_url = ''

    video, created = Video.objects.get_or_create(
        title=root.find('title').text,
        sample_url=root.find('trailer').text,
        plot=root.find('plot').text,
        runtime=root.find('runtime').text,
        fanart_url=fanart_url,
        poster_url=poster_url,
        dvd_id=root.find('id').text,
        release_date=root.find('releasedate').text,
        file_path=path,
    )
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

    # TODO: director, set, studio
    video.save()

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
