
@dataclass
class CreateTrackRequest:
    classifier_sets: List[AudioClassifierSet]
    file: Any
    metadata: ContentMetadata
    title: str

    @staticmethod
    def from_dict(obj: Any) -> 'CreateTrackRequest':
        assert isinstance(obj, dict)
        classifier_sets = from_list(AudioClassifierSet.from_dict, obj.get("classifierSets"))
        file = obj.get("file")
        metadata = ContentMetadata.from_dict(obj.get("metadata"))
        title = from_str(obj.get("title"))
        return CreateTrackRequest(classifier_sets, file, metadata, title)

    def to_dict(self) -> dict:
        result: dict = {}
        result["classifierSets"] = from_list(lambda x: to_class(AudioClassifierSet, x), self.classifier_sets)
        result["file"] = self.file
        result["metadata"] = to_class(ContentMetadata, self.metadata)
        result["title"] = from_str(self.title)
        return result
