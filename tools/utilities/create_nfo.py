from pathlib import Path
import subprocess


def create_nfo(path: Path) -> None:
    subprocess.run(
        [
            '/Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/bin/java',
            '-jar',
            '/Users/weihan/mysite/tools/utilities/JAVMovieScraper.jar',
            '-scrape',
            'r18',
            path.absolute()
        ]
    )


if __name__ == '__main__':
    file_path = Path('/Users/weihan/mysite/temp/movies-import/ABP-249.m4v')
    create_nfo(file_path)
