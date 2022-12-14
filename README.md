# Retro-Downloader

Asset download tool specifically written for [Retro-CMS](https://github.com/0x78f1935/Retro-CMS)

## QuickStart

This application is a command line tool, therefor to use it, open a terminal and navigate to te folder which holds
`RetroDownloader.exe`. You can run `RetroDownloader.exe --help` for a overview of available commands.

```
.\RetroDownloader.exe --help
RetroDownloader 1.0.0
Copyright (C) 2022 RetroDownloader

  -v, --verbose      (Default: false) Set output to verbose messages.

  -o, --out          (Default: .) Set the output folder.

  -b, --build        (Default: latest) Build version of Game, found at https://habboassets.com/swfs.

  -a, --agent        (Default: Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/534.2.1 (KHTML, like Gecko)
                     Chrome/35.0.822.0 Safari/534.2.1) Set custom user agent.

  -w, --workers      (Default: 2) Total concurrent downloaders used for downloading data.

  -r, --revision     (Default: false) Save output in revision structure.

  -R, --articles     Download Articles.

  -B, --badges       Download Badges.

  -C, --clothing     Download Clothing.

  -E, --effects      Download effects.

  -F, --furniture    Download Furniture.

  -O, --gordon       Download gordon data.

  -G, --gamedata     Download gamedata.

  -H, --hotelview    Download hotelview.

  -P, --parts        Download Badgeparts.

  -T, --pets         Download Pets.

  -S, --sound        Download Sound.

  -Q, --quests       Download Quests.

  -A, --all          Download All.

  --help             Display this help screen.

  --version          Display version information.
```

For example, to download all files to the relative directory `./tmp` with 25 workers,
```
RetroDownloader.exe -A --out ./tmp -v -w 25
```

## Advance usage Python

Believe it or not, This application also provides an entrypoint for Python. It's a bit more strict with parameters, but
it totally works.

Install the python library `pythonnet` -> `pip install pythonnet`.
The following snippet is how you could utilize the provided `.DLL` within your python snippet.
```python
# -*- mode: python ; coding: utf-8 -*-
# Official wrapper for: https://github.com/0x78f1935/Retro-Downloader
# ---------------
# """
from pythonnet import load

load("coreclr")
import clr
import sys
from pathlib import Path, PurePosixPath

# Directory Path to RetroDownloader.dll. (Not the file itself)
assembly_path = PurePosixPath(Path(__file__).resolve().parent.parent).as_posix()

sys.path.append(assembly_path)
clr.AddReference("RetroDownloader")

from RetroDownloader import Application



class DownloadWrapper(object):
    def __init__(
        self,
        debug: bool,
        outputPath: str,
        buildVersion: str,
        agent: str,
        maxConcurrentWorkers: int,
        downloadAll: bool,
        doArticles: bool,
        doBadges: bool,
        doClothing: bool,
        doEffects: bool,
        doFurniture: bool,
        doGamedata: bool,
        doGordon: bool,
        doHotelView: bool,
        doParts: bool,
        doPets: bool,
        doSound: bool,
        doQuest: bool
    ) -> None:
        """
        Python wrapper for RetroDownloader. All arguments must be provided. Otherwise it won't work.
        Args:
            debug (bool): When True stdout will contain verbose messages,
            outputPath (str): Path which will be used to download files to,
            buildVersion (str): Build version of Game, found at https://habboassets.com/swfs,
            agent (str): User agent,
            maxConcurrentWorkers (int): Total concurrent workers which download the download queue,
            downloadAll (bool): When True, download all other parameters,
            doArticles (bool): Download Articles,
            doBadges (bool): Download Badges,
            doClothing (bool): Download Clothing,
            doEffects (bool): Download Effects,
            doFurniture (bool): Download Furniture,
            doGamedata (bool): Download GameData,
            doGordon (bool): Download Gordon production data,
            doHotelView (bool): Download Hotel Views,
            doParts (bool): Download Badgeparts,
            doPets (bool): Download Pets,
            doSound (bool): Download Sounds,
            doQuest (bool): Download Quests, 
        """
        args = (
            debug,
            outputPath,
            buildVersion,
            agent,
            maxConcurrentWorkers,
            downloadAll,
            doArticles,
            doBadges,
            doClothing,
            doEffects,
            doFurniture,
            doGamedata,
            doGordon,
            doHotelView,
            doParts,
            doPets,
            doSound,
            doQuest,
        )
        Application.WrapperEntrypoint(*args)  # Starts download
```