6-26-24
  - Basic structure started.
  - Write tests for shows
  - Write tests for episodes
  - Begin auth section, refactor code to be more expandable

6-28-24
  - User authentication has been added
  - Admin permissions have been added
  - JWT tokens are active
  - Permissions have been set

6-29-24
  - Client skeleton has been established
  - Initial connection between api and client established.

6-30-24
  - Switching to config objects for Flask app
  - Send store JWT tokens as cookies

TO DO:



DEPLOYMENT TO DO:
  - Set config to load from a config file with `str(secrets.SystemRandom().getrandbits(128))`
  - "Your Flask application can implicitly refresh JWTs that are close to expiring, which simplifies the logic of keeping active users logged in. More on this in the next section!"
https://pypi.org/project/sqlalchemy-easy-softdelete/
https://medium.com/@jesscsommer/how-to-serialize-and-validate-your-data-with-marshmallow-a815b2276a
