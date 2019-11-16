from track_service.domain.model import Track, CreateTrackRequestModel
from flask import Blueprint, app, request
from repository.track_repo_cloudstorage import TrackRepositoryCloudStorage
from service import TrackService 

from google.cloud import storage

blueprint = Blueprint('track_server', __name__)

track_repo = TrackRepositoryCloudStorage()
track_service = TrackService(track_repo)

@blueprint.route('/', methods=['GET'])
def list_tracks():
    return json.dumps(track_service.find())

@blueprint.route('/<id>', methods=['GET'])
def get_track(id):
    return json.dumps(track_service.get(id))

@blueprint.route('/',methods=['POST'])
def create_track():
    payload_json = request.get_json()
    file = request.files['file']
    req = CreateTrackRequestModel.from_json(payload_dict)

    result = track_service.create(metadata=req.metadata, file=file, classifier_sets=req.classifier_sets,)
    resp = json.dumps(result)
    return resp

"""
@blueprint.route('/<id>', methods=['PUT'])
def update_track(id):
    pass

@blueprint.route('/<id>',methods=['PATCH'])
def patch_track(id)

@blueprint.route('/<id>', methods=['DELETE'])
def delete_track(id):
    return json.dumps(track_service.remove(id))
"""

@blueprint.route('/<id>/downloadUrl',methods=['GET'])
def get_track_download_url(id):
    return json.dumps(track_service.get_download_url(id))

@blueprint.route('/build')
def render_template

"""
@blueprint.route('/<track_id>/classifierSets/<classifier_type_id>/generate')
def generate_track_classifier_set(track_id, classifier_type_id):
    pass
"""

if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint('track_server',route_prefix='/tracks')
