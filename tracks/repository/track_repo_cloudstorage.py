from tracks.domain import ContentItem, Track, ITrackRepository, ProductionStatus

class TrackRepositoryCloudStorage(ITrackRepository):
    def __init__(self, storage_bucket):
        self.bucket = storage_bucket

    def find(self, kwargs**):
        #returns list of resources
        matches = []
        blobs = self.bucket.get_blobs()

        if kwargs 

        for blob in blobs:
            track = json.loads(blob.metadata)
            if not check_is_match(track, kwargs):
                continue
            matches.append(track)
        return matches

    def list(self):
        blobs = self.bucket.get_blobs()
        tracks = []
        for blob in blobs:
            tracks.append(json.loads(blob.metadata))
        return tracks


    def get(self, id):
        blob = self.bucket.get_blob(id)
        track = json.loads(blob.metadata)
        #returns specific resource
        return track

    def remove(self, id):
        blob = self.bucket.get_blob(id)
        blob.delete()

    def update(self, track):
        blob = self.bucket.get_blob(track.id)
        blob.metadata = track.to_dict()
        blob.save()
        return 

    def insert(self, track, file):
        try:
            self.get(track.id)
        except:
            blob = self.bucket.blob(track.id)
            blob.metadata = track.to_dict()
            blob.upload_from_file(file)
            return True

    def get_download_url(self, id, expiration)
        blob = self.bucket.get_blob(id)
        download_url = blob.generate_signed_url(expiration=expiration)
        return download_url


def check_is_match(track, kwargs**):
    is_match = True
    for key, arg in kwargs:
        if not track[key] == arg:
            is_match = false
            break

    return is_match

def content_item_from_blob(blob):
    item = ContentItem(
        id=blob.id,
        name=blob.name,
        metadata=ContentMetadata.from_dict(blob.metadata)
    )
    return item

def content_item_to_blob(bucket, content_item):
    
    blob = bucket.blob(content_item.name)
    blob.metadata = content_item.metadata.to_dict()
    blob.id = content_item.id

    return blob
