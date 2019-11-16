from tracks.domain import ContentItem, Track, ITrackRepository, ProductionStatus


class TrackRepositoryRTDB(ITrackRepository):
    def __init__(self, rtdb_reference, content_repository):
        self.ref = rtdb_reference.child('tracks')
        self.file_repo = file_repository

    def find(self, kwargs**):
        #returns list of resources
        pass

    def get(self, id):
        #returns specific resource
        track_dict = self.ref.child(id).get()
        track = Track.from_dict(track_dict)
        track.source = self.content_repo.find_by_name(track.source.name)
        return track

    def get_download_url(self, id, expiration)
        track_dict = self.ref.child(id).get()
        track = Track.from_dict(track_dict)


    def remove(self, id):
        #delete resource
        track = self.get(id)
        self.file_repo.remove(track.content_item.name)
        self.ref.child(id).remove()
        return True

    def update(self, track):

    def insert(self, track, file=None):
        track.id = self.ref.push(track.to_dict()).key
        self.content_repo.insert()
        if file is not None:

        return True


class TrackRepositoryRTDBCloudStorage(ITrackRepository):
    def __init__(self, rtdb_reference, storage_client):
        self.ref = rtdb_reference.child('tracks')
        self.bucket = storage_client.create_bucket("")

    def find(self, kwargs**):
        #returns list of resources
        pass

    def get(self, id):
        #returns specific resource
        track_dict = self.ref.child(id).get()
        track = Track.from_dict(track_dict)
        return track

    def remove(self, id):
        #delete resource
        track = self.get(id)
        self.file_repo.remove(track.content_item.name)
        self.ref.child(id).remove()
        return True

    def update(self, track):



    def insert(self, track, file):
        new_ref = self.ref.push()

        track.id = 


        blob = self.bucket.blob(key)
        blob.upload_from_file(file)

        return True


