# Retro-Downloader

Asset download tool specifically written for [Retro-CMS](https://github.com/0x78f1935/Retro-CMS)

## QuickStart

This application is a command line tool, therefor to use it, open a terminal and navigate to te folder which holds
`RetroDownloader.exe`. You can run `RetroDownloader.exe --help` for a overview of available commands.

```
.\RetroDownloader.exe --help
RetroDownloader 1.0.0
undeƒined

  -v, --verbose      (Default: false) Output debug stdout information.

  -o, --out          (Default: .) Set the output folder.

  -b, --build        (Default: latest) Build version of Game, found at https://habboassets.com/swfs.

  -a, --agent        (Default: Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/534.2.1 (KHTML, like Gecko) Chrome/35.0.822.0 Safari/534.2.1) Set custom user agent.

  -w, --workers      (Default: 2) Total concurrent downloaders used for downloading data.

  -e, --embeddir     (Default: ) Manipulate the embedded directory. Delimiter: ";". See Readme.

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

  -I, --archive      Download Archive.

  -L, --catalog      Download Catalog Icons.

  -A, --all          Download All.

  --help             Display this help screen.
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


class DownloadWrapper(Application):
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
        doQuest: bool,
        doArchive: bool,
        doCatalog: bool,
        embeddir: str
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
            doArchive (bool): Download Archive
            doCatalog (bool): Download Catalog Icons
            embeddir (str): Set subdir in embedded application
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
            doArchive,
            doCatalog,
            embeddir
        )
        Application.WrapperEntrypoint(*args)  # Starts download

    @property
    def is_running(self):
        """
        Indicate if the program is actively running
        """
        return Application.isRunning

```

For an example on how to utilize the code snippet above, please refer to [this specific line](https://github.com/0x78f1935/Retro-CMS/blob/refactor/all-in-one/backend/tasks/downloader/__init__.py#L50) in the source code of the CMS.

## Settings

| Shortcut 	| Flag        	| Type   	| Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            	|
|----------	|-------------	|--------	|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| -v       	| --verbose   	| bool   	| Output debug stdout information. Can be very noisy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    	|
| -o       	| --out       	| string 	| Set the output folder where the downloaded files will be downloaded to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                	|
| -b       	| --build     	| string 	| Build version of Game, found at [habbo-assets](https://habboassets.com/swfs). When set to "latest" the downloader will download the latest version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    	|
| -a       	| --agent     	| string 	| Set a custom user agent, defaults to: `Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/534.2.1 (KHTML, like Gecko) Chrome/35.0.822.0 Safari/534.2.1`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              	|
| -w       	| --workers   	| int    	| The more workers you have, the faster your download goes. should be thread safe.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       	|
| -e       	| --embeddir  	| string 	| If you desire to embed this application, there is a chance the application is unable to find the `Resources` folder. For example, If you start a main thread in `/myApp` and the dll is located in `/myApp/tools/RetroDownloader/RetroDownloader.dll`, you might want to use this option. The DLL will in this case error because it's unable to find the `Resources` folder located in `/myApp/Resources`. Why is the DLL looking in `/myApp` and not in `/myApp/tools/RetroDownloader`? The main thread started in the `/myApp` location.  A hacky way is to start the main application in the `/myApp/tools/RetroDownloader` by just adding `cd../../.. && <start application>`, but this won't work in all situations. **embeddir** generates a path between te Resource folder and the application based on the delimiter `;`.  To fix our situation in the example we simply assign this parameter with the value `tools;RetroDownloader`.  The DLL will do the rest which looks something like this: `/myApp/<embeddir>/Resources` -> `/myApp/tools/RetroDownloader/Resources`. 	|
|          	|             	|        	|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        	|
| -R       	| --articles  	| bool   	| Download all available articles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        	|
| -B       	| --badges    	| bool   	| Download all available badges                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          	|
| -C       	| --clothing  	| bool   	| Download all available clothing                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        	|
| -E       	| --effects   	| bool   	| Download all available effects                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         	|
| -F       	| --furniture 	| bool   	| Download all available furniture                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       	|
| -O       	| --gordon    	| bool   	| Download all available production data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 	|
| -G       	| --gamedata  	| bool   	| Download all available gamedata                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        	|
| -H       	| --hotelview 	| bool   	| Download all available hotel views                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     	|
| -P       	| --parts     	| bool   	| Download all available badge parts                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     	|
| -T       	| --pets      	| bool   	| Download all available pet assets                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      	|
| -S       	| --sound     	| bool   	| Download all available mp3 assets                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      	|
| -Q       	| --quests    	| bool   	| Download all available quest assets                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    	|
| -I       	| --archive    	| bool   	| Download all available archived assets                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -L       	| --catalog    	| bool   	| Download all available catalog icon assets                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|          	|             	|        	|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        	|
| -A       	| --all       	| bool   	| Download all available assets. When set, other capital parameters will be ignored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     	|

