GET `/users` - AUTH_ONLY
  - Get all users
GET `/users/<username>` - AUTH_ONLY
  - Get a specific user, gets associated shows
DELETE `/users/<username>` - ADMIN ONLY
  - Soft deletes a user from the website

GET `/invites/` [ADMIN ONLY]
  - Get a list of all sent invites to the station
GET `/invites/<invite_id>` [ADMIN ONLY]
  - Get a specific invite
POST `/invites/` [ADMIN ONLY]
  - Create an invite for a user
DELETE `/invites/<invite_id>` [ADMIN ONLY]

GET `/shows`
  - Gets all shows
GET `/shows/<show_id>`
  - Gets a specific show
  - Include most recent episodes of the show
  - Filters for season?
GET `/episodes`
  - List of all episodes, probably 25 most recent
GET `/episodes/<episode_id>`
  - Get a specific episode
  - Includes show track list
GET `/tracks`
  - Gets tracks played on the station
GET `/tracks/<track_id>`
  - Gets a specific track played on the station
  - Includes the artist associated
  - Includes plays
GET `/artists`
  - Gets artists played on the station
GET `/artists/<artist_id>`
  - Gets a specific artist played on the station
