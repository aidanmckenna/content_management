# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = content_metadata_from_dict(json.loads(json_string))
#     result = content_item_from_dict(json.loads(json_string))
#     result = track_from_dict(json.loads(json_string))
#     result = create_track_request_model_from_dict(json.loads(json_string))
#     result = audio_classifier_set_type_from_dict(json.loads(json_string))
#     result = audio_classifier_set_from_dict(json.loads(json_string))
#     result = production_status_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


@dataclass
class ContentMetadata:
    date_created: str
    date_updated: str
    title: str
    author: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    docs: Optional[str] = None
    link: Optional[str] = None
    rights: Optional[str] = None
    tags: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ContentMetadata':
        assert isinstance(obj, dict)
        date_created = from_str(obj.get("dateCreated"))
        date_updated = from_str(obj.get("dateUpdated"))
        title = from_str(obj.get("title"))
        author = from_union([from_str, from_none], obj.get("author"))
        category = from_union([from_str, from_none], obj.get("category"))
        description = from_union([from_str, from_none], obj.get("description"))
        docs = from_union([from_str, from_none], obj.get("docs"))
        link = from_union([from_str, from_none], obj.get("link"))
        rights = from_union([from_str, from_none], obj.get("rights"))
        tags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("tags"))
        return ContentMetadata(date_created, date_updated, title, author, category, description, docs, link, rights, tags)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dateCreated"] = from_str(self.date_created)
        result["dateUpdated"] = from_str(self.date_updated)
        result["title"] = from_str(self.title)
        result["author"] = from_union([from_str, from_none], self.author)
        result["category"] = from_union([from_str, from_none], self.category)
        result["description"] = from_union([from_str, from_none], self.description)
        result["docs"] = from_union([from_str, from_none], self.docs)
        result["link"] = from_union([from_str, from_none], self.link)
        result["rights"] = from_union([from_str, from_none], self.rights)
        result["tags"] = from_union([lambda x: from_list(from_str, x), from_none], self.tags)
        return result


@dataclass
class ContentItem:
    id: str
    metadata: ContentMetadata

    @staticmethod
    def from_dict(obj: Any) -> 'ContentItem':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        metadata = ContentMetadata.from_dict(obj.get("metadata"))
        return ContentItem(id, metadata)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["metadata"] = to_class(ContentMetadata, self.metadata)
        return result


@dataclass
class AudioClassifierSet:
    audio_classifier_set_type: Any

    @staticmethod
    def from_dict(obj: Any) -> 'AudioClassifierSet':
        assert isinstance(obj, dict)
        audio_classifier_set_type = obj.get("AudioClassifierSetType")
        return AudioClassifierSet(audio_classifier_set_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AudioClassifierSetType"] = self.audio_classifier_set_type
        return result


@dataclass
class Track:
    classifier_sets: List[AudioClassifierSet]
    id: str
    metadata: ContentMetadata
    production_status: float

    @staticmethod
    def from_dict(obj: Any) -> 'Track':
        assert isinstance(obj, dict)
        classifier_sets = from_list(AudioClassifierSet.from_dict, obj.get("classifierSets"))
        id = from_str(obj.get("id"))
        metadata = ContentMetadata.from_dict(obj.get("metadata"))
        production_status = from_float(obj.get("productionStatus"))
        return Track(classifier_sets, id, metadata, production_status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["classifierSets"] = from_list(lambda x: to_class(AudioClassifierSet, x), self.classifier_sets)
        result["id"] = from_str(self.id)
        result["metadata"] = to_class(ContentMetadata, self.metadata)
        result["productionStatus"] = to_float(self.production_status)
        return result


@dataclass
class CreateTrackRequestModel:
    file: Any
    metadata: ContentMetadata
    classifier_sets: Optional[List[AudioClassifierSet]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CreateTrackRequestModel':
        assert isinstance(obj, dict)
        file = obj.get("file")
        metadata = ContentMetadata.from_dict(obj.get("metadata"))
        classifier_sets = from_union([lambda x: from_list(AudioClassifierSet.from_dict, x), from_none], obj.get("classifierSets"))
        return CreateTrackRequestModel(file, metadata, classifier_sets)

    def to_dict(self) -> dict:
        result: dict = {}
        result["file"] = self.file
        result["metadata"] = to_class(ContentMetadata, self.metadata)
        result["classifierSets"] = from_union([lambda x: from_list(lambda x: to_class(AudioClassifierSet, x), x), from_none], self.classifier_sets)
        return result


@dataclass
class AudioClassifierSetType:
    data_dict: str
    id: str
    software_version: str

    @staticmethod
    def from_dict(obj: Any) -> 'AudioClassifierSetType':
        assert isinstance(obj, dict)
        data_dict = from_str(obj.get("dataDict"))
        id = from_str(obj.get("id"))
        software_version = from_str(obj.get("softwareVersion"))
        return AudioClassifierSetType(data_dict, id, software_version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dataDict"] = from_str(self.data_dict)
        result["id"] = from_str(self.id)
        result["softwareVersion"] = from_str(self.software_version)
        return result


def content_metadata_from_dict(s: Any) -> ContentMetadata:
    return ContentMetadata.from_dict(s)


def content_metadata_to_dict(x: ContentMetadata) -> Any:
    return to_class(ContentMetadata, x)


def content_item_from_dict(s: Any) -> ContentItem:
    return ContentItem.from_dict(s)


def content_item_to_dict(x: ContentItem) -> Any:
    return to_class(ContentItem, x)


def track_from_dict(s: Any) -> Track:
    return Track.from_dict(s)


def track_to_dict(x: Track) -> Any:
    return to_class(Track, x)


def create_track_request_model_from_dict(s: Any) -> CreateTrackRequestModel:
    return CreateTrackRequestModel.from_dict(s)


def create_track_request_model_to_dict(x: CreateTrackRequestModel) -> Any:
    return to_class(CreateTrackRequestModel, x)


def audio_classifier_set_type_from_dict(s: Any) -> AudioClassifierSetType:
    return AudioClassifierSetType.from_dict(s)


def audio_classifier_set_type_to_dict(x: AudioClassifierSetType) -> Any:
    return to_class(AudioClassifierSetType, x)


def audio_classifier_set_from_dict(s: Any) -> AudioClassifierSet:
    return AudioClassifierSet.from_dict(s)


def audio_classifier_set_to_dict(x: AudioClassifierSet) -> Any:
    return to_class(AudioClassifierSet, x)


def production_status_from_dict(s: Any) -> float:
    return from_float(s)


def production_status_to_dict(x: float) -> Any:
    return to_float(x)
