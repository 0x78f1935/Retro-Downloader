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
            embeddir
        )
        Application.WrapperEntrypoint(*args)  # Starts download

    @property
    def is_running(self):
        """
        Indicate if the program is actively running
        """
        return Application.isRunning
