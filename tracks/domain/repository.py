from abc import ABC, abstractmethod
class ITrackRepository:
    @abstractmethod
    def find(self, kwargs**):
        #returns list of resources
        pass

    @abstractmethod
    def get(self, id):
        #returns specific track
        pass
    @abstractmethod
    def get_download_url(self, id, expiration)
        pass

    @abstractmethod
    def remove(self, id):
        #delete resource
        pass

    @abstractmethod
    def save(self, track):
        pass

    @abstractmethod
    def insert(self, track):
        pass


class IContentRepository:
    @abstractmethod
    def find_by_name(self, name):
        pass

    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    def get_download_url(self, name, expiration):
        pass

    @abstractmethod
    def get_upload_url(self, name):
        pass

    @abstractmethod
    def insert(self, content_item, file=None):
        pass

    @abstractmethod
    def remove(self, name):
        pass