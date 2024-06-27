from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from schedule.models import EpisodeModel
from schedule.schemas import EpisodeSchema, EpisodeUpdateSchema

from db import db

blp = Blueprint("episodes", __name__, description="Operations on shows")


@blp.route("/episodes")
class EpisodeList(MethodView):
  
  @blp.response(200, EpisodeSchema(many=True))
  def get(self):
    return EpisodeModel.query.all()

  @blp.arguments(EpisodeSchema)
  @blp.response(201, EpisodeSchema)
  def post(self, episode_data):
    episode = EpisodeModel(**episode_data)
    
    try:
      db.session.add(episode)
      db.session.commit()
    except SQLAlchemyError:
      abort(500, message="An error occurred creating the episode.")
    return episode

@blp.route("/episodes/<int:episode_id>")
class Episode(MethodView):
  
  @blp.response(200, EpisodeSchema)
  def get(self, episode_id):
    episode = db.get_or_404(EpisodeModel, episode_id)
    return episode

  @blp.response(204)
  def delete(self, episode_id):
    episode = db.get_or_404(EpisodeModel, episode_id)
    db.session.delete(episode)
    db.session.commit()
  
  @blp.arguments(EpisodeUpdateSchema)
  @blp.response(200, EpisodeSchema)
  def put(self, episode_data, episode_id):
    episode = db.get_or_404(EpisodeModel, episode_id)
    if episode:
      episode.name = episode_data["name"]
      episode.date = episode_data["date"]
    else:
      episode = EpisodeModel(id=episode_id, **episode_data)
    
    db.session.add(episode)
    db.session.commit()
