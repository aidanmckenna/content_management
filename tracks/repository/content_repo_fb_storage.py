from domain.repository import IFileRepository
from domain.model import ContentItem

class FileRepository_Firestore(IFileRepository):
    def __init__(self, firestore_bucket):
        self.bucket = firestore_bucket

    def get_by_id(self, id):
        blobs = self.bucket.list_blobs()
        for blob in blobs:
            if blob.id == id:
                the_blob_i_want = self.get_by_name(blob.name)
                return content_item_from_blob(the_blob_i_want)
        raise Exception("Content item not found")

    def get_by_name(self, name):
        item_blob = self.bucket.get_blob(name)
        item = content_item_from_blob(item_blob)
        return item

    def insert(self, content_item, file):
        blob = content_item_to_blob(self.bucket, content_item)
        blob.upload_from_file(file)
        return

    def remove(self, name):
        blob = self.bucket.get_blob(name)
        blob.delete()
        return


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
        



