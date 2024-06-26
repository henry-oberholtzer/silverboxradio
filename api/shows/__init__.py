import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schema import ShowSchema, ShowUpdateSchema

blp = Blueprint("shows", __name__, description="Operations on shows")


@blp.route("/shows")
class ShowList(MethodView):
  
  @blp.response(200, ShowSchema(many=True))
  def get(self):
    pass

  @blp.arguments(ShowSchema)
  def post(self, show_data):
    pass
  
  @blp.arguments(ShowUpdateSchema)
  @blp.response(200, ShowSchema)
  def put(self, show_data, show_id):
    pass

@blp.route("/shows/<string:show_id>")
class Show(MethodView):
  
  @blp.response(200, ShowSchema)
  def get(self, show_id):
    pass

  def delete(self, show_id):
    pass
