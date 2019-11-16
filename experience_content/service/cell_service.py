from cms.shared.service.crud_service_interface import IResourceService

class CellService(IResourceService):

    @abstractmethod
    def find(self, kwargs**):
        pass

    @abstractmethod
    def get(self, id):
        #returns specific resource
        pass

    @abstractmethod
    def create(self, track_id, entrainmentDriverFrequency, args*):
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