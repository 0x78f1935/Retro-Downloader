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