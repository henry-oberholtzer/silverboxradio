from flask_smorest import abort
from flask_jwt_extended import get_jwt, get_jwt_identity

def is_user_or_admin(user_id):
  current_id = get_jwt_identity()
  is_admin = get_jwt().get("is_admin")
  if current_id != user_id and is_admin is False:
    return abort(401, message="Unauthorized.")
  return is_admin

def admin_only():
  is_admin = get_jwt().get("is_admin")
  if not is_admin:
    return abort(401, message="Unauthorized.")
  return get_jwt_identity()
