from tracks.domain.track import Track
from interface import ITrackService
import uuid



class TrackService(ITrackService):
    def __init__(self, repo):
        self.repo = repo

    def find(self, kwargs**):
        return self.repo.list(kwargs)

    def get(self, id):
        #returns specific resource
        return self.repo.get(id)

    def create(self, metadata,file, classifier_sets=None):
        #creates new resource with data
        unique_id = uuid.uuid1()
        track = Track(id=unique_id, metadata=metadata, classifier_sets=classifier_sets, production_status='awaiting_review')
        self.repo.insert(track, file)
        return

    def update(self, id, data, args*):
        #replaces existing resource by id with data 
        pass

    def patch(self, id, data, args*):
        #Merge new data into a resource
        pass

    def remove(self, id, args*):
        #delete resource
        self.repo.remove(id)

    def get_download_url(self, id, expiration_timestamp):
        self.repo.get_download_url()

