import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint("seasons", __name__, description="Operations on seasons")

@blp.route("/season/<string:season_id>")
class Season(MethodView):
  def get(self, season_id):
    pass

  def delete(self, season_id):
    pass
