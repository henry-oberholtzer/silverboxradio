from marshmallow import Schema, fields

class ShowSchema(Schema):
  id = fields.Str(dump_only=True)
  name = fields.Str(required=True)
  description = fields.Str()
  duration = fields.Int(required=True)

class ShowUpdateSchema(Schema):
  name = fields.Str(required=True)
  description = fields.Str()
  duration = fields.Int(required=True)
