# Users
GET `/users` - AUTH ONLY
  - Get all users
  - Active
GET `/users/<username>` - AUTH ONLY
  - Get a specific user, gets associated shows
  - Active
DELETE `/users/<username>` - EXACT USER OR ADMIN ONLY
  - Deletes a user from the website
  - Active

# Access
PUT `/users/<int:user_id>/access/` - ADMIN ONLY
  - Set whether a user is admin

# Invites
GET `/invites/` - ADMIN ONLY
  - Get a list of all sent invites to the station
GET `/invites/<invite_id>` - ADMIN ONLY
  - Get a specific invite
POST `/invites/` - ADMIN ONLY
  - Create an invite for a user
DELETE `/invites/<invite_id>` - ADMIN ONLY
  - Remove an invite

# Shows
GET `/shows`
  - Gets all shows
POST `/shows` - ADMIN ONLY
  - Create and schedule a new show
PUT `/shows/`
  - Update a specific show
  - Assign to users
  - Change description
GET `/shows/<show_id>`
  - Gets a specific show
  - Include most recent episodes of the show
  - Filters for season?

# Episodes
GET `/episodes`
  - List of all episodes, probably 25 most recent
GET `/episodes/<episode_id>`
  - Get a specific episode
  - Includes show track list

# Plays
GET `/plays`
 - Gets a list of recent plays
 - Can query based on between different times
GET `/plays/<play_id>`
  - Get a specific play instance

# Tracks
GET `/tracks`
  - Gets tracks played on the station
GET `/tracks/<track_id>`
  - Gets a specific track played on the station
  - Includes the artist associated
  - Includes plays

# Artists
GET `/artists`
  - Gets artists played on the station
GET `/artists/<artist_id>`
  - Gets a specific artist played on the station
