6-26-24
  - Basic structure started.
  - Write tests for shows
  - Write tests for episodes
  - Begin auth section, refactor code to be more expandable

TO DO:
  - Add user authentication
  - Set authentication permissions and current user only permissions
  - Set admin permissions
  - Add "created_on" field, create a base model?

DEPLOYMENT TO DO:
  - Set config to load from a config file with `str(secrets.SystemRandom().getrandbits(128))`
  - "Your Flask application can implicitly refresh JWTs that are close to expiring, which simplifies the logic of keeping active users logged in. More on this in the next section!"
https://pypi.org/project/sqlalchemy-easy-softdelete/
https://medium.com/@jesscsommer/how-to-serialize-and-validate-your-data-with-marshmallow-a815b2276a
