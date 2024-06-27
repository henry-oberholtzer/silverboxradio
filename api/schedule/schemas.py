from marshmallow import Schema, fields, validate, validates, ValidationError

from db import db
from .models import ShowModel

# Plain Schemas

class PlainEpisodeSchema(Schema):
  id = fields.Int(dump_only=True)
  name = fields.Str(validate=validate.Length(min=1, max= 100))
  date = fields.Date()
  
class PlainShowSchema(Schema):
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True, validate=validate.Length(min=1, max= 100))
  description = fields.Str(validate=validate.Length(max=500))
  duration = fields.Int(required=True)

# Update Schemas

class EpisodeUpdateSchema(PlainEpisodeSchema):
  class Meta:
    exclude = ["id"]
  
class ShowUpdateSchema(PlainShowSchema):
  class Meta:
    exclude = ["id"]

# Nested Schemas

class EpisodeSchema(PlainEpisodeSchema):
  show_id = fields.Int(required=True, load_only=True)
  show = fields.Nested(PlainShowSchema(), dump_only=True)
  
  @validates("show_id")
  def validates_show_id(self, show_id):
    if db.session.get(ShowModel, show_id) is None:
      raise ValidationError("Show does not exist.")
    
  

class ShowSchema(PlainShowSchema):
  episodes = fields.List(fields.Nested(PlainEpisodeSchema()), dump_only=True)
