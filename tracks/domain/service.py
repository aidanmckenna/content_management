from amb import ABC, abstractmethod

class ITrackService(ABC):

    @abstractmethod
    def find(self, kwargs**):
        pass
    @abstractmethod
    def get(self, id):
        #returns specific resource
        pass
    @abstractmethod
    def create(self, args*):
        #creates new resource with data
        pass
    @abstractmethod
    def update(self, id, args*):
        #replaces existing resource by id with data 
        pass
    @abstractmethod
    def patch(self, id, args*):
        #Merge new data into a resource
        pass
    @abstractmethod
    def remove(self, id, args*):
        #delete resource
        pass
    @abstractmethod
    def get_download_url(self,id, expiry):
        #returns a playable url for the track
        pass