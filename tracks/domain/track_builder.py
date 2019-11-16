from abc import ABC, abstractmethod

class ITrackBuilder(ABC):

    def setFile(self, file):


def getFileInfo(file):

    info = eyed3.load(file_path).info
