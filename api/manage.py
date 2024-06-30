import getpass
from flask.cli import FlaskGroup

from auth.models import UserModel
from passlib.hash import pbkdf2_sha256
from db import db
from app import create_app

cli = FlaskGroup(create_app=create_app)

@cli.command("create_admin")
def create_admin():
    """Creates the admin user."""
    email = input("Enter email address: ")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Enter password again: ")
    if password != confirm_password:
        print("Passwords don't match")
        return 1
    try:
        user = UserModel(
            email=email,
            username=username,
            password=pbkdf2_sha256.hash(password),
            is_admin=True)
        print(user)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        print("Couldn't create admin user:", e)

if __name__ == "__main__":
    cli()
