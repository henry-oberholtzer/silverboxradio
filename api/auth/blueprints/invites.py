from flask.views import MethodView
from flask_smorest import Blueprint, abort, Page
from flask_jwt_extended import jwt_required
from sqlalchemy import desc
from lib.permissions import admin_only
from db import db
from auth.models import InviteModel
from auth.schemas import InviteSchema, InvitePostSchema

class CursorPage(Page):
  @property
  def item_count(self):
    return self.collection.count()

blp = Blueprint("Invites", "invites", description="Operations on invites")

@blp.route("/invites")
class InviteList(MethodView):
  
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
  @blp.paginate(CursorPage)
  @jwt_required()
  def get(self):
    admin_only()
    return db.session.query(InviteModel).order_by(desc(InviteModel.created))

@blp.route("/invites/<int:invite_id>")
class Invite(MethodView):
  
  @blp.response(204)  
  @jwt_required()
  def delete(self, invite_id):
    admin_only()
    invite = db.get_or_404(InviteModel, invite_id)
    db.session.delete(invite)
    db.session.commit()
    
