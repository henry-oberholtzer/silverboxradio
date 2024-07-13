from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from lib.permissions import admin_only
from db import db
from auth.models import InviteModel
from auth.schemas import InviteSchema, InvitePostSchema

blp = Blueprint("Invites", "invites", description="Operations on invites")

@blp.route("/invites")
class Invite(MethodView):
  
  @blp.arguments(InvitePostSchema)
  @blp.response(201, InviteSchema)
  @jwt_required()
  def post(self, invite_data):
    admin = admin_only()
    
    invite = InviteModel(
      email=invite_data["email"],
      owner_id=admin
    )
    db.session.add(invite)
    db.session.commit()
    return invite

  @blp.response(200, InviteSchema(many=True))
  @jwt_required()
  def get(self):
    admin = admin_only()
    return InviteModel.query.all()
