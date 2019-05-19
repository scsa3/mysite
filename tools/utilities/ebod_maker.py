import sys
from pathlib import Path


def dummy_maker(source_directory: Path) -> None:
    for i in range(1, 101):
        Path('{}/ebod-{:0>3}.mp4'.format(source_directory, i)).touch()


if __name__ == '__main__':
    # arguments by hand
    target_str = '/Users/weihan/mysite/temp/movies'

    dummy_maker(Path(target_str))
