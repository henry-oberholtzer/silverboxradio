from flask import session
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from schedule.models import ShowModel
from schedule.schemas import ShowSchema, ShowUpdateSchema
from sqlalchemy.exc import SQLAlchemyError

from db import db

blp = Blueprint("shows", __name__, description="Operations on shows")


@blp.route("/shows")
class ShowList(MethodView):
  
  @blp.response(200, ShowSchema(many=True))
  def get(self):
    return ShowModel.query.all()


  @blp.response(201, ShowSchema)
  @blp.arguments(ShowSchema)
  @jwt_required()
  def post(self, show_data):
    
    show = ShowModel(**show_data)
    try:
      db.session.add(show)
      db.session.commit()
    except SQLAlchemyError:
      abort(500, message="An error has occured creating the show.")

    return show
  

@blp.route("/shows/<int:show_id>")
class Show(MethodView):
  
  @blp.response(200, ShowSchema)
  def get(self, show_id):
    show = db.get_or_404(ShowModel, show_id)
    return show

  @blp.response(204)
  @jwt_required()
  def delete(self, show_id):
    show = db.get_or_404(ShowModel, show_id)
    db.session.delete(show)
    db.session.commit()
    
  @blp.arguments(ShowUpdateSchema)
  @blp.response(200, ShowSchema)
  @jwt_required()
  def put(self, show_data, show_id):
    show = db.get_or_404(ShowModel, show_id)
    if show:
      show.name = show_data["name"]
      show.description = show_data["description"]
      show.duration = show_data["duration"]
    else:
      show = ShowModel(id=show_id, **show_data)
    
    db.session.add(show)
    db.session.commit()
    return show
