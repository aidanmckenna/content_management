from abc import ABC, abstractmethod
import eyed3

class Factory(ABC):
    @abstractmethod
    def make(self, args**)

class ITrackFactory(Factory):
    def make(self, title, author, file, metadata, data_sets):
        file_info = eyed3.load()

        
